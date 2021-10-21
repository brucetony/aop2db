"""Collection of methods for parsing and downloading."""
import os
import logging
import pickle

import GEOparse as gp

from typing import Set
from tqdm import tqdm
from configparser import ConfigParser

from aop2db.constants import DATABASE
from aop2db.defaults import SOFT_DIR, CONFIG, CONN_STRING, TIME_DIR

logger = logging.getLogger(__name__)


def __check_config_file() -> bool:
    if not os.path.isfile(CONFIG):  # then make empty file
        with open(CONFIG, 'w'):
            pass
        return False

    return True


def get_conn() -> str:
    """Retrieves CONN in the config file. If no config file, it makes one and sets the CONN to SQLite by default."""
    __check_config_file()
    config = ConfigParser()
    config.read(CONFIG)

    if not config.has_section(DATABASE):
        config.add_section(DATABASE)
        config.set(DATABASE, "CONN", CONN_STRING)
        with open(CONFIG, 'w') as cf:
            config.write(cf)

        return CONN_STRING

    else:
        return config.get(DATABASE, "CONN")


def set_conn(conn_string: str) -> None:
    get_conn()  # To make sure config file is there
    config = ConfigParser()
    config.read(CONFIG)
    config.set(DATABASE, "CONN", conn_string)
    with open(CONFIG, 'w') as cf:
        config.write(cf)


def download_soft_files(series_ids: Set[str], verbose: bool = False) -> int:
    """Downloads the SOFT files for each GEO Series provided

    :series_id Set[str] Set of GEO Series IDs.
    """
    to_download = set()
    silent = not verbose
    for geo_id in series_ids:
        if not os.path.isfile(os.path.join(SOFT_DIR, f"{geo_id}_family.soft.gz")):
            to_download.add(geo_id)

    logger.warning(f"Downloading {len(to_download)} SOFT files.")

    downloaded = 0
    for geo_id in tqdm(to_download, desc="Downloading SOFT files"):
        gp.get_GEO(geo=geo_id, destdir=SOFT_DIR, silent=silent)
        downloaded += 1

    return downloaded


def load_pickle(pickle_file: str, directory: str = TIME_DIR) -> dict:
    """Loads the stored metadata from a pickle file."""
    pickle_path = os.path.join(directory, pickle_file)

    with open(pickle_path, 'rb') as pf:
        data = pickle.load(pf)

    return data


def write_results_to_pickle(phenos: dict, gse_id: str, output_dir: str = TIME_DIR) -> None:
    """Write extracted metadata to a pickle file. Used due to tuples.

    Parameters
    ----------
    phenos: dict
        Dictionary containing time results of interest.

    gse_id: str
        GEO Series Accession ID.

    output_dir: str
        Directory to write pickle files to.
    """
    cache_path = os.path.join(output_dir, f"{gse_id}.p")
    with open(cache_path, 'wb') as md_file:
        pickle.dump(phenos, md_file)


def get_gse_ids() -> tuple:
    """Returns a list of GSE IDs of interest."""
    return tuple([soft_file.split("_")[0] for soft_file in os.listdir(SOFT_DIR)])

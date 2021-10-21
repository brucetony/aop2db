"""Test the AOP module methods and submodules."""

from aop2db.orm.manager import engine, CONN
from aop2db.aop.importer import import_aop_data
from sqlalchemy_utils import database_exists


class TestImporter:
    """Tests for the importer submodule."""

    def test_importer(self):
        """Test the general import method."""
        # import_aop_data()

        assert database_exists(CONN)

        required_tables = {
            "aop",
            "aop_bio_action",
            "aop_bio_event",
            "aop_bio_object",
            "aop_bio_process",
            "aop_cell_term",
            "aop_chemical",
            "aop_chemical_synonym",
            "aop_kers_aop_association",
            "aop_key_event",
            "aop_key_event_aop_association",
            "aop_key_event_relationship",
            "aop_life_stage",
            "aop_life_stage_aop_association",
            "aop_life_stage_ker_association",
            "aop_life_stage_key_event_association",
            "aop_organ_term",
            "aop_sex",
            "aop_sex_aop_association",
            "aop_sex_ker_association",
            "aop_sex_key_event_association",
            "aop_stressor",
            "aop_stressor_aop_association",
            "aop_taxonomy",
            "aop_taxonomy_ker_association",
            "aop_taxonomy_key_event_association",
            "key_event_bio_event_association",
            "stressor_chemical_association",
            "stressor_key_event_association",
        }

        # Check tables are all there
        conn = engine.connect()
        if engine.name == "sqlite":
            query = "SELECT name FROM sqlite_master WHERE type='table';"

        else:
            query = "SHOW TABLES;"

        tables_in_db = set([x[0] for x in conn.execute(query).fetchall()])

        missing_tables = required_tables - tables_in_db
        assert not missing_tables

        # Check none of the tables are empty
        for table_name in required_tables:
            entry = conn.execute(f"SELECT * FROM {table_name} LIMIT 1;").fetchone()
            assert entry


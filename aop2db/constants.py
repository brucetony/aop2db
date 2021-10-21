"""String definitions."""

# GEO String constants
SERIES = 'series'
PLATFORM = 'platform'
SAMPLE = 'sample'

NEG = 'neg'
CHECK = 'check'
POS = 'pos'

TITLE = 'title'
SUMMARY = 'summary'
HIT = 'hit'
EVALUATION = 'evaluation'

DATABASE = "DATABASE"

# AOP String constants
ID = "@id"
AOP_ID = "aop_id"
APPLICABILITY = "applicability"
TAXONOMY = "taxonomy"
EVIDENCE = "evidence"
SEX = "sex"
LIFESTAGE = "life-stage"
LAST_MODIFIED = "last_modified"
LM_TIMESTAMP = "last-modification-timestamp"
CREATION = "creation"
CREATION_TIMESTAMP = "creation-timestamp"

# REGEX
# Group 1 will be the numbers (if any) and group 2 will be units (e.g. dpf, hours post fertilization, etc)
TIME_REGEX = "(?:(\d*(?:\.\d+)?)\s*)?([h|d]\.*p\.*f\.*|(?:hours|days|minutes) (?:post|after) fertili[z|s]ation)"
TREATMENT_REGEX = "treat|expos|drug|compound|toxic|agent|chemical"
DECHORIONATED_REGEX = "([D|d]e-?)?([C|c]hor[o|i]o?n)"
GSM_REGEX = "GSM[0-9]+"

# API
SCAIVIEW_API = "http://api.dev.zet-o-map.k8s.bio.scai.fraunhofer.de/api/v6/documents/GEO%3A{}"
TAX_ID_LOOKUP = "https://rest.ensembl.org/taxonomy/id/{}?content-type=application/json"

# AOP Download
AOP_XML_DOWNLOAD = "https://aopwiki.org/downloads/aop-wiki-xml-2021-07-01.gz"

# Developmental Stages
STAGES = {
    0.2: "Zygote:1-cell",
    0.75: "Cleavage:2-cell",
    1: "Cleavage:4-cell",
    1.25: "Cleavage:8-cell",
    1.5: "Cleavage:16-cell",
    1.75: "Cleavage:32-cell",
    2: "Cleavage:64-cell",
    2.25: "Blastula:128-cell",
    2.5: "Blastula:256-cell",
    2.75: "Blastula:512-cell",
    3: "Blastula:1k-cell",
    3.3: "Blastula:High",
    3.7: "Blastula:Oblong",
    4: "Blastula:Sphere",
    4.3: "Blastula:Dome",
    4.7: "Blastula:30%-epiboly",
    5.3: "Blastula:50%-epiboly",
    5.7: "Gastrula:Germ-ring",
    6: "Gastrula:Shield",
    8: "Gastrula:75%-epiboly",
    9: "Gastrula:90%-epiboly",
    10: "Gastrula:Bud",
    11: "Segmentation:1-4 somites",
    12: "Segmentation:5-9 somites",
    14: "Segmentation:10-13 somites",
    16: "Segmentation:14-19 somites",
    17: "Segmentation:20-25 somites",
    19: "Segmentation:26+ somites",
    24: "Pharyngula:Prim-5",
    30: "Pharyngula:Prim-15",
    36: "Pharyngula:Prim-25",
    42: "Pharyngula:High-pec",
    48: "Hatching:Long-pec",
    60: "Hatching:Pec-fin",
    72: "Larval:Protruding-mouth",
    96: "Larval:Day 4",
    120: "Larval:Day 5",
    144: "Larval:Day 6",
}

# /usr/bin/env python


def get_versions():
    return versions[0]["number"]


versions = [
    {"number": "1.0.4",
     "features": [
         "support fq head with @XXXX.XXXX.X",
         "automatically skip empty fq files for spades",
     ]},
    {"number": "1.0.3a",
     "features": [
         "gunzip",
     ]},
    {"number": "1.0.3",
     "features": [
         "accept .gz/.zip files as input",
         "logging errors as utf8",
     ]},
    {"number": "1.0.2a",
     "features": [
         "prompt failure in Utilities/slim_fastg.py",
     ]},
    {"number": "1.0.2",
     "features": [
         "removing duplicates become a parameter to control the memory usage.",
     ]},
    {"number": "1.0.1a",
     "features": [
         "Fix the bug of running spades.py with --continue when no output file exists.",
     ]},
    {"number": "1.0.1",
     "features": [
         "Add default reference (Library/SeqReference).",
     ]}
]
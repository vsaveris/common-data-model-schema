'''
File name: cdm.py
    Example usage code of the Common Data Model Schema Extraction class.
           
Author: Vasileios Saveris
email: vsaveris@gmail.com

License: MIT

Date last modified: 03.04.2020

Python Version: 3.7
'''

import cdm
import sys

c = cdm.CDM(path = sys.argv[1], core_path = sys.argv[2], base_path = sys.argv[3])

# Schema can be accessed by: c.getSchema()

c.printSchema()
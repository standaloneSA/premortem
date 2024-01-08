#!/usr/bin/env python3

import sys
from PyPDF2 import PdfReader
import yaml
import json

def pprint(data):
    print(json.dumps(data))

FILE = "reports/AIR2301.pdf"

f = open(FILE, 'rb')

pdf = PdfReader(f)
for page in pdf.pages:
    print(type(page))
    print(page)
    sys.exit()
#pprint(pdf.metadata)
sys.exit()
item_count = 0
for item in pdf.outline:
    print(f"Item {item_count}: {item}")
    item_count += 1
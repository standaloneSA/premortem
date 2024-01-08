#!/usr/bin/env python3
""" Kicks off the training process """

import sys
import json
from datastructures import Analysis
from ingest import determine_filetype
from ai_interface import analyze_report
import yaml

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <path-to-postmortem>')
        sys.exit(1)
    
    path = sys.argv[1]
    print("Extracting text")
    text = determine_filetype(path)

    print("Analyzing report")
    ai_output = analyze_report(text).replace("\n", "")
    
    doc_dict = None
    try:
        doc_dict = json.loads(ai_output)
    except json.decoder.JSONDecodeError:
        print("Error decoding json. Here is the raw value")
        print(ai_output)
    except Exception as err:
        print("Error decoding json. Here is the raw value")
        print(ai_output)
    
    
    if doc_dict:
        print(yaml.safe_dump(doc_dict))


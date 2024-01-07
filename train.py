#!/usr/bin/env python3
""" Kicks off the training process """

import sys
from datastructures import Analysis
from ingest import determine_filetype
from ai_interface import analyze_report

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(f'Usage: {sys.argv[0]} <path-to-postmortem>')
        sys.exit(1)
    
    path = sys.argv[1]
    text = determine_filetype(path)

    ai_output = analyze_report(text)
    print(ai_output)


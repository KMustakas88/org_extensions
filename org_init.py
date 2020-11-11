#!/usr/local/bin/python3

import argparse
import inspect
import os
from pathlib import Path
import sys

# read in cli args
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_name', required=True, help='name of org file')
parser.add_argument('-c', '--category', required=True, choices=['dst','att','daily'])
args = parser.parse_args()

# set file name to user input
file_name = args.file_name
category = args.category

# chose an org header based on user input
#if args.package
header = f"""
        #+title:
        #+description:
        #+setupfile: ~/org/setup_themes/read_the_docs/theme-readtheorg.setup
        #+export_file_name: ~/org/exports/{category}/{file_name}
        #+bind: org-export-publishing-directory "~/org/exports/{category}"
        #+options: num:nil"""

# set full file path
path = f'{os.getenv("HOME")}/org/org_files/{category}/{file_name}.org'

# confirm file name doesn't exist
existing_files = [str(file) for file in Path(f'{os.getenv("HOME")}/org/org_files/{category}').iterdir()]

if path in existing_files:
    sys.exit('File name already exists. Please rename file')



# write header out to new file
# cleandoc function removes all leading and trailing whitespace
with open(path, 'w') as f:
    f.write(inspect.cleandoc(header))

# open newly created org file with Emacs
os.system(f'open -a "Emacs" {path}')

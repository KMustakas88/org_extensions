#!/usr/local/bin/python3

import argparse
import inspect
import os

# read in cli args
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file_name', required=True, help='name of org file')
parser.add_argument('-p', '--package', choices='docs')
args = parser.parse_args()

# set file name to user input
file_name = args.file_name

# chose an org header based on user input
if args.package:
    header = f"""
        #+title:
        #+description:
        #+setupfile: /Users/mustakas/Documents/org/setup_themes/theme-readtheorg.setup
        #+bind: org-export-publishing-directory "./exports"
        #+options: num:nil"""
else:
    header = f"""
        #+title:
        #+description:"""

# set full file path
path = f'/Users/mustakas/Documents/att/projects/org_files/{file_name}.org'

# write header out to new file
# cleandoc function removes all leading and trailing whitespace
with open(path, 'w') as f:
    f.write(inspect.cleandoc(header))

# open newly created org file with Emacs
os.system(f'open -a "Emacs" {path}')
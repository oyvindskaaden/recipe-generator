#!/usr/bin/env python3

import os
import argparse

import json

from jinja2 import Environment, select_autoescape
from jinja2.environment import Template
from jinja2.loaders import FileSystemLoader


parser = argparse.ArgumentParser(description="Generate recipes within a directory tree to different formats")
parser.add_argument('source_dir', metavar='dir', help="The directory in which the source files are located.")
parser.add_argument('-t', dest="template_folder", metavar='template_dir', default='templates', help='Folder for the different templates.')

args = parser.parse_args()

#print(args.source_dir)

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

filelist = []
dirlist = []
for root, dirs, files in os.walk(f"./{args.source_dir}"):
    for file in files:
        if(file.endswith(".json")):
            filelist.append(os.path.join(root,file))
            if root not in dirlist:
                dirlist.append(root)

print(filelist)
print(dirlist)

formatlist = []
#for root, dirs, files in os.walk(args.template_dir):
#    print()

for dir in dirlist:
    os.makedirs(os.path.join("./_generated", dir), mode=0o775, exist_ok=True)

def generateTemplate(template: Template):
    file = open("examples/pizzadeig.json")

    data = json.load(file)

    file.close()

    return template.render(
        title=data['title'], 
        description=data['description'],  
        interactive=True,
        portions=data['portions'],
        ingredients=data['ingredients'],
        steps=data['steps']
    )

#print(generateTemplate(env.get_template("jekyll/jekyll.md.jinja")))
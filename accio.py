#!/usr/bin/env python3
# python accio.py [options] [language] [tag]

import argparse
import json
import subprocess

def install_tool(language, import_path, name):
    # Determine the installation command based on the language of the tool
    if language == "go":
        cmd = ["go", "install", "-v", import_path]
    elif language == "pip":
        cmd = ["pip", "install", "--upgrade", import_path]
    elif language == "python":
        cmd = ["git", "clone", import_path]
    elif language == "npm":
        cmd = ["npm", "install", "-g", import_path]
    elif language == "yarn":
        cmd = ["yarn", "global", "add", import_path]
    elif language == "brew":
        cmd = ["brew", "install", import_path]
    elif language == "apt":
        cmd = ["sudo", "apt", "install", import_path]
    elif language == "apk":
        cmd = ["sudo", "apk", "add", import_path]
    elif language == "pacman":
        cmd = ["sudo", "pacman", "-S", import_path]
    else:
        print(f"Unknown language: {language}")
        return

    # Run the installation command
    try:
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode("utf-8")
        print(f"Installed {name}:")
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Error installing {name}: {e.output.decode('utf-8')}")

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--all", action="store_true", help="Install all tools regardless of language or tag")
parser.add_argument("--language", nargs="?", help="Only install tools with this language")
parser.add_argument("--tag", nargs="?", help="Only install tools with this tag")
args = parser.parse_args()

# Read in the JSON file
with open("tools.json", "r") as f:
    tools = json.load(f)

# Install the requested tools
for tool in tools:
    name = tool["name"]
    import_path = tool["import_path"]
    language = tool["language"]
    tags = tool["tags"]

    if args.all or (args.language is None or language == args.language) and (args.tag is None or args.tag in tags):
        install_tool(language, import_path, name)


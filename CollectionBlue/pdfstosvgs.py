#/usr/bin/env python

"""
This script converts PDFs exported by Adobe Illustrator
to clean SVGs using Inkscape
"""

import os
import sys

if sys.platform.startswith('win32'):
    # Inkscape's path is different on Windows
    # So a different command has to be used
    for filename in os.listdir("."):
        svg_name = filename.replace(".pdf", ".svg")
        command = "C:\Program Files\Inkscape\inkscape.exe " + filename + " -l -o " + svg_name
        print(command)
        os.system(command)
        print("Command executed successfully!")
else:
    # On all Unix-based system and cywin
    for filename in os.listdir("."):
        svg_name = filename.replace(".pdf", ".svg")
        command = "inkscape " + filename + " -l -o " + svg_name
        print(command)
        os.system(command)
        print("Command executed successfully!")


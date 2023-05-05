#! /bin/bash

echo "Only run this file in the working directory that it exists in."
echo "Press enter to continue"
read -p ""
python3 python/generate_foodcompat_html.py

#!/bin/bash

# Change directory to the code_segments folder
# cd code_segments

# Loop through all the files in the folder
for i in {1..7}; do
    # Run the command `python cfgGen.py code_segments/1.py`
    python cfgGen.py code_segments/$i.py
done

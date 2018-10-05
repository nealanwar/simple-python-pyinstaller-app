#!/bin/bash

sudo apt-get install python
python collection.py ${SETTINGS} ${TRAIN} ${TEST}

#!/bin/bash

apt-get install python
python collection.py ${SETTINGS} ${TRAIN} ${TEST}

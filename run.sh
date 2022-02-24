#!/bin/bash

cd $HOME/kioskTest

export DISPLAY=:0.0
xhost si:localuser:root
sudo python3 $HOME/kioskTest/src/app.py
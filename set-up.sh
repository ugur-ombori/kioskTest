#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip curl #install pip3 and curl
sudo -H pip3 install --upgrade pip #update pip3
pip3 install -r requirements.txt #install required packages(list can be shorten)
sudo apt-get update && sudo apt-get upgrade -y #update & upgrade
sudo apt-get install xinput-calibrator -y #install xinput calibrator for touchscreen test and calibration

#install required libraries for qt to use screen without error.
sudo apt-get install ffmpeg libsm6 libxext6 libxcb-icccm4 libxcb-image0 libxcb-util1 libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 -y

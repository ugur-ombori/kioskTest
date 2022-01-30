#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip curl
sudo -H pip3 install --upgrade pip
pip3 install -r requirements.txt
sudo apt-get update && sudo apt-get upgrade -y
curl -sLS https://apt.adafruit.com/add | sudo bash
sudo apt-get install xinput_calibrator -y

sudo apt-get install ffmpeg libsm6 libxext6 libxcb-icccm4 libxcb-image0 libxcb-util1 libxcb-keysyms1 libxcb-render-util0 libxcb-xinerama0 libxcb-xkb1 libxkbcommon-x11-0 -y

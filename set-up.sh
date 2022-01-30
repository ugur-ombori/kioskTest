#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip
sudo -H pip3 install --upgrade pip
pip3 install -r requirements2.txt
sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install xinput_calibrator
#!/bin/bash

source $HOME/kioskTest/venv/bin/activate

sudo docker build -t kiosk-test:0.1 .
xhost +local:docker
sudo docker run -it --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" kiosk-test:0.1


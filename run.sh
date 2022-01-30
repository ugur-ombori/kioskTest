#!/bin/bash

HOME=/home/kioksk
source $HOME/kioskTest/venv/bin/activate

#sudo docker build -t kiosk-test:0.1 .
#xhost +local:docker
#sudo docker run --net=host --env="DISPLAY" --volume="$HOME/.Xauthority:/root/.Xauthority:rw" kiosk-test:0.1

python3 /home/kioksk/kioskTest/app.py

#sudo docker run --user=$(id -u $USER):$(id -g $USER) --net=host --env="DISPLAY" --volume="/etc/group:/etc/group:ro" --volume="/etc/passwd:/etc/passwd:ro" --volume="/etc/shadow:/etc/shadow:ro" --volume="/etc/sudoers.d:/etc/sudoers.d:ro" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" kiosk-test:0.1
    

#!/bin/bash

xset -dpms
xset s off
xset s noblank

echo $0
echo $1
echo $2
SCREEN_ROTATION=$1

if [ -z "$SCREEN_ROTATION" ]
then
  echo "SCREEN_ROTATION not set"
else
  xrandr -o $SCREEN_ROTATION

  TOUCH_DEVICE=`xinput list | grep -i "touch" | grep -i "pointer" | sed s/id=.*// | sed s/[^\ 0-9a-z_A-Z\.]//g | head -n 1 | xargs`;
  TOUCH_DEVICE='VirtualBox mouse integration'
  echo TOUCH_DEVICE
  echo $TOUCH_DEVICE
  echo $SCREEN_ROTATION

  if [ -n "$TOUCH_DEVICE" ]
  then

    if [ "$SCREEN_ROTATION" == "left" ]
    then
      xinput set-prop "$TOUCH_DEVICE" "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1
    elif [ "$SCREEN_ROTATION" == "right" ]
    then
      xinput set-prop "$TOUCH_DEVICE" "Coordinate Transformation Matrix" 0 1 0 -1 0 1 0 0 1
    elif [ "$SCREEN_ROTATION" == "inverted" ]
    then
      xinput set-prop "$TOUCH_DEVICE" "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1
    elif [ "$SCREEN_ROTATION" == "normal" ]
    then
      xinput set-prop "$TOUCH_DEVICE" "Coordinate Transformation Matrix" 0 0 0 0 0 0 0 0 0
    fi
  fi
fi

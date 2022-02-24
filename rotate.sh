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

  SEARCH="Touch"
  if [ "$SEARCH" = "" ]; then 
      exit 1
  fi
  echo $SEARCH
  ids=$(xinput --list | awk -v search="$SEARCH" \
      '$0 ~ search {match($0, /id=[0-9]+/);\
                    if (RSTART) \
                      print substr($0, RSTART+3, RLENGTH-3)\
                  }'\
      )
      

  echo -ids-
  echo $ids
  echo $SCREEN_ROTATION

  cnt=0
  for i in $ids
  do
    if (( $cnt<2 )) 
    then
      cnt=$((cnt+1))
      if [ "$SCREEN_ROTATION" == "left" ]
      then                                                                 
        xinput set-prop $i "Coordinate Transformation Matrix" 0 -1 1 1 0 0 0 0 1
        echo $i
      elif [ "$SCREEN_ROTATION" == "right" ]
      then                                                                
        xinput set-prop $i "Coordinate Transformation Matrix" 0 1 0 -1 0 1 0 0 1
        echo $i
      elif [ "$SCREEN_ROTATION" == "inverted" ]                           
      then                                                                 
        xinput set-prop $i "Coordinate Transformation Matrix" -1 0 1 0 -1 1 0 0 1
        echo $i
      elif [ "$SCREEN_ROTATION" == "normal" ]
      then                                                                 
        xinput set-prop $i "Coordinate Transformation Matrix" 0 0 0 0 0 0 0 0 0
        echo $i
      fi
    fi
  done
fi

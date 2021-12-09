#!/bin/bash
for ((i = 1 ; i < 26 ; i++)); do
  x="`printf \"%02d\" $i`"
  if [[ ! (-e day$x)]]; then
    mkdir day$x
    touch day$x/input.txt
    touch day$x/puzzle.txt
  fi
done
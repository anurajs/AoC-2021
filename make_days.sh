for ((i = 1 ; i < 26 ; i++)); do
  x="`printf \"%02d\" $i`"
  if [[ ! (-e day$x)]]; then
    mkdir day$i
    touch day$i/solution.py
  fi
done
for ((i = 1 ; i < 26 ; i++)); do
  if [[ ! (-e day$i)]]; then
    mkdir day$i
    touch day$i/solution.py
  fi
done
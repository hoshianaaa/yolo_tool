ls | awk '{ printf "mv %s test%03d.png\n", $0, NR+150 }'
ls | awk '{ printf "mv %s test%03d.png\n", $0, NR+150 }' | sh

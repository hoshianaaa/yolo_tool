ls | awk '{ printf "mv %s image%04d.jpg\n", $0, NR+150 }'
ls | awk '{ printf "mv %s image%04d.jpg\n", $0, NR+150 }' | sh

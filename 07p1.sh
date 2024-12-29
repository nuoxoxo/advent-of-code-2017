#!bin/bash
bulk=''
while read -r line; do
    bulk+="$line "
done
echo -n "part 1: "
echo "$bulk" | grep -oE '[a-z]+' | sort | uniq -u

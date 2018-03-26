#!/bin/bash

counter=1
f="img"
for d in */ ; do
	filename="$f$counter"	
	mv -T "$d" "$filename"
	((counter++))
done

echo finished

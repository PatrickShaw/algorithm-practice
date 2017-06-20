#!/bin/bash
a_score=0
b_score=0
read a_numbers
i=0;
for number in $a_numbers; do
    a_array[$i]=$number
    (( i++ ))
done
read b_numbers
i=0;
for number in $b_numbers; do
    b_array[$i]=$number
    (( i++ ))
done
for i in {0..2}; do
	if [ ${a_array[$i]} -lt ${b_array[$i]} ]; then
		(( a_score++ ))
	elif [ ${a_array[$i]} -gt ${b_array[$i]} ]; then
		(( b_score++ ))
	fi
done
echo "$a_score $b_score"

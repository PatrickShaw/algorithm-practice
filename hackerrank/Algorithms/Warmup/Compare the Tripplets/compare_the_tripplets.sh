#!/bin/bash
a_score=0
b_score=0
read a_numbers
i=0;
for number in $a_numbers; do
    a_tupple[$i]=$number
    (( i++ ))
done
read b_numbers
i=0;
for number in $b_numbers; do
    b_tupple[$i]=$number
    (( i++ ))
done
for i in {0..2}; do
	if [ ${a_tupple[$i]} -lt ${b_tupple[$i]} ]; then
		(( a_score++ ))
	elif [ ${a_tupple[$i]} -gt ${b_tupple[$i]} ]; then
		(( b_score++ ))
	fi
done
echo "$a_score $b_score"

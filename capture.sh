#!/bin/bash
DST=$1
> sender-ss.txt
while [ 1 ]; do 
	ss -ein dst $DST | ts '%.s' | tee -a sender-ss.txt 
done


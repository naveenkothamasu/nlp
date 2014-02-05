#!/bin/sh
for i in $(seq -f "%05g" 1250 1500) 
do
	echo 'moving /mnt/shared-windows/544HW1/SENTIMENT_training/NEG.'$i'.txt' '/mnt/shared-windows/544HW1/SENTIMENT_3'
	mv '/mnt/shared-windows/544HW1/SENTIMENT_training/NEG.'$i'.txt' '/mnt/shared-windows/544HW1/SENTIMENT_3'
	echo 'moving /mnt/shared-windows/544HW1/SENTIMENT_training/POS.'$i'.txt' '/mnt/shared-windows/544HW1/SENTIMENT_3'
	mv '/mnt/shared-windows/544HW1/SENTIMENT_training/POS.'$i'.txt' '/mnt/shared-windows/544HW1/SENTIMENT_3'
done

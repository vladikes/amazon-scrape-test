#!/bin/bash

IFS=,
while read column1 column2 column3 column4 column5 column6
      do
        echo "INSERT INTO cost (titles, dates, authors, prices, stars, reviews) VALUES ('$column1', '$column2', '$column3', '$column4', '$column5', '$column6');"

done < results.csv | mysql -u myusername -p mypassword mydata;

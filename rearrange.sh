sed -r 's/^/,/; s/\\"/\x01/g; s/,"([^"]*)"/,\x02\1\x03/g; s/,"/,\x02/; :MC; s/\x02([^\x03]*),([^\x03]*)/\x02\1\x04\2/g; tMC; s/^,// ' items_2.csv |
  awk 'BEGIN{FS=OFS=","} { print $1,$2,$4,$5,$3}' |
    sed -r 's/\x01/\\"/g; s/(\x02|\x03)/"/g; s/\x04/,/g'
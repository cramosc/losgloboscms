#! /usr/bin/env bash

OUT_FILE="out.tar.gz"

cd out
tar -cvzf "../$OUT_FILE" *
cd ..

curl -s -u "$FTP_CREDENTIALS" -T "$OUT_FILE" "$FTP_SERVER/$OUT_FILE"
curl -s -u "$FTP_CREDENTIALS" -T scripts/extractor.php "$FTP_SERVER/extractor.php"

curl -s "http://losglobos.de/extractor.php"

curl -s -u "$FTP_CREDENTIALS" "$FTP_SERVER" -Q 'DELE out.tar.gz'
curl -s -u "$FTP_CREDENTIALS" "$FTP_SERVER" -Q 'DELE out.tar'
curl -s -u "$FTP_CREDENTIALS" "$FTP_SERVER" -Q 'DELE extractor.php'

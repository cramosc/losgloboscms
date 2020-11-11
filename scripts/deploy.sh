#! /usr/bin/env bash

OUT_FILE="out.tar.gz"

echo "creating tar file..."
cd out
tar -czf "../$OUT_FILE" *
cd ..

echo "uploading tar file..."
curl -s -u "$FTP_CREDENTIALS" -T "$OUT_FILE" "$FTP_SERVER/$OUT_FILE"
echo "uploading php script..."
curl -s -u "$FTP_CREDENTIALS" -T scripts/extractor.php "$FTP_SERVER/extractor.php"

echo "executing php script..."
curl "http://losglobos.de/extractor.php"
echo ""

echo "clean up..."
curl -s -u "$FTP_CREDENTIALS" "$FTP_SERVER" -Q 'DELE out.tar.gz' > /dev/null
curl -s -u "$FTP_CREDENTIALS" "$FTP_SERVER" -Q 'DELE out.tar' > /dev/null
curl -s -u "$FTP_CREDENTIALS" "$FTP_SERVER" -Q 'DELE extractor.php' > /dev/null

echo "Deployment done!"

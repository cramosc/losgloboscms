#! /usr/bin/env bash

cd out
find * -type f -exec curl -u "$FTP_CREDENTIALS" --ftp-create-dirs -T {} "$FTP_SERVER"/test/{} \;
cd -

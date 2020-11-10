#! /usr/bin/env bash

cd out
find * -type f -exec echo Deploying {} ... \; -exec curl -s -u "$FTP_CREDENTIALS" --ftp-create-dirs -T {} "$FTP_SERVER"/test/{} \; -exec echo Done \;
cd -

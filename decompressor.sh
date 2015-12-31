#!/bin/sh

mkdir tmp
mv *.zip tmp/
unzip 'tmp/*.zip' -d .
rm -rf tmp



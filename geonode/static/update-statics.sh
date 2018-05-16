#!/bin/bash

set -e 
set +x

wget https://nodejs.org/dist/v6.11.2/node-v6.11.2-linux-x64.tar.xz
tar Jxvf node-v6.11.2-linux-x64.tar.xz
PATH=$PATH:./node-v6.11.2-linux-x64/bin/
npm install npm@latest
npm install -g bower
npm install -g grunt
npm install
bower --allow-root install
grunt production
rm -fr node-v6.11.2-linux-x64*

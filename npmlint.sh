#!/bin/bash

set -e

npm install

npm run lint

EXIT_CODE=$?

rm -rf node_modules

exit $EXIT_CODE

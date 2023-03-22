#!/bin/bash

set -e

npm install eslint@^8.28.0 \
                    eslint-config-prettier@^8.6.0 \
                    @angular-eslint/builder@14.4.0 \
                    @angular-eslint/eslint-plugin@14.4.0 \
                    @angular-eslint/eslint-plugin-template@14.4.0 \
                    @angular-eslint/schematics@14.4.0 \
                    @angular-eslint/template-parser@14.4.0 \
                    @typescript-eslint/eslint-plugin@5.43.0 \
                    @typescript-eslint/parser@5.43.0

npm run lint

EXIT_CODE=$?

git stash
rm -rf node_modules

exit $EXIT_CODE

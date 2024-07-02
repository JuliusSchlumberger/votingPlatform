#!/bin/bash

# Parse the DATABASE_URL to extract the components
eval $(echo $DATABASE_URL | sed -e 's,postgres://\([^:]*\):\([^@]*\)@\(.*\):\([0-9]*\)/\(.*\),export DATABASE_URL_USER=\1 DATABASE_URL_PASSWORD=\2 DATABASE_URL_HOST=\3 DATABASE_URL_PORT=\4 DATABASE_URL_DBNAME=\5,')

# Export the parsed components
export DATABASE_URL_USER
export DATABASE_URL_PASSWORD
export DATABASE_URL_HOST
export DATABASE_URL_PORT
export DATABASE_URL_DBNAME

#!/bin/bash
set -o errexit
set -o pipefail
set -o nounset
python /src/backen_api/manage.py migrate
python /src/backen_api/manage.py runserver 0.0.0.0:8000

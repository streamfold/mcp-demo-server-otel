#!/bin/bash

CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"

set -e

cd $CWD/.. && source .venv/bin/activate

# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# reload environ
source $HOME/.local/bin/env

PORT=${PORT:-10000}

exec uv run uvicorn --host 0.0.0.0 --port ${PORT} main:app

#!/bin/bash

CWD="$(cd -P -- "$(dirname -- "$0")" && pwd -P)"

set -e

# install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# reload environ
source $HOME/.local/bin/env

uv sync

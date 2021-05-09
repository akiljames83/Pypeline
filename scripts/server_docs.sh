#!/bin/sh

#  Run an http server for the docs
python -m http.server -d docs/Pypeline

# Usage ./scripts/server_docs.sh
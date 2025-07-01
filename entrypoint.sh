#!/bin/bash
ruff .
pytest
exec "$@"

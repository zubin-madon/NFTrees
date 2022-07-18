#!/bin/sh

gunicorn --worker-tmp-dir /dev/shm --config gunicorn.config.py nft_server:app
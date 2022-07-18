#!/bin/sh

gunicorn --config gunicorn.config.py nft_server:app
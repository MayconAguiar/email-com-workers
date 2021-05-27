#!/bin/sh
pip uninstall psycopg2 -y
pip install bottle==0.12.13 psycopg2==2.7.7
python -u sender.py
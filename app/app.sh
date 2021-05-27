#!/bin/sh
pip uninstall psycopg2 -y
# além de inserir no banco de dados o app vai mandar uma mensagem pra a fila, por isso o redis
pip install bottle==0.12.13 psycopg2==2.7.7 redis==2.10.5
python -u sender.py
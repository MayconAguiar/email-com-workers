FROM python:3.6
USER root
LABEL maintainer 'Maycon Aguiar'

# executar os prints, saida do sistema, não usar o buffer 
# executar isso de forma síncrona
# para poder ver as mensagens exibidas sem o buffer
ENV PYTHONUNBUFFERED 1
# faz a instalação do redis
RUN pip install redis==2.10.5

ENTRYPOINT ["/usr/local/bin/python"]
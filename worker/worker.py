import redis
import json
from time import sleep
from random import randint

# faz o teste para ver se esse é o arquivo principal que está sendo executado
if __name__ == '__main__':
    # pega a referência do redis apontando para máquina 
    # e para a porta que está sendo executado
    r = redis.Redis(host='queue', port=6379, db=0)

    # laço para consumir as mensagens
    while True:
        # pegar dentro da fila sender 
        # a mensagem faz o loads do json e atribui a mensagem
        mensagem = json.loads(r.blpop('sender')[1])
        # simulando o envio do e-mail
        print('Mandando a mensagem', mensagem['assunto'])
        sleep(randint(15, 45))
        print('Mensagem', mensagem['assunto'], 'enviada')
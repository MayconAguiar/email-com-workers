import psycopg2
import redis
import json
from bottle import Bottle, request

#Classe Sender que herda de Bottle
class Sender(Bottle):
    # faz algumas inicializações
    def __init__(self):
        # chama o init do super
        super().__init__()
        # na herança eu tenho a disposição o método route
        self.route('/', method='POST', callback=self.send)
        self.fila = redis.StrictRedis(host='queue', port=6379, db=0)
        
        DSN = 'dbname=email_sender user=postgres password=email-com-workers host=db'
        self.conn = psycopg2.connect(DSN)

    def register_message(self, assunto, mensagem):
        SQL = 'INSERT INTO emails (assunto, mensagem) VALUES (%s, %s)'
        
        cur = self.conn.cursor()
        cur.execute(SQL, (assunto, mensagem))
        self.conn.commit()
        cur.close()
        
        msg = {'assunto': assunto, 'mensagem': mensagem}
        # passa a mensagem para a fila no formato json
        self.fila.rpush('sender', json.dumps(msg))
        print ('Mensagem registrada !')

    def send(self):
        assunto = request.forms.get('assunto')
        mensagem = request.forms.get('mensagem')
        self.register_message(assunto, mensagem)
        return 'Mensagem enfileirada! Assunto: {} Mensagem: {}'.format(
            assunto, mensagem
        )

#verifica se é o arquivo principal
if __name__ == '__main__':
    sender = Sender()
    sender.run(host='0.0.0.0', port=8080, debug=True)
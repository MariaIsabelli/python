import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket criado')

host = 'localhost'
porta = 5432

s.bind((host , porta))
mensagem = 'Servidor: Hello'

while 1:
  dados, end = s.recvfrom(4096)
  
if dados:
  print('Servidor enviando....')
  s.sendto((ados + mensagem.ecode()), end)
  

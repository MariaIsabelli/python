import socket

s = socket.socket(socket.AF_INET, socket.SOCCK_DGRAM)

print('Cliente socket')

host = 'localhost'
porta = 5433
mensagem = 'Fsocity.dat'

try:
  print('Cliente: '+ mensagem)
  s.sendto(mensagem.encode(), (host, 5432))
  
  dados, servidor = s.recvfrom(4096)
  dados = dados.decode()
  
  print("Cliente: " + dados)
  
finally:
  print('Cliente: Fecahndo a Conexão')
  s.close()
  

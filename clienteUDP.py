import socket  ##UDP principio da Disponibilidade
## Criado o objeto de conexao s socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket criado com Sucesso!!!')
## Porta do cliente localhost de numero 5433
host = 'localhost'
porta = 5433
mensagem = 'Ola servidor tudo firmeza?'
## Tentar enviar uma mensagem e fechar no final
try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('Cliente: '+ dados)
finally:
    print('Cliente: Fechando a Conexão')
    s.close()
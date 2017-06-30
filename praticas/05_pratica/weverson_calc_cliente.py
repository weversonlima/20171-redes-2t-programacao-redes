import socket

HOST = socket.gethostbyname ('localhost')
PORT = 3000

socket_tcp_cliente = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
socket_tcp_cliente.connect ((HOST, PORT))

while True: #Cliente permanece na calculadora enviando operações aritméticas
	envio1 = input ("Entre com a operacao (<QUIT> para sair): ")
	msgenvio1 = envio1.encode ('utf-8') #Codificação da mensagem a ser enviada
	socket_tcp_cliente.send (msgenvio1) #Envio da operação aritmética pelo cliente

	if envio1.upper() == "<QUIT>": #Cliente envia mensagem pedindo para encerrar sua conexão
		retorno_servidor = socket_tcp_cliente.recv (1024)
		msg_retorno_servidor = retorno_servidor.decode ('utf-8') #Aviso de fim de conexão devolvido ao cliente
		print (msg_retorno_servidor)
		break #Quando o cliente pede para sair, sua conexão é encerrada. Em outros casos, permanece na calculadora.
		
	envio2 = socket_tcp_cliente.recv (1024) #Resultado da operação (retorno do servidor)
	msgenvio2 = envio2.decode ('utf-8') #Decodificação da mensagem recebida
	print (msgenvio2) #Impressão do resultado da operação no cliente

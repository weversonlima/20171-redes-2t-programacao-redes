import socket, re
from math import sqrt #Importando o método aritmético sqrt (raiz quadrada)

HOST = socket.gethostbyname ('localhost')
PORT = 3000

tcp_server_socket = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
tcp_server_socket.bind ((HOST,PORT))
tcp_server_socket.listen (2)

numeroValido = re.compile(r"^[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?$") #Essa expressão identifica um número e somente um número inclusive negativo

def sendMsg(client, mensagem): #Funcao para reduzir o código para enviar mensagens ao cliente
	send = mensagem 
	msgsend = send.encode ('utf-8')
	client.send (msgsend) #Servidor avisa ao cliente que houve mensagem inválida e, por isso, sua conexão será encerrada.

while True:
	client, addr = tcp_server_socket.accept ()
	while True: #Mantém o servidor em escuta, isto é, permitindo várias conexões sem encerrar
		data0 = client.recv (1024)
		msgrecebida = data0.decode ('utf-8')
		print ("Mensagem recebida do cliente:", repr (msgrecebida)) 
		# ↑ Servidor imprime (informa) sempre o conteúdo enviado do cliente ↑
		splitmsg = msgrecebida.split (' ')
		comando = splitmsg[0]
		if (comando == "raiz_quadrada"):	
			if (len(splitmsg) != 2):
				sendMsg(client, "Mensagem invalida. Reconecte e entre com uma operacao valida.") 
				continue
			n1 = splitmsg[1]
			if (numeroValido.match(n1) is None):
				sendMsg(client, "Número Inválido. Reconecte e entre com uma operacao valida.")
				continue
			if (float(n1) < 0):
				sendMsg(client, "Número Inválido (negativo). Reconecte e entre com uma operacao valida.")
				continue
			raiz = sqrt (float (n1)) #Calcula-se a raiz
			sendMsg(client, "Resultado da raiz quadrada: " + str (raiz))
		elif (comando == "soma"):
			if (len(splitmsg) != 3):
				sendMsg(client, "Mensagem invalida. Reconecte e entre com uma operacao valida.") 
				continue
			n1 = splitmsg[1]
			n2 = splitmsg[2]
			if (numeroValido.match(n1) is None or numeroValido.match(n2) is None ):
				sendMsg(client, "Número Inválido. Reconecte e entre com uma operacao valida.")
				continue
			soma = float (n1) + float (n2) #Somando os 2 números
			sendMsg(client,"Resultado da soma: " + str (soma))
		elif (comando.upper() == "<QUIT>"):
			sendMsg(client, "Conforme desejado, sua conexao foi encerrada!")
			print ("Aguardando nova conexao...\n")
			break                 
		else: 
			sendMsg(client, "Mensagem invalida. Reconecte e entre com uma operacao valida.")
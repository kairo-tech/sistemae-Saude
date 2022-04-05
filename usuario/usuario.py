import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('localhost', 7777))
print('Bem-vindo(a) ao agendamento do e-Saúde!!\n')

namefile = str(input('Digite o nome dos documentos para anexar:'))

client.send(namefile.encode())

with open(namefile, 'wb') as file:
    while 1:
        data = client.recv(1000000)
        if not data:
            break
        file.write(data)

print(f'{namefile} recebido!\n')
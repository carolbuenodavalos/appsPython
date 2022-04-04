# Escreva um programa que receba (entrada de dados através do teclado) o nome do cliente, o dia de vencimento, o mês de vencimento e o valor da fatura  e imprima (saída de dados) a mensagem com os dados recebidos
nomedoCliente = input('Digite o nome do Cliente:')
diaVencimento = input('digite o dia do vencimento: ')
mesVencimento = input('digite o mes do vencimento: ')
valorFatura = input('digite o valor da fatura:')

print('Olá,', nomedoCliente , 'a sua fatura com vencimento em',
diaVencimento, 'de', mesVencimento, 'com o valor de R$', valorFatura, '...')

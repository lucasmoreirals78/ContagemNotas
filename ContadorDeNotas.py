

numero = int(input('Informe o valor do saque entre 10 e 600: '))


notaCem = numero%100 != numero
qntCem = int(numero/100)
numero = numero - qntCem * 100


notaCinquenta = numero%50 != numero
qntCinquenta = int(numero/50)
numero = numero - qntCinquenta * 50



notaCinco = numero%5 != numero
qntCinco = int(numero/5)
numero = numero - qntCinco * 5


notaDez = numero%10 != numero
qntDez = int(numero/10)
numero = numero - qntDez * 10

notaVinte = numero%20 != numero
qntVinte = int(numero/20)
numero = numero - qntVinte * 20

notaUm = numero%1 != numero


if(notaCem):
  if(qntCem ==1): print(qntCem, ' cem, ')
  else: print(qntCem, ' em cem, ')

if(notaCinquenta):
  if(qntCinquenta ==1): print(qntCinquenta, ' cinquenta, ')
  else: print(qntCinquenta, ' em cinquenta, ')

if(notaVinte) :
  if(qntDez==1): print(qntDez, ' vinte ')
  else: print(qntVinte, ' em vinte ')

if(notaDez)  :
  if(qntDez==1): print(qntDez, ' dez ')
  else: print(qntDez, ' em dez ')

if(notaCinco):
  if(qntCinco ==1): print(qntCinco, ' cinco, ')
  else: print(qntCinco, ' em cinco, ')

if(notaUm):
  if(numero==1): print('e ', numero, 'um')
  else: print('e ', numero, ' em um')




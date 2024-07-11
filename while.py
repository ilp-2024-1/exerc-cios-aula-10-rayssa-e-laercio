#--- QUESTÃO 1 - COMPLETA ---

#Escreva um programa que exiba os valores dos números de 1 até 100. Ao término o 
#programa deverá exibir uma mensagem de encerramento informando que o programa 
#terminou.

#valor = 0
#while valor < 100:
#      valor +=1
#      print(valor)
#print("Programa Encerrado")


# --- QUESTÃO 2 - INCOMPLETA ---

#Escreva um programa que solicita ao usuário valores numéricos e realiza a soma
#desses valores. Quando o usuário digitar o valor 0 o programa deverá exibir o valor do
#somatório e encerrar o programa com uma mensagem de término do programa. O
#usuário deverá ser informado no início do programa o que o programa faz e qual a
#condição para encerramento do programa.


#p_valor = int(input("digite seu valor: "))
#s_valor = int(input("digite seu valor:; "))

#while (p_valor != 0):
#       print(p_valor)
#while (s_valor != 0):
#      print(s_valor)


#--- QUESTÃO 3 - COMPLETA ---

#Crie um programa que solicita ao usuário uma senha e em seguida compare esse valor
#com uma senha armazenada em uma variável. Enquanto o usuário não acertar o valor
#da senha o programa deverá solicitar a senha ao usuário. Quando o usuário acerta a
#senha, o programa deverá encerrar exibindo uma mensagem encerramento e informar
#que o usuário acertou a senha.


#senha = "Rayssa"
#usuario = str(input("digite sua senha: "))

#while(senha != usuario):
#    print("senha incorreta")
#    usuario = input("digite uma nova senha: ")


#print("seja bem vindo")
#print("Fim da questão")



#--- QUESTÃO 4 - INCOMPLETA ---

#Escreva um programa que gere um número aleatório entre 1 e 100 e peça ao usuário
#para adivinhar qual é o número. O programa deve continuar pedindo palpites até que
#o usuário acerte o número. Ao final, o programa deve informar quantos palpites foram
#necessários e informar que o programa encerrou.


import random

palpite= int(input("digite sua escolha : "))
n_aleatorio = random.randint(1,100)

while(n_aleatorio != palpite):
        print(n_aleatorio)
if (n_aleatorio == palpite):
      palpite +=1
print(palpite)

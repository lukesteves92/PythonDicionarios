from Dicionarios.FuncoesManage import *
usuarios = {}

opcao = perguntar()

while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login:").upper()
        nome = input("Digite o nome:").upper()
        data = input("Digite a última data de acesso:").upper()
        estacao = input("Qual a última estação acessada").upper()
        usuarios[chave] = [nome, data, estacao]
    opcao = perguntar()
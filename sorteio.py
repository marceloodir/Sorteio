#!/usr/bin/python3
import random
import pickle
import operator
import datetime
__author__ = 'marcelo'
arquivo = 'dados.dat'

class Participante:

    def __init__(self,nome='',telefone='',email=''):
        self.setNome(nome)
        self.setTelefone(telefone)
        self.setEmail(email)
        self.dataCadastro = datetime.datetime.now().strftime("%d-%m-%Y")

    def setNome(self,nome):
        self.nome =  " ".join(nome.split()).title()

    def setTelefone(self,telefone):
        self.telefone = telefone

    def setEmail(self,email):
        self.email = email.lower()

    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.telefone

    def getEmail(self):
        return self.email

    def getDataCadastro(self):
        return self.dataCadastro

    def eIgual(self,nome):
        nome = " ".join(nome.split()).title()
        if nome == self.nome:
            return True
        else:
            return False

def adicionar(participantes):
    nome = input("Entre com o nome completo do participante:")
    tel = input("Entre com o telefone do participante:")
    email = input("Entre com o email do participante:")

    participante = Participante(nome,tel,email)
    participantes.append(participante)

    with open(arquivo,'wb') as arq_file:
        pickle.dump(participantes,arq_file)

    print("Participante adicionado")

def listar(participantes):
    if len(participantes) == 0:
        print("Não há participantes cadastrados")
    else:
        participantes.sort(key=operator.attrgetter('nome'))
        for participante in participantes:
            print(participante.getNome()+' ---- '+participante.getDataCadastro())

def sortear(participantes):
    print("Sorteando...")
    if len(participantes) == 0:
        print("Não há participantes cadastrados para haver sorteio")
    else:
        sorteado = random.choice(participantes)
        print("A pessoa sorteada foi:",sorteado.getNome())
        print("Telefone:",sorteado.getTelefone())
        print("Email:",sorteado.getEmail())

def remover(participantes):
    nome = input("Entre com o nome completo do participante a ser removido:")
    for participante in participantes:
        if(participante.eIgual(nome)):
            participantes.remove(participante)
            with open(arquivo,'wb') as arq_file:
                pickle.dump(participantes,arq_file)
            print("Participante removido")
            return 0
    print("Nenhum participante encontrado com esse nome")

def limpar():
    verificacao = input("Digite SIM para confirmar a remoção de todos os participantes:")

    if verificacao != 'SIM':
        print("Remoção cancelada")
        return 0;

    listaVazia = list()

    with open(arquivo,'wb') as arq_file:
        pickle.dump(listaVazia,arq_file)

    print("Todos os participantes foram apagados")



while True:
    try:
        with open(arquivo,'rb') as arq_file:
            participantes = pickle.load(arq_file)

    except IOError as err:
        participantes = list()

    print("\n*******************************************************************")
    print("Quantidade de Participantes Cadastrados: ",len(participantes))
    print("\n1 - Adicionar Participante")
    print("2 - Listar Participantes")
    print("3 - Sortear Vencedor")
    print("4 - Limpar todos os participantes")
    print("5 - Remover um participante")
    print("6 - Sair")
    escolha = input("opção:")
    if int(escolha) == 1:
        adicionar(participantes)
    elif int(escolha) == 2:
        listar(participantes)
    elif int(escolha) == 3:
        sortear(participantes)
    elif int(escolha) == 4:
        limpar()
    elif int(escolha) == 5:
        remover(participantes)
    elif int(escolha) == 6:
        print("Saindo...")
        exit(0)
    else:
        print("Escolha inválida")
        exit(-1)




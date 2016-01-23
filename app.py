# -*- coding: UTF-8 -*-

def procurar(nomes):
	print 'Digite o nome a procurar:'
	nome = raw_input()
	if nome in nomes:
		print '%s encontrado na posição %s' % (nome, nomes.index(nome))
	else:
		print '%s não encontrado' % (nome)

def altera(nomes):
	print 'Digite o nome a ser alterado:'
	nome_antigo = raw_input()
	if nome_antigo in nomes:
		print 'Digite o novo nome:'
		nome_novo = raw_input()
		nomes[nomes.index(nome_antigo)] = nome_novo
	else:
		print 'nome nao encontrado.'

def remove(nomes):
	print 'Digite o nome para remover'
	nome = raw_input()
	nomes.remove(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def cadastrar(nomes):
	print 'Digite o nome:'
	nome = raw_input()
	nomes.append(nome)

def menu():
	nomes = []
	escolha = ''
	while(escolha != '0'):
		print 'Digite: 1 para cadastrar, 0 para terminar, 2 para listar, 3 para remover, 4 para alterar, 5 para procurar'
		escolha = raw_input()

		if(escolha == '1'):
			cadastrar(nomes)

		if(escolha == '2'):
			listar(nomes)

		if(escolha == '3'):
			remove(nomes)

		if(escolha == '4'):
			altera(nomes)
		if(escolha == '5'):
			procurar(nomes)
menu()
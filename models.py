# -*- conding: UTF-8 -*-

class Perfil(object):
	'Classe de usuario'

	def __init__(self, nome, telefone, empresa):
		self.nome = nome
		self.telefone = telefone
		self.empresa = empresa
		self.__curtidas = 0

	def imprimir(self):
		print 'Nome: %s, Telefone: %s, Empresa: %s' % (self.nome, self.telefone, self.empresa)

	def curtir(self):
		self.__curtidas += 1

	def obter_curtidas(self):
		return self.__curtidas

	@classmethod
	def gerar_perfis(nome_classe,nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		perfis = []
		for linha in arquivo:
			valores = linha.split(',')
			perfis.append(nome_classe(*valores))
		arquivo.close()
		return perfis


class PerfilVip(Perfil):
	'Classe com perfil de usuarios Vip'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(PerfilVip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(PerfilVip, self).obter_curtidas() * 10.0


class Conta(object):
	def __init__(self, titular, saldo):
		self.titular = titular
		self.saldo = saldo

	def calcular_imposto(self):
		self.saldo = self.saldo * 0.10
		return self.saldo

class ContaCorrente(Conta):
	def __init__(self, titular, saldo):
		super(ContaCorrente, self).__init__(titular, saldo)

	def calcular_imposto(self):
		return super(ContaCorrente,self).calcular_imposto() + 20


class Data(object):

	def __init__(self, dia, mes, ano):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def imprimir(self):
		print '%s/%s/%s' % (self.dia, self.mes, self.ano)

class Pessoa(object):
	def __init__(self, nome, peso, altura):
		self.nome = nome
		self.peso = peso
		self.altura = altura

	def imprime_imc(self):
		imc = self.peso/(self.altura ** 2)
		print 'Imc de %s: %s' % (self.nome, imc)

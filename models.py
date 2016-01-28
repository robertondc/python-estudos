# -*- conding: UTF-8 -*-

class Perfil(object):
	'Classe de usuario'

	def __init__(self, nome, telefone, empresa):
		if (len(nome) < 3):
			raise ArgumentoInvalidoError('Nome deve ter pelo menos 3 caracteres')
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
		arquivo = None
		try:
			arquivo = open(nome_arquivo, 'r')
			perfis = []
			for linha in arquivo:
				valores = linha.split(',')
				if (len(valores) is not 3):
					raise ValueError('A linha "%s" deve conter 3 valores' % (linha))
				perfis.append(nome_classe(*valores))
			arquivo.close()
			return perfis
		except (IOError, TypeError) as erro:
			print('FERROU!! Erro: %s') % (erro)
		finally:
			if (arquivo is not None):
				print('fechando arquivo')
				arquivo.close()

class PerfilVip(Perfil):
	'Classe com perfil de usuarios Vip'

	def __init__(self, nome, telefone, empresa, apelido=''):
		super(PerfilVip, self).__init__(nome, telefone, empresa)
		self.apelido = apelido

	def obter_creditos(self):
		return super(PerfilVip, self).obter_curtidas() * 10.0

class ArgumentoInvalidoError(Exception):
	def __init__(self, mensagem):
		self.mensagem = mensagem

	def __str__(self):
		return rpr(self.mensagem)


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

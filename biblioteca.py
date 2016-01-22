def gera_nome_convite(convite):
	posicao_final = len(convite)
	posicao_inical = posicao_final - 4
	parte1 = convite[0:4]
	parte2 = convite[posicao_inical: posicao_final]
	return parte1 + ' ' + parte2

def envia_convite(nome_formatado):
	return 'Enviando convite para %s' % (nome_formatado)

def processa_convite(convite):
	nome_formatado = gera_nome_convite(convite)
	return envia_convite(nome_formatado)

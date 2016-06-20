#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import re
import sys

azul = '\033[1;34m'
verde = '\033[1;32m'
fimCor = '\033[0m'
amarelo = '\033[1;33m'
vermelho = '\033[1;31m'

def lastInfo(codePacked):
	request = requests.get("http://developers.agenciaideias.com.br/correios/rastreamento/json/"+codePacked)
	cor = ''
	if request.status_code == 200:
		obJason = json.loads(request.content)
		index = len(obJason)-1
		print vermelho,"Tipo da Encomenda = ",fimCor,getPrefixCode(codePacked)
		print 'Data      = '+obJason[index]['data']
		print 'Local     = '+obJason[index]['local']
		if obJason[index]['acao'] == u'saiu para entrega ao destinatário'\
		or obJason[index]['acao'] == 'entrega efetuada':
			cor = verde
		elif obJason[index]['acao'] == 'postado':
			cor = azul
		elif obJason[index]['acao'] == 'encaminhado':
			cor = amarelo
		print 'Acao      = '+cor+obJason[index]['acao']+fimCor
		print 'Detalhes  = '+obJason[index]['detalhes']
	else:
		print 'Sem conexão com a internet'

def menu():
	if len(sys.argv)== 1:
		print vermelho,"Nome",fimCor,"\n\trastreiaEncomendas.py\n\n",verde,"Sinopse",fimCor,"\n\t rastreiaEncomendas.py [opção][parametro]\n\n",amarelo,"Descrição",fimCor,"\n\tLocaliza sua encomenda e fornece informações do percurso\n\n",azul,"Opções",fimCor,"\n\t-r,rastrear (-r código fornecido pelos correios)\n\t\tex: -r PJ123456789BR\n\n\t-v,validar código (-v código fornecido pelos correios\n\t\tVerifica se o código passado é um código válido de um objeto)\n\n\t-u,último status ( -u código fornecido pelos correios)\n\t\tRetorna apenas a última informação do objeto\n\n\t-i, informação sobre o tipo do objeto(-i primeiras duas letras )\n\t\tApresenta qual é o tipo do objeto\n\n",verde,"Informações do Código de rastreamento",fimCor,"\n\t O código de rastreamento é formado por  PJ123456789BR onde :\n\t 2 Letras iniciais é um sigla que representa o tipo da encomenda\n\t Os 9 dígitos são do código do Objeto\n\t BR relativo ao Brasil (Sério?!)\n\n",verde,"Autor",fimCor,"\n\tErik Ferreira - ekdespe\n\temail : ekdespe@gmail.com\n\tGitHub:fsafasdfa\n\tCarteira Bitcoin:fadsfdafdafda\n\tCarteira Litecoin\n\tLinux User #123456\n\n",amarelo,"Licensa",fimCor,"\n\tGPL"

	else:
		if sys.argv[1] =='-r':
			if toValidCodePacked(sys.argv[2]):
				showPackedInfo(sys.argv[2])
			else:
				print 'O código do objeto não é válido '	
		
		elif sys.argv[1] =='-u': 
			if toValidCodePacked(sys.argv[2]):
				lastInfo(sys.argv[2])
			else:
				print 'O código do objeto não é válido '	
		
		elif sys.argv[1] =='-v':
			if toValidCodePacked(sys.argv[2]):
				print 'O código informado é válido'
			else:
				print 'O código do objeto não é válido '	
		
		elif sys.argv[1] == '-i':
			if re.search(r'^([A-Z]{2})',sys.argv[2]):
				try:
					print getPrefixCode(sys.argv[2])
				except:
					print 'Sigla inexistente!'
			else:
				print 'Digite apenas duas letras maiúsculas'
		
		else :
			print 'Função inválida chame o programa sem argumentos para ver as opções'

#show the all informations about the package
def showPackedInfo(codePacked):
	request = requests.get("http://developers.agenciaideias.com.br/correios/rastreamento/json/"+codePacked)
	
	if request.status_code == 200:
		obJason = json.loads(request.content)
		print vermelho,"Tipo da Encomenda = ",fimCor,getPrefixCode(codePacked)
		for index in obJason:
		
			print 'Data      = '+index['data']
			print 'Local     = '+index['local']
			if index['acao'] == u'saiu para entrega ao destinatário':
				cor = verde
			elif index['acao'] == 'postado':
				cor = azul
			elif index['acao'] == 'encaminhado':
				cor = amarelo
			#else:
			#	cor ='\033[0;0m' 
			print 'Acao      = '+cor+index['acao']+fimCor
			print 'Detalhes  = '+index['detalhes']
			print amarelo+'-----------------------------------------------------------------'+fimCor
	else:
		print "Sem Conexao com a Internet"

#Show the full name of the two chart of CodePackage
def getPrefixCode(codePrefix):
	code = codePrefix[:2]
	listInfo = {"AL":"Agentes de leitura",
	"AR":"Avisos de recebimento",
	"AS":"PAC - Ação Social",
	"CA":"Encomenda Internacional - Colis",
	"CB":"Encomenda Internacional - Colis",
	"CC":"Encomenda Internacional - Colis",
	"CD":"Encomenda Internacional - Colis",
	"CE":"Encomenda Internacional - Colis",
	"CF":"Encomenda Internacional - Colis",
	"CG":"Encomenda Internacional - Colis",
	"CH":"Encomenda Internacional - Colis",
	"CI":"Encomenda Internacional - Colis",
	"CJ":"Encomenda Internacional - Colis",
	"CK":"Encomenda Internacional - Colis",
	"CL":"Encomenda Internacional - Colis",
	"CM":"Encomenda Internacional - Colis",
	"CN":"Encomenda Internacional - Colis",
	"CO":"Encomenda Internacional - Colis",
	"CP":"Encomenda Internacional - Colis",
	"CQ":"Encomenda Internacional - Colis",
	"CR":"Carta registrada sem Valor Declarado",
	"CS":"Encomenda Internacional - Colis",
	"CT":"Encomenda Internacional - Colis",
	"CU":"Encomenda internacional - Colis",
	"CV":"Encomenda Internacional - Colis",
	"CW":"Encomenda Internacional - Colis",
	"CX":"Encomenda internacional - Colis ou Selo Lacre para Caixetas",
	"CY":"Encomenda Internacional - Colis",
	"CZ":"Encomenda Internacional - Colis",
	"DA":"SEDEX ou Remessa Expressa com AR Digital",
	"DB":"SEDEX ou Remessa Expressa com AR Digital (Bradesco)",
	"DC":"Remessa Expressa CRLV/CRV/CNH e Notificações",
	"DD":"Devolução de documentos",
	"DE":"Remessa Expressa Talão/Cartão com AR",
	"DF":"e-SEDEX",
	"DG":"SEDEX",
	"DI":"SEDEX ou Remessa Expressa com AR Digital (Itaú)",
	"DJ":"SEDEX",
	"DK":"PAC Extra Grande",
	"DL":"SEDEX",
	"DM":"e-SEDEX",
	"DN":"SEDEX",
	"DO":"SEDEX ou Remessa Expressa com AR Digital (Itaú)",
	"DP":"SEDEX Pagamento na Entrega",
	"DQ":"SEDEX ou Remessa Expressa com AR Digital (Santander)",
	"DR":"Remessa Expressa com AR Digital (Santander)",
	"DS":"SEDEX ou Remessa Expressa com AR Digital (Santander)",
	"DT":"Remessa econômica com AR Digital (DETRAN)",
	"DU":"e-SEDEX",
	"DV":"SEDEX c/ AR digital",
	"DX":"SEDEX 10",
	"EA":"Encomenda Internacional - EMS",
	"EB":"Encomenda Internacional - EMS",
	"EC":"PAC",
	"ED":"Packet Express",
	"EE":"Encomenda Internacional - EMS ",
	"EF":"Encomenda Internacional - EMS ",
	"EG":"Encomenda Internacional - EMS ",
	"EH":"Encomenda Internacional - EMS ou Encomenda com AR Digital",
	"EI":"Encomenda Internacional - EMS ",
	"EJ":"Encomenda Internacional - EMS ",
	"EK":"Encomenda Internacional - EMS ",
	"EL":"Encomenda Internacional - EMS ",
	"EM":"- final BR",
	"En":"omenda Internacional - SEDEX Mundi",
	"EM":"- final diferente de BR",
	"En":"omenda Internacional - EMS Importação",
	"EN":"Encomenda Internacional - EMS ",
	"EO":"Encomenda Internacional - EMS",
	"EP":"Encomenda Internacional - EMS ",
	"EQ":"Encomenda de serviço não expressa (ECT)",
	"ER":"Objeto registrado",
	"ES":"e-SEDEX ou EMS ",
	"ET":"Encomenda Internacional - EMS",
	"EU":"Encomenda Internacional - EMS ",
	"EV":"Encomenda Internacional - EMS ",
	"EW":"Encomenda Internacional - EMS ",
	"EX":"Encomenda Internacional - EMS ",
	"EY":"Encomenda Internacional - EMS ",
	"EZ":"Encomenda Internacional - EMS ",
	"FA":"FAC registrado",
	"FE":"Encomenda FNDE",
	"FF":"Objeto registrado (DETRAN)",
	"FH":"FAC registrado com AR Digital",
	"FM":"FAC monitorado",
	"FR":"FAC registrado",
	"IA":"Logística Integrada (agendado / avulso)",
	"IC":"Logística Integrada (a cobrar) g",
	"ID":"Logística Integrada (devolução de documento)",
	"IE":"Logística Integrada (Especial)",
	"IF":"CPF",
	"II":"Logística Integrada (ECT)",
	"IK":"Logística Integrada com Coleta Simultânea",
	"IM":"Logística Integrada (Medicamentos)",
	"IN":"Correspondência e EMS recebido do Exterior",
	"IP":"Logística Integrada (Programada)",
	"IR":"Impresso Registrado",
	"IS":"Logística integrada standard (medicamentos)",
	"IT":"Remessa Expressa Medicamentos / Logística Integrada Termolábil",
	"IU":"Logística Integrada (urgente)",
	"IX":"EDEI Expresso",
	"JA":"Remessa econômica com AR Digital",
	"JB":"Remessa econômica com AR Digital",
	"JC":"Remessa econômica com AR Digital",
	"JD":"Remessa econômica Talão/Cartão",
	"JE":"Remessa econômica com AR Digital",
	"JF":"Remessa econômica com AR Digital",
	"JG":"Objeto registrado urgente/prioritário",
	"JH":"Objeto registrado urgente / prioritário",
	"JI":"Remessa econômica Talão/Cartão",
	"JJ":"Objeto registrado (Justiça)",
	"JK":"Remessa econômica Talão/Cartão",
	"JL":"Objeto registrado",
	"JM":"Mala Direta Postal Especial",
	"JN":"Objeto registrado econômico",
	"JO":"Objeto registrado urgente",
	"JP":"Receita Federal",
	"JQ":"Remessa econômica com AR Digital",
	"JR":"Objeto registrado urgente / prioritário",
	"JS":"Objeto registrado",
	"JT":"Objeto Registrado Urgente",
	"JV":"Remessa Econômica (c/ AR DIGITAL)",
	"LA":"SEDEX com Logística Reversa Simultânea em Agência",
	"LB":"e-SEDEX com Logística Reversa Simultânea em Agência",
	"LC":"Objeto Internacional (Prime)",
	"LE":"Logística Reversa Econômica",
	"LF":"Objeto Internacional (Prime)",
	"LI":"Objeto Internacional (Prime)",
	"LJ":"Objeto Internacional (Prime)",
	"LK":"Objeto Internacional (Prime)",
	"LM":"Objeto Internacional (Prime)",
	"LN":"Objeto Internacional (Prime)",
	"LP":"PAC com Logística Reversa Simultânea em Agência",
	"LS":"SEDEX Logística Reversa",
	"LV":"Logística Reversa Expressa",
	"LX":"Packet Standard / Econômica",
	"LZ":"Objeto Internacional (Prime)",
	"MA":"Serviços adicionais do Telegrama",
	"MB":"Telegrama (balcão)",
	"MC":"Telegrama (Fonado)",
	"MD":"SEDEX Mundi (Documento interno)",
	"ME":"Telegrama",
	"MF":"Telegrama (Fonado)",
	"MK":"Telegrama (corporativo)",
	"ML":"Fecha Malas (Rabicho)",
	"MM":"Telegrama (Grandes clientes)",
	"MP":"Telegrama (Pré-pago)",
	"MR":"AR digital",
	"MS":"Encomenda Saúde",
	"MT":"Telegrama (Telemail)",
	"MY":"Telegrama internacional (entrante)",
	"MZ":"Telegrama (Correios Online)",
	"NE":"Tele Sena resgatada",
	"NX":"EDEI Econômico (não urgente)",
	"PA":"Passaporte",
	"PB":"PAC",
	"PC":"PAC a Cobrar ",
	"PD":"PAC",
	"PE":"PAC",
	"PF":"Passaporte",
	"PG":"PAC",
	"PH":"PAC",
	"PI":"PAC",
	"PJ":"PAC",
	"PK":"PAC Extra Grande",
	"PL":"PAC",
	"PR":"Reembolso Postal",
	"QQ":"Objeto de teste (SIGEP Web)",
	"RA":"Objeto registrado / prioritário",
	"RB":"Carta registrada",
	"RC":"Carta registrada com Valor Declarado",
	"RD":"Remessa econômica ou objeto registrado (DETRAN) ",
	"RE":"Objeto registrado econômico",
	"RF":"Receita Federal",
	"RG":"Objeto registrado",
	"RH":"Objeto registrado com AR Digital",
	"RI":"Objeto registrado internacional prioritário",
	"RJ":"Objeto registrado",
	"RK":"Objeto registrado",
	"RL":"Objeto registrado",
	"RM":"Objeto registrado urgente",
	"RN":"Objeto registrado (SIGEPWEB ou Agência)",
	"RO":"Objeto registrado",
	"RP":"Reembolso Postal",
	"RQ":"Objeto registrado",
	"RR":"Objeto registrado",
	"RS":"Objeto registrado",
	"RT":"Remessa econômica Talão/Cartão",
	"RU":"Objeto registrado (ECT)",
	"RV":"Remessa econômica CRLV/CRV/CNH e Notificações com AR Digital",
	"RW":"Objeto internacional",
	"RX":"Objeto internacional",
	"RY":"Remessa econômica Talão/Cartão com AR Digital",
	"RZ":"Objeto registrado",
	"SA":"SEDEX",
	"SB":"SEDEX 10",
	"SC":"SEDEX a cobrar",
	"SD":"SEDEX ou Remessa Expressa (DETRAN)",
	"SE":"SEDEX",
	"SF":"SEDEX",
	"SG":"SEDEX",
	"SH":"SEDEX com AR Digital / SEDEX ou AR Digital",
	"SI":"SEDEX",
	"SJ":"SEDEX Hoje",
	"SK":"SEDEX",
	"SL":"SEDEX ",
	"SM":"SEDEX 12",
	"SN":"SEDEX ",
	"SO":"SEDEX",
	"SP":"SEDEX Pré-franqueado",
	"SQ":"SEDEX",
	"SR":"SEDEX",
	"SS":"SEDEX",
	"ST":"Remessa Expressa Talão/Cartão",
	"SU":"Encomenda de serviço expressa (ECT)",
	"SV":"Remessa Expressa CRLV/CRV/CNH e Notificações com AR Digital",
	"SW":"e-SEDEX",
	"SX":"SEDEX 10",
	"SY":"Remessa Expressa Talão/Cartão com AR Digital",
	"SZ":"SEDEX",
	"TC":"Objeto para treinamento",
	"TE":"Objeto para treinamento",
	"TS":"Objeto para treinamento",
	"VA":"Encomendas com valor declarado",
	"VC":"Encomendas",
	"VD":"Encomendas com valor declarado",
	"VE":"Encomendas",
	"VF":"Encomendas com valor declarado",
	"VV":"Objeto internacional",
	"XA":"Aviso de chegada (internacional)",
	"XM":"SEDEX Mundi",
	"XR":"Encomenda SUR Postal Expresso",
	"XX":"Encomenda SUR Postal 24 horas"}
	return listInfo[code]	

def help():
	None

#use regex to validate the codePacked
def toValidCodePacked(codePacked):
	return re.search(r'[A-Z]{2}[0-9]{9}BR',codePacked)


menu()

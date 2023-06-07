#!/usr/bin/python3.8

import re
lin = 0
lin2 = 0
lin3 = 0

modulo = [10]
modulo = ["scd"]
cliente = "None"
licenca = "None"
licenca = "None"
teste_cancelada = 0
quant_licencas = 0
teste_existente = 0
try:
 L = open('orig/Licencas', 'r+', encoding="utf-8")


 for linha in L:
    licenca = "None"
    teste_cancelada = 0
    teste_existente = 0
    lin = linha.split(',')
    
    if lin[0] == "#":
     continue
    
    # Definindo codigo do cliente
    C = open('Clientes', 'r', encoding="utf-8")
    
    for linha2 in C:
     lin2 = linha2.split(',')
     if lin2[0] == lin[0] :
      cliente = lin2[0]
      break
    
    C.close()
    # Encontrando as atualizadas e canceladas para descarte
    # Lista criada a partir do comando "find -name *_lic"
    AC = open('licencas23.txt', 'r', encoding="utf-8")
    lin[5] = re.sub('[\n$]','',lin[5])
    licenca_lista = lin[0] + "_" + lin[1] + "_Linux_" + lin[3] + "_" + lin[2] + "-" + lin[4] + "-" + lin[5] + "_lic"
    for linha in AC:
     lin3 = linha.split('/')

     # Verificando cliente
     if cliente != lin3[1]:
      continue

     # Verificando se cancelada/atualizada
     elif len(lin3) == 4 and (lin3[2] == "CANCELADAS" or lin3[2] == "ATUALIZADAS"):
      match_licenca_cancelada = re.match(licenca_lista,lin3[3])
      if match_licenca_cancelada:
       licenca = lin3[3]
       teste_cancelada = 1
       break
      continue
     
     # Verificando se existe a licenca na lista de arquivos

     match_licenca_existente = re.match(licenca_lista,lin3[2])
     if match_licenca_existente:
      teste_existente = 1

    AC.close()
    
    # Verifica flag de cancelada
    if teste_cancelada == 1:
     continue
     # -------------------
    
    # Verificando flag de arquivo existente e se é permanente

    if (int(lin[4]) == 0) and (int(teste_existente) == 1):
     validade_modulo = "NULL"
     print("Prazo: Permanente")
    else:
    # Comente o "continue para printar também lics temporárias"
     continue
     print(f"Prazo: {lin[4]} dias")

    # --------
    
    print(f"COD Cliente: {cliente}")

    licenciado = lin[0]
    print(f"Licenciado: {licenciado}")
    
    site = lin[1]
    print(f"Site: {site}")
    
    id = lin[2]
    print(f"ID: {id}")

    # Convertendo nome dos modulos

    if lin[3] == "sageiccp":
     lin[3] = "iccp"

    elif lin[3] == "sage61850":
     lin[3] = "61850"

    elif lin[3] == "sagesnmp":
     lin[3] = "snmp"

    modulo = lin[3]
    print(f"Modulo: {modulo}")
    
    if int(lin[5]) >= 2:
     redund = "Sim"
     print(f"Redundancia: {redund}")
    else:
     redund = "Não"
     print(f"Redundancia: {redund}")
    
    quant_licencas += 1

    ## Listando módulos do banco
   
   #tamMod = len(modulo) - 1 
    #contador = 0
    #while tamMod >= contador:
    # if lin[3] != modulo[contador]:
    #  if contador == tamMod:
    #   modulo.append(lin[3])
    #   break
    # elif lin[3] == modulo[contador]:
    #  break
    # contador += 1
    
    # Definindo data de geração
    posi_data_init = re.search(lin2[1], lin[2]).end()
    posi_data_finish = posi_data_init + 4 
    data = lin[2]
    data = data[posi_data_init:posi_data_finish]
    data = "01/" + data[0:2] + "/20" + data[2:4]
    print(f"Data: {data}\n")
    
 L.close()

except Exception as e :
 print(f"Arquivo de \"Licenças\" ou \"Clientes\" não encontrado ou erro encontrado nos arquivos: {e}")
else:
 print("Fim...")
 print(f"Quantidade de licenças listadas {quant_licencas}")

# print(f"Modulos identificados {modulo}")

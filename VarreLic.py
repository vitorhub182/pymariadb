#!/usr/bin/python3.8

import re
lin = 0
lin2 = 0
lin3 = 0

modulo = [10]
modulo = ["scd"]
cliente = "None"
licenca = "None"
teste = 0
quant_licencas = 0

try:
 L = open('orig/Licencas', 'r', encoding="utf-8")


 for linha in L:
    teste = 0
    lin = linha.split(',')
    
    if lin[0] == "#":
     continue
    
    # Definindo codigo do cliente
    C = open('Clientes', 'r', encoding="utf-8")
    
    for linha2 in C:
     lin2 = linha2.split(',')
     if lin2[0] == lin[0] :
      cliente = lin2[0]
      print(f"Cliente: {cliente}")
      break
    
    C.close()
    # Encontrando as atualizadas e canceladas para descarte
    # Lista criada a partir do comando "find -name *_lic"
    AC = open('licencas23.txt', 'r', encoding="utf-8")

    licenca_lista = lin[0] + "_" + lin[1]
    print(f"Licenca_lista: {licenca_lista}")
    for linha in AC:
     lin3 = linha.split('/')
     if cliente != lin3[1]:
      print("Cliente diferente...continua")
      continue
     if len(lin3) == 4:
      print("Verificando Match com o cliente")
      match_cliente = re.search("^" + cliente,lin3[3])
      if  match_cliente and (lin3[2] == "CANCELADAS" or lin3[2] == "ATUALIZADAS"):
       print("Verificando Match com a licenca")
       match_licenca = re.search("^" + licenca_lista,lin3[3])
       if match_licenca:
        licenca = lin3[3]
        print(f"Licenca descarte:{licenca}")
        teste = 1
        break
       #print(f"{cliente} : {lin3[1]}/{lin3[2]}/{lin3[3]}")
       continue
      continue
    AC.close()
    
    # TESTA SE É CANCELADA
    if teste == 1:
     break
    if int(lin[4]) == 0:
     print("Prazo: Permanente")
    else:
    # Comente o "continue para printar também lics temporárias"
     continue
     print(f"Prazo: {lin[4]} dias")

    # --------
    
    print(f"COD Cliente: {cliente}")
    print(f"Licenciado: {lin[0]}")
    print(f"Site: {lin[1]}")
    print(f"ID: {lin[2]}")

    if lin[3] == "sageiccp":
     lin[3] = "iccp"

    elif lin[3] == "sage61850":
     lin[3] = "61850"

    elif lin[3] == "sagesnmp":
     lin[3] = "snmp"

    print(f"Modulo: {lin[3]}")
    
    if int(lin[5]) == 2: 
     print("Redundancia: Sim")
    else:
     print("Redundancia: Não")
    
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
    print(f"Data: {data[0:2]}/{data[2:4]}")
    print("")
    
 L.close()

except Exception as e :
 print(f"Arquivo de \"Licenças\" ou \"Clientes\" não encontrado ou erro encontrado nos arquivos: {e}")
else:
 print("Fim...")
 print(f"Quantidade de licenças listadas {quant_licencas}")

# print(f"Modulos identificados {modulo}")

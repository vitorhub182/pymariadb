#!/usr/bin/python3.8

import re
lin = 0
lin2 = 0

modulo = [10]
modulo = ["scd"]

try:
 L = open('Licencas', 'r', encoding="utf-8")


 for linha in L:
    lin = linha.split(',')
    #tam = len(lin)
    #tam -= 1
    #lin[tam] = lin[tam].rstrip('\n')
    
    if int(lin[4]) == 0:
     print("Prazo: Permanente")
    else:
    # Comente o "continue para printar também lics temporárias"
     #continue
     print(f"Prazo: {lin[4]} dias")
    
    # Definindo codigo do cliente
    C = open('Clientes', 'r', encoding="utf-8")
    
    for linha2 in C:
     lin2 = linha2.split(',')
     if lin2[0] == lin[0] :
      break
    
    C.close()
    
    # --------
    
    print(f"COD Cliente: {lin2[1]}")
    print(f"Licenciado: {lin[0]}")
    print(f"Site: {lin[1]}")
    print(f"ID: {lin[2]}")

    #if lin[3] == "sageiccp"
    # lin[3] = "iccp"
    # print(f"Modulo: {lin[3]}")

    #elif lin[3] == "sage61850"
    # lin[3] = "61850"

    #elif lin[3] == "sagesnmp"
    # lin[3] = "snmp"

    #print(f"Modulo: {lin[3]}")
    #
    #if int(lin[5]) == 2: 
    # print("Redundancia: Sim")
    #else:
    # print("Redundancia: Não")
    
    # Listando módulos do banco
    tamMod = len(modulo) - 1 
    contador = 0
    while tamMod >= contador:
     if lin[3] != modulo[contador]:
      if contador == tamMod:
       modulo.append(lin[3])
       break
     elif lin[3] == modulo[contador]:
      break
     contador += 1
    # Definindo data de geração
    
    posi_data_init = re.search(lin2[1], lin[2]).end()
    posi_data_finish = posi_data_init + 4
    
    data = lin[2]
    data = data[posi_data_init:posi_data_finish]
    print(f"Data: {data[0:2]}/{data[2:4]}")
    print("")
    
    #try:
    # D = open("licencas23.txt",'r', encoding="utf-8")
    # 
    # for linha3 in D:
    #  lin3 = linha3.split('/')
    #   if lin3[2] ==  
    #  
    # 
    #except Exception:
    # print("Falha ao ler os arquivo de Diretorios")
    
 L.close()

except Exception as e :
 print(f"Arquivo de \"Licenças\" ou \"Clientes\" não encontrado ou erro encontrado nos arquivos: {e}")
else:
 print("Fim...")
 print(f"Modulos identificados {modulo}")

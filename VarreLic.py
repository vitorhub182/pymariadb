#!/usr/bin/python3.8

import re
lin = 0
lin2 = 0

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
     continue
     print(f"Prazo: {lin[4]} dias")
    
    # Definindo codigo do cliente
    try:
     C = open('Clientes', 'r', encoding="utf-8")
    
     for linha2 in C:
      lin2 = linha2.split(',')
      if lin2[0] == lin[0] :
       break
    
     C.close()
    
    except Exception:
     print("Arquivo de Clientes não encontrado ")
    # --------
    
    print(f"COD Cliente: {lin2[1]}")
    print(f"Licenciado: {lin[0]}")
    print(f"Site: {lin[1]}")
    print(f"ID: {lin[2]}")
    print(f"Modulo: {lin[3]}")
     
    if int(lin[5]) == 2: 
     print("Redundancia: Sim")
    else:
     print("Redundancia: Não")
    
    
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

except Exception:
 print("Arquivo de \"Licenças\" ou \"Clientes\" não encontrado ou erro encontrado nos arquivos")
else:
 print("Fim...")
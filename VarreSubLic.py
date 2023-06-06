#!/usr/bin/python3.8

import re

try:
 
 C = open('Clientes', 'r', encoding="utf-8")

 for line in C:
  clin = line.split(',')
  cliente = clin[0]

  L = open('licencas23.txt', 'r', encoding="utf-8")

  for linha in L:
     lin = linha.split('/')
     if len(lin) >= 4:
      match = re.search("^" + cliente,lin[3])
      if  match and (lin[2] == "CANCELADAS" or lin[2] == "ATUALIZADAS"):
       print(f"{cliente} : {lin[1]}/{lin[2]}/{lin[3]}")
      else:
       continue
      continue
     
  L.close()
 C.close()

except Exception as e :
 print(f"A lista  \"licencas23.txt\" não foi encontrado ou erro encontrado nos arquivos: {e}")
else:
 print("Fim...")

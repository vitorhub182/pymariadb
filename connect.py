#!/usr/bin/python3.8
import mariadb
import sys

busca = [10] 

#Insersão de Cliente
def insertCliente(cliente)
 
 sql = "insert into cliente (sigla,obs) values (%s, %s)"
 cur.execute(sql,(cliente,"Origem: Banco de dados SAGE 23",))
 
 sql = "select max(id) from cliente"
 cur.execute(sql)
 id_cliente = cur.fetchall()
 return id_cliente

# Insersão de Site
def insertSite(id_cliente)
 sql = "insert into empreendimento (id_cliente,site,descricao) values (%s,%s,%s)
 cur.execute(sql,(id_cliente,site,"SITE DE LICENCAS 23",)

 sql = "select max(id) from empreendimento"
 cur.execute(sql)
 id_empreendimento = cur.fetchall()
 return id_empreendimento

# Insersão de Lic
def insertLic(id_empreendimento):
 
 sql = "insert into licenca (mrid,id_licenciado,,tipo_licenca,versao_sage,release_sage,updates_ate,data_criacao,data_atualizacao,pfihm,cancelada) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
 cur.execute(sql,(id,id_cliente,id_empreendimento,"Producao",23, 00,data,data,data,0,0,)
 
 sql = "select max(id) from licenca"
 cur.execute(sql)
 id = cur.fetchall()
 return id


# Insersão de ambiente_licenca
def insertAl(id)
 sql = "insert into ambiente_licenca (mrid, id_amb, redundante, cancelada) values (%s,%s,%s,%s)"
 cur.execute(sql,(id,"tr", 1, 0)
 
 sql = "select max(id) from ambiente_licenca"
 id_al = cur.fetchall()
 return id_al

# Insersão de Módulo
def insertmod(id_al):
 if modulo == "sclone":
  sql = "insert into em ambiente_licenca (id,mrid,id_amb,redundante,cancelada) values (%s, %s, %s, %s, %s)"
  cur.execute(sql,(id_ambiente,result_lic,"clone", 1, 0,)
  id_al = id_ambiente
 elif modulo == "scd":
  sql = "insert into modulo_ambiente (id_ambiente_licenca, id_mdl, id_contratante, copias, data_criacao,data_validade, cancelada) values (%s, %s, %s, %s, %s, %s)"
  cur.execute(sql,(id_al, "ihm", id_cliente, redund,data ,"NULL",0,)

 sql = "insert into modulo_ambiente (id_ambiente_licenca, id_mdl, id_contratante, copias, data_criacao,data_validade, cancelada) values (%s, %s, %s, %s, %s, %s)"
 cur.execute(sql,(id_al, modulo, id_cliente, redund,data ,"NULL",0,)



def conexao(cliente,site,id,modulo,redund,data):
# Connect to MariaDB Platform

 try:
  conn = mariadb.connect(
   user="sagelicuser",
   password="sagelicpw",
   host="161.79.58.242",
   port=3306,
   database="sagelicbd"
  )
 except mariadb.Error as e:
  print(f"Erro ao connectar o MariaDB na Plataforma: {e}")
  sys.exit(1)
 # Get Cursor
         						
 cur = conn.cursor()
 # Verificando Cliente
 sql = "select c.id from cliente c where c.sigla = %s group by c.id"
 cur.execute(sql, (cliente,))
 result = cur.fetchall()
 id_cliente = result
 print(f"Id do cliente {id_cliente}")
 
 if result: 
   print("Cliente Encontrado\n")
   print("Verificando existencia de empreendimento...\n")
   
   # Verificando Empreendimento(site)
   sql = "select e.site from empreendimento where e.site = %s"
   cur.execute(sql, (site,))
   result = cur.fetchall()
   
   if result:
    print("Instalação encontrada\n")
    print("Verificando licenca...\n")
     

    sql = "select l.mrid from licenca l inner join empreendimento e on id.e = id_empreendimento where l.mrid = %s"
    cur.execute(sql,(id,))
    result = cur.fetchall()
    
    if result:
     print("Licenca encontrada\n")
     print("Verificando modulo...\n")
     
     sql = "select ma.id_ambiente_licenca from modulo_ambiente ma inner join ambiente_licenca al on al.id = ma.id_ambiente_licenca inner join licenca l on l.mrid = al.mrid where l.mrid = %s and ma.id_mdl = %s group by ma.id_ambiente_licenca"
     cur.execute(sql, (id,modulo,))
     id_mdl = cur.fetchall()
     if id_mdl:
      print("Modulo já registrado encontrado")
      print("Seguindo para a próxima licença...")
      continue
     else :
      print(f"Módulo {modulo}  não encontrado, inserindo-o na licenca: {id}")
    else :
     print("Licença não encontrada")
     print("Inserindo nova licença...")

     print("Inserindo módulo...")
   else :
 else :
  print("Cliente não encontrado\n")
  print("Inserindo novo cliente\n")

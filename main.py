import sqlite3
from django.conf.locale import sq
# Capturando informação

try:
    nome = input("Digite o seu nome: ")
    altura = float(input("Digite sua altura, (Ex. 1.70):"))
    peso = float(input("Digite o seu peso, (Ex. 65.3): "))
    resultado = peso / (altura * altura)
    print("Seu IMC: ", resultado)
except (ValueError, TypeError):
    print("Digite valores validos. Ex Altura 1.55, Peso = 70.5")
    
# Criando conexão
con = sqlite3.connect('imc.db')
cur = con.cursor()

# Criando tabela
sql = 'create table imc' \
      '(id integer primary key,' \
      'nome varchar(100),'\
      'altura real,'\
      'peso real,'\
      'resultado real)'

if(sql ==  False):
    cur.execute(sql)
# Fechando conexão
con.close()
print("Banco de Dados criado con sucesso.")

# Criando conexão
con = sqlite3.connect('imc.db')
cur = con.cursor()

# Sentença para inserir dados
sql = 'insert into imc values(null,?,?,?,?)'

lista = []
lista.append(nome)
lista.append(altura)
lista.append(peso)
lista.append(resultado)

cur.execute(sql, lista)

con.commit()
con.close()




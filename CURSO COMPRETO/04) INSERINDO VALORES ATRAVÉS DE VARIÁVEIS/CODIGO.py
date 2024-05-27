import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Define os valores a serem inseridos usando variáveis
nome = 'Bob'
telefone = '987654321'
email = 'bob@example.com'

# Insere os valores na tabela clientes usando variáveis
cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))

# Confirma as mudanças
conn.commit()

# Fecha a conexão
conn.close()

print("Registro inserido com sucesso.")

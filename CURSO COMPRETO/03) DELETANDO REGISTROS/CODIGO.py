import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Deleta um registro da tabela clientes onde o nome seja 'Alice'
cursor.execute("DELETE FROM clientes WHERE nome = ?", ('Alice',))

# Confirma as mudanças
conn.commit()

# Fecha a conexão
conn.close()

print("Registro deletado com sucesso.")

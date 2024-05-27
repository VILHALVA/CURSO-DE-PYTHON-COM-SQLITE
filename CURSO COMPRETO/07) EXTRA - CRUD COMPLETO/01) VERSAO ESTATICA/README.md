# EXTRA - CRUD COMPLETO
## VERSAO ESTATICA
Aqui está um exemplo de um CRUD completo (Create, Read, Update, Delete) em Python usando SQLite:

```python
import sqlite3

# Função para conectar ao banco de dados
def conectar():
    conn = sqlite3.connect('database.db')
    return conn

# Função para criar a tabela clientes
def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Função para inserir um novo cliente
def inserir_cliente(nome, telefone, email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    conn.close()

# Função para visualizar todos os clientes
def visualizar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

# Função para atualizar um cliente existente
def atualizar_cliente(id, novo_nome, novo_telefone, novo_email):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome = ?, telefone = ?, email = ? WHERE id = ?", (novo_nome, novo_telefone, novo_email, id))
    conn.commit()
    conn.close()

# Função para deletar um cliente
def deletar_cliente(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    conn.close()

# Criar a tabela clientes se ainda não existir
criar_tabela()

# Inserir alguns clientes de exemplo
inserir_cliente('João', '123456789', 'joao@example.com')
inserir_cliente('Maria', '987654321', 'maria@example.com')

# Visualizar todos os clientes
print("Todos os clientes:")
clientes = visualizar_clientes()
for cliente in clientes:
    print(cliente)

# Atualizar o cliente com id=1
atualizar_cliente(1, 'João da Silva', '987654321', 'joao.silva@example.com')

# Visualizar todos os clientes novamente
print("\nTodos os clientes após a atualização:")
clientes_atualizados = visualizar_clientes()
for cliente in clientes_atualizados:
    print(cliente)

# Deletar o cliente com id=2
deletar_cliente(2)

# Visualizar todos os clientes novamente após a exclusão
print("\nTodos os clientes após a exclusão:")
clientes_depois_exclusao = visualizar_clientes()
for cliente in clientes_depois_exclusao:
    print(cliente)
```

Este é um exemplo simples de como realizar operações CRUD em um banco de dados SQLite usando Python. Ele cria uma tabela de clientes, insere alguns clientes de exemplo, visualiza todos os clientes, atualiza um cliente existente, exclui um cliente e, em seguida, visualiza os clientes novamente para mostrar as alterações.
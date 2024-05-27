# EXTRA - CRUD COMPLETO
## VERSAO COM INPUT
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
def inserir_cliente():
    nome = input("Digite o nome do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO clientes (nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conn.commit()
    print("Cliente inserido com sucesso.")
    conn.close()

# Função para visualizar todos os clientes
def visualizar_clientes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    if clientes:
        print("Todos os clientes:")
        for cliente in clientes:
            print(cliente)
    else:
        print("Nenhum cliente encontrado.")

# Função para atualizar um cliente existente
def atualizar_cliente():
    id = input("Digite o ID do cliente que deseja atualizar: ")
    novo_nome = input("Digite o novo nome do cliente: ")
    novo_telefone = input("Digite o novo telefone do cliente: ")
    novo_email = input("Digite o novo email do cliente: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE clientes SET nome = ?, telefone = ?, email = ? WHERE id = ?", (novo_nome, novo_telefone, novo_email, id))
    conn.commit()
    print("Cliente atualizado com sucesso.")
    conn.close()

# Função para deletar um cliente
def deletar_cliente():
    id = input("Digite o ID do cliente que deseja deletar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id,))
    conn.commit()
    print("Cliente deletado com sucesso.")
    conn.close()

# Criar a tabela clientes se ainda não existir
criar_tabela()

# Menu de opções
while True:
    print("\n=== MENU ===")
    print("1. Inserir cliente")
    print("2. Visualizar clientes")
    print("3. Atualizar cliente")
    print("4. Deletar cliente")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        inserir_cliente()
    elif opcao == '2':
        visualizar_clientes()
    elif opcao == '3':
        atualizar_cliente()
    elif opcao == '4':
        deletar_cliente()
    elif opcao == '5':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
```

Este código permite:

1. Inserir um novo cliente, onde você digita o nome, telefone e email.
2. Visualizar todos os clientes cadastrados.
3. Atualizar um cliente existente, onde você informa o ID do cliente e os novos dados.
4. Deletar um cliente, onde você informa o ID do cliente a ser deletado.
5. Sair do programa.

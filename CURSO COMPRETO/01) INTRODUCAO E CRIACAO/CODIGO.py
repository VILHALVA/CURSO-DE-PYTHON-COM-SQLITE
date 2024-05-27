import sqlite3

# Função para criar a conexão e a tabela
def create_database():
    # Conecta ao banco de dados (ou cria um novo se não existir)
    conn = sqlite3.connect('database.db')
    # Cria um cursor
    cursor = conn.cursor()
    # Cria a tabela clientes se não existir
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            telefone TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    # Confirma as mudanças
    conn.commit()
    # Fecha a conexão
    conn.close()
    print("Banco de dados e tabela 'clientes' criados com sucesso.")

# Função para inserir dados na tabela clientes
def insert_data():
    # Conecta ao banco de dados
    conn = sqlite3.connect('database.db')
    # Cria um cursor
    cursor = conn.cursor()
    # Dados a serem inseridos
    clientes = [
        ('Alice', '123456789', 'alice@example.com'),
        ('Bob', '987654321', 'bob@example.com'),
        ('Carol', '555123456', 'carol@example.com')
    ]
    # Insere os dados na tabela
    cursor.executemany('''
        INSERT INTO clientes (nome, telefone, email)
        VALUES (?, ?, ?)
    ''', clientes)
    # Confirma as mudanças
    conn.commit()
    # Fecha a conexão
    conn.close()
    print("Dados inseridos com sucesso na tabela 'clientes'.")

# Função para selecionar e exibir os dados da tabela clientes
def select_data():
    # Conecta ao banco de dados
    conn = sqlite3.connect('database.db')
    # Cria um cursor
    cursor = conn.cursor()
    # Seleciona todos os registros da tabela clientes
    cursor.execute('SELECT * FROM clientes')
    # Obtém todos os registros
    rows = cursor.fetchall()
    # Exibe os registros
    print("Registros na tabela 'clientes':")
    for row in rows:
        print(row)
    # Fecha a conexão
    conn.close()

# Executa as funções
create_database()
insert_data()
select_data()

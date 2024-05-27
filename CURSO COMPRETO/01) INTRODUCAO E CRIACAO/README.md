# INTRODUÇÃO E CRIAÇÃO
## Conceito
Python com SQLite é uma combinação poderosa para a criação e manipulação de bancos de dados. SQLite é um sistema de gerenciamento de banco de dados relacional embutido que armazena dados em um único arquivo. Ele é conhecido por sua simplicidade, leveza e não requerer uma configuração de servidor, o que o torna ideal para aplicações menores, desenvolvimento local e prototipagem rápida.

## Instalação
A biblioteca `sqlite3` vem incluída na instalação padrão do Python, portanto, não é necessário instalar pacotes adicionais para começar a trabalhar com SQLite em Python.

## Configuração
A configuração é simples, pois não há necessidade de configurar um servidor de banco de dados. Basta importar a biblioteca `sqlite3` e criar uma conexão com um banco de dados (o arquivo será criado automaticamente se não existir).

## Criando Banco de Dados e Tabela
Vamos criar um banco de dados chamado `database.db` e uma tabela chamada `clientes` usando Python.

1. **Crie um arquivo Python:**
   Crie um novo arquivo chamado `create_database.py`.

2. **Importe a biblioteca SQLite e crie a conexão:**
   No arquivo `create_database.py`, adicione o seguinte código:

```python
import sqlite3

# Conecta ao banco de dados (ou cria um novo se não existir)
conn = sqlite3.connect('database.db')

# Cria um cursor
cursor = conn.cursor()

# Cria a tabela clientes
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
```

## Explicação do Código:
- `import sqlite3`: Importa a biblioteca `sqlite3`.
- `sqlite3.connect('database.db')`: Cria uma conexão com o banco de dados chamado `database.db`. Se o arquivo não existir, ele será criado automaticamente.
- `conn.cursor()`: Cria um cursor para executar comandos SQL.
- `cursor.execute(...)`: Executa um comando SQL para criar a tabela `clientes` se ela não existir.
- `conn.commit()`: Confirma as mudanças no banco de dados.
- `conn.close()`: Fecha a conexão com o banco de dados.

## Inserindo Dados e Selecionando Registros
Vamos estender o exemplo anterior para inserir dados na tabela `clientes` e depois consultar esses registros usando o comando `SELECT`.

1. **Crie um arquivo Python:**
   Crie um novo arquivo chamado `CODIGO.py`.

2. **Importe a biblioteca SQLite, crie a conexão e a tabela (se ainda não existir):**
   No arquivo `CODIGO.py`, adicione o seguinte código:

```python
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
```

## Explicação do Código:
- **Função `create_database`:**
  - Conecta ao banco de dados, cria a tabela `clientes` se não existir, e fecha a conexão.

- **Função `insert_data`:**
  - Conecta ao banco de dados, insere múltiplos registros na tabela `clientes` usando `executemany`, e fecha a conexão.

- **Função `select_data`:**
  - Conecta ao banco de dados, seleciona todos os registros da tabela `clientes`, exibe os registros, e fecha a conexão.

- **Execução das Funções:**
  - Chama as funções `create_database`, `insert_data`, e `select_data` para criar a tabela, inserir dados e exibir os registros.

## Executando o Código:
1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `insert_and_select.py` está localizado.
3. Execute o código com o comando:

```bash
python CODIGO.py
```

## Conclusão:
O código criará a tabela `clientes` (se ainda não existir), inserirá alguns registros de exemplo e, em seguida, selecionará e exibirá esses registros. Esse exemplo mostra como manipular dados em um banco de dados SQLite usando Python, incluindo a criação de tabelas, inserção de dados e execução de consultas para recuperação de dados.

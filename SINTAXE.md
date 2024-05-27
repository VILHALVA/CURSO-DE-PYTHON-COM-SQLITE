# SINTAXE
## PROJETO SIMPLES:
Um exemplo simples de como Python pode ser usado para interagir com um banco de dados SQLite:

```python
import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('exemplo.db')

# Criar um cursor para interagir com o banco de dados
cursor = conn.cursor()

# Criar uma tabela
cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER
    )
''')

# Inserir dados
cursor.execute('''
    INSERT INTO usuarios (nome, idade)
    VALUES ('Alice', 30)
''')

# Salvar (commit) as mudanças
conn.commit()

# Consultar dados
cursor.execute('SELECT * FROM usuarios')
print(cursor.fetchall())

# Fechar a conexão
conn.close()
```

Neste exemplo, um banco de dados SQLite chamado `exemplo.db` é criado, uma tabela `usuarios` é definida e preenchida com dados, e depois os dados são consultados e exibidos. Esta é a base para entender como Python pode interagir com SQLite, oferecendo uma solução simples e eficaz para gerenciamento de dados.

## CRUD COMPLETO:
Neste tutorial, vamos criar um aplicativo CRUD (Create, Read, Update, Delete) usando Python e SQLite. O banco de dados `database.db` será criado no mesmo diretório do código Python.

### PASSO 1: CONFIGURAÇÃO DO AMBIENTE
1. Certifique-se de ter Python instalado em seu sistema.
2. A biblioteca `sqlite3` é incluída na biblioteca padrão do Python, então não é necessário instalar pacotes adicionais.

### PASSO 2: ESTRUTURA DO PROJETO
Crie um diretório para o seu projeto e dentro deste diretório crie um arquivo chamado `crud.py`.

### PASSO 3: CÓDIGO DO CRUD
Abra o arquivo `crud.py` e adicione o seguinte código:

```python
import sqlite3

# Função para criar a conexão com o banco de dados
def create_connection():
    conn = sqlite3.connect('database.db')
    return conn

# Função para criar a tabela
def create_table(conn):
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

# Função para inserir um cliente
def create_client(conn, nome, telefone, email):
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO clientes (nome, telefone, email)
        VALUES (?, ?, ?)
    ''', (nome, telefone, email))
    conn.commit()

# Função para ler todos os clientes
def read_clients(conn):
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# Função para atualizar um cliente
def update_client(conn, client_id, nome, telefone, email):
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE clientes
        SET nome = ?, telefone = ?, email = ?
        WHERE id = ?
    ''', (nome, telefone, email, client_id))
    conn.commit()

# Função para deletar um cliente
def delete_client(conn, client_id):
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM clientes
        WHERE id = ?
    ''', (client_id,))
    conn.commit()

# Função principal para executar o CRUD
def main():
    conn = create_connection()
    create_table(conn)
    
    while True:
        print("\n1. Adicionar Cliente")
        print("2. Listar Clientes")
        print("3. Atualizar Cliente")
        print("4. Deletar Cliente")
        print("5. Sair")
        
        choice = input("Escolha uma opção: ")
        
        if choice == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            create_client(conn, nome, telefone, email)
        elif choice == '2':
            read_clients(conn)
        elif choice == '3':
            client_id = int(input("ID do Cliente: "))
            nome = input("Novo Nome: ")
            telefone = input("Novo Telefone: ")
            email = input("Novo Email: ")
            update_client(conn, client_id, nome, telefone, email)
        elif choice == '4':
            client_id = int(input("ID do Cliente: "))
            delete_client(conn, client_id)
        elif choice == '5':
            conn.close()
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()
```

### PASSO 4: EXECUTANDO O CÓDIGO
1. Abra um terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `crud.py` está localizado.
3. Execute o código com o comando:

```bash
python crud.py
```

### PASSO 5: UTILIZANDO O CRUD
Você verá o seguinte menu:

```
1. Adicionar Cliente
2. Listar Clientes
3. Atualizar Cliente
4. Deletar Cliente
5. Sair
Escolha uma opção:
```

- **Adicionar Cliente**: Insira o nome, telefone e email do cliente.
- **Listar Clientes**: Exibe todos os clientes no banco de dados.
- **Atualizar Cliente**: Atualiza as informações de um cliente existente pelo ID.
- **Deletar Cliente**: Deleta um cliente pelo ID.
- **Sair**: Fecha a conexão com o banco de dados e encerra o programa.

### CONCLUSÃO
Você criou um CRUD simples utilizando Python e SQLite. Este exemplo cobre as operações básicas de criar, ler, atualizar e deletar registros em um banco de dados SQLite. Para projetos maiores, considere a utilização de frameworks como Flask ou Django, que oferecem suporte integrado a bancos de dados e facilitam o desenvolvimento de aplicações web complexas.

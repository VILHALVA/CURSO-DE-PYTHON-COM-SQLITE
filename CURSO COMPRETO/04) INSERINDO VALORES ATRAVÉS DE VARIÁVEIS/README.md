# INSERINDO VALORES ATRAVÉS DE VARIÁVEIS
Para inserir valores em uma tabela SQLite usando variáveis em Python, você pode fazer algo assim:

```python
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
```

Neste exemplo, definimos as variáveis `nome`, `telefone` e `email` com os valores que queremos inserir na tabela `clientes`. Então, utilizamos essas variáveis na query SQL dentro do método `execute()`, substituindo os valores estáticos. 

Isso nos permite inserir valores dinâmicos na tabela usando variáveis Python. Certifique-se de substituir `'database.db'` pelo nome do seu banco de dados SQLite.
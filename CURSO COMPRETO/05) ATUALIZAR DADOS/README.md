# ATUALIZAR DADOS
Para atualizar dados em uma tabela SQLite usando Python, você pode seguir este exemplo:

```python
import sqlite3

# Conecta ao banco de dados
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Define os novos valores
novo_telefone = '999999999'
novo_email = 'novobob@example.com'

# Atualiza os dados na tabela clientes onde o nome seja 'Bob'
cursor.execute("UPDATE clientes SET telefone = ?, email = ? WHERE nome = ?", (novo_telefone, novo_email, 'Bob'))

# Confirma as mudanças
conn.commit()

# Fecha a conexão
conn.close()

print("Dados atualizados com sucesso.")
```

Neste exemplo, estamos atualizando os valores da tabela `clientes` para um novo telefone e email onde o nome seja 'Bob'. Você pode modificar a condição `WHERE` conforme necessário para atender aos seus critérios de atualização. Certifique-se de substituir `'Bob'` pelos valores apropriados.
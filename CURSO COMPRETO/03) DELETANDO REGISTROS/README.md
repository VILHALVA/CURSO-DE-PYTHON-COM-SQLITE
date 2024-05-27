# DELETANDO REGISTROS
Para deletar registros de uma tabela SQLite usando Python, você pode seguir este exemplo:

```python
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
```

Neste exemplo, estamos deletando registros da tabela `clientes` onde o nome seja 'Alice'. Você pode modificar a condição `WHERE` conforme necessário para atender aos seus critérios de exclusão. Certifique-se de substituir `'Alice'` pelo valor que deseja buscar para deletar.

Após executar o script, o registro correspondente será deletado da tabela `clientes` no banco de dados. Certifique-se de substituir `'database.db'` pelo nome do seu banco de dados SQLite.
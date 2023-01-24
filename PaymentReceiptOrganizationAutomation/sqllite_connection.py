import sqlite3

conn = sqlite3.connect('contas.db')

c = conn.cursor()

# c.execute("""CREATE TABLE  contas (
#             descricao text,
#             data text
#             )""")

def insert_conta(conta):
    conn = sqlite3.connect('contas.db')
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO contas VALUES (:descricao, :data)", {'descricao': conta.descricao, 'data': conta.data})



conn.commit()

conn.close()
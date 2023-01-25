import sqlite3

dbPath = 'E:\Daniel\Programacao\Projetos Completos\PaymentReceiptOrganizationAutomation.git\PaymentReceiptOrganizationAutomation\contas.db'

conn = sqlite3.connect(dbPath)

c = conn.cursor()

# c.execute("""CREATE TABLE  contas (
#             descricao text,
#             data text
#             )""")

def insert_conta(conta):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO contas VALUES (:descricao, :data)", {'descricao': conta.descricao, 'data': conta.data})



conn.commit()

conn.close()
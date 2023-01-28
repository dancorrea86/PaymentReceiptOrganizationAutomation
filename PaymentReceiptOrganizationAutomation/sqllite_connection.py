import sqlite3

dbPath = 'E:\Daniel\Programacao\Projetos Completos\PaymentReceiptOrganizationAutomation.git\PaymentReceiptOrganizationAutomation\contas.db'

conn = sqlite3.connect(dbPath)

c = conn.cursor()

# c.execute("""CREATE TABLE  contas (
#             id integer PRIMARY KEY AUTOINCREMENT NOT NULL,
#             descricao text,
#             data text,
#             arquivo text
#             )""")

def insert_conta(conta):
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()
    with conn:
        c.execute("INSERT INTO contas VALUES (:id, :descricao, :data, :arquivo)", (None, conta.descricao, conta.data, conta.arquivo))



conn.commit()

conn.close()
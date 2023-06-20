- Projeto para mover arquivos de comprovantes de Pagamentos.

Projeto para automação do processo de mover arquivos, o sistema organiza os comprovantes na pasta desejada por mês e ano.

Os arquivos a serem movidos devem possuir a seguinte nomenclatura:

- Comprovantes
"yyyy-mm-dd - ['nomeDoArquivo' Comprovante.pdf]
Exemplo: 2022-10-01 - Pagamento X Comprovante.pdf

- Boletos
"yyyy-mm-dd - ['nomeDoArquivo' Boleto Pago.pdf]
Exemplo: 2022-10-01 - Pagamento X Boleto Pago.pdf

- Utilização

Para utilização altere no código os caminhos das pastas de oritem e destino ao chama o método "main" e rodo a aplicação utilizando o comando:

Python PaymentReceiptOrganizationAutomation.py

Também é possível criar um executábel utilizando o módulo Pyinstaller. Instale o módulo utilizando o comando:

pip install pyinstaller

Após a instalação do módulo, rodo o comando:
pyinstaller --onefile -i="imagens/Frm_Principal.ico" main.py

- Lista de tarefas

[x] Listar todos arquivos do diretório
[x] Filtrar arquivos conforme necessidade
[x] Mover arquivos
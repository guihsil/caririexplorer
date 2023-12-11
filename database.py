import sqlite3
import os

#PONTOS TURÍSTICOS
def carrega_schemaPT():
    arquivo = open("schema_ponto_tur.sql", "r")
    schema = ""
    for linha in arquivo.readlines():
        schema += linha
    arquivo.close()
    return schema

def cria_tabelaPT():
    con = sqlite3.connect('bd_ponto_tur.sqlite')
    cursor = con.cursor()
    cursor.execute(carrega_schemaPT())
    con.commit()
    con.close()
    print('Feity!!!')

def insere_dadosPT(diretorio):
    con = sqlite3.connect('bd_ponto_tur.sqlite')
    cursor = con.cursor()
    with open(diretorio, 'r') as f:
        dados = [linha for linha in f]
    nome = dados[0]
    endereco = dados[1]
    cidade = dados[2]
    categoria = dados[3]
    horariofunc = dados[4]
    descricao = dados[5]
    cursor.execute('INSERT INTO pontos_turisticos (nome, endereco, cidade, categoria, horariofunc, descricao) VALUES (?, ?, ?, ?, ?, ?)', (nome, endereco, cidade, categoria, horariofunc, descricao))
    con.commit()
    con.close()
    print('\nDados adicionados com sucesso!!')

def testa_dadosPT(diretorio):
    os.system('cls')
    with open(diretorio, 'r') as f:
        dados = [linha for linha in f]
    print('Nome: ', dados[0])
    print('Endereço: ', dados[1])
    print('Cidade: ', dados[2])
    #print('Categoria: ', dados[3]) #Sugestão de ocultar essa opção
    print('Horario de funcionamento: ', dados[4])
    print('Descrição: ', dados[5])

def remove_dadosPT():
    id = int(input('ID a ser removido: '))
    con = sqlite3.connect('bd_ponto_tur.sqlite')
    cursor = con.cursor()
    cursor.execute('DELETE FROM pontos_turisticos WHERE id=?', (id,))
    con.commit()
    con.close()
    print('Dados removidos com sucesso!!')

#RESTAURANTES
def carrega_schemaR():
    arquivo = open("schema_restaurante.sql", "r")
    schema = ""
    for linha in arquivo.readlines():
        schema += linha
    arquivo.close()
    return schema

def cria_tabelaR():
    con = sqlite3.connect('bd_principal.sqlite')
    cursor = con.cursor()
    cursor.execute(carrega_schemaR())
    con.commit()
    con.close()
    print('Feity!!!')

def insere_dadosR(diretorio):
    con = sqlite3.connect('bd_restaurantes.sqlite')
    cursor = con.cursor()
    with open(diretorio, 'r') as f:
        dados = [linha for linha in f]
    nome = dados[0]
    nota = dados[1]
    endereco = dados[2]
    cidade = dados[3]
    horariofunc = dados[4]
    tipocomida = dados[5]
    descricao = dados[6]
    cursor.execute('INSERT INTO restaurante (nome, nota, endereco, cidade, horariofunc, tipocomida, descricao) VALUES (?, ?, ?, ?, ?, ?, ?)', (nome, nota, endereco, cidade, horariofunc, tipocomida, descricao))
    con.commit()
    con.close()
    print('\nDados adicionados com sucesso!!')

def transfere_bdR():
    con = sqlite3.connect('bd_restaurantes.sqlite')
    con2 = sqlite3.connect('bd_principal.sqlite')
    cursor = con.cursor()
    cursor2 = con2.cursor()
    cursor.execute('SELECT *FROM restaurante')
    for dados in cursor.fetchall():
        cursor2.execute('''INSERT INTO restaurantes 
        (nome, nota, endereco, cidade, horariofunc, tipocomida, descricao) 
        VALUES (?, ?, ?, ?, ?, ?, ?)''', 
        (dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7]))
        con2.commit()
    con2.close()

    con.close()
    print('Feito!')

def testa_dadosR(diretorio):
    os.system('cls')
    with open(diretorio, 'r') as f:
        dados = [linha for linha in f]
    print('Nome: ', dados[0])
    print('Nota: ', dados[1])
    print('Endereço: ', dados[2])
    print('Cidade: ', dados[3])
    print('Horario de funcionamento: ', dados[4])
    print('Tipo de comida: ', dados[5])
    print('Descrição: ', dados[6])

def remove_dadosR():
    id = int(input('ID a ser removido: '))
    con = sqlite3.connect('bd_restaurantes.sqlite')
    cursor = con.cursor()
    cursor.execute('DELETE FROM restaurante WHERE id=?', (id,))
    con.commit()
    con.close()
    print('Dados removidos com sucesso!!')

#EVENTOS
def carrega_schemaE():
    arquivo = open ("schema_eventos.sql", "r")
    schema = ""
    for linha in arquivo.readlines():
        schema += linha
    arquivo.close()
    return schema

def cria_tabelaE():
    con = sqlite3.connect('bd_principal.sqlite')
    cursor = con.cursor()
    cursor.execute(carrega_schemaE())
    con.commit()
    con.close()
    print('Feity!!!')

def insere_dadosE(diretorio):
    con = sqlite3.connect('bd_eventos.sqlite')
    cursor = con.cursor()
    with open(diretorio, 'r') as f:
        dados = [linha for linha in f]
    titulo = dados[0]
    tipo = dados[1] 
    datahorario = dados[2]
    custoentrada = dados [3]
    endereco = dados[4]
    cidade = dados[5]
    descricao = dados[6]
    cursor.execute('INSERT INTO eventos (titulo, tipo, datahorario, custoentrada, endereco, cidade, descricao) VALUES (?, ?, ?, ?, ?, ?, ?)', (titulo, tipo, datahorario, custoentrada, endereco, cidade, descricao))
    con.commit()
    con.close()
    print('\nDados adicionados com sucesso!!')

def transfere_bdE():
    con = sqlite3.connect('bd_eventos.sqlite')
    conn = sqlite3.connect('bd_principal.sqlite')
    cursor2 = conn.cursor()
    cursor = con.cursor()
    cursor.execute('SELECT *FROM eventos')
    for dados in cursor.fetchall():
        cursor2.execute('INSERT INTO eventos (titulo, tipo, datahorario, custoentrada, endereco, cidade, descricao) VALUES (?, ?, ?, ?, ?, ?, ?)', (dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7]))
        conn.commit()
    conn.close()

    con.close()
    print('Feity!!!')

def testa_dadosE(diretorio):
    os.system('cls')
    with open(diretorio, 'r') as f:
        dados = [linha for linha in f]
    print('Título do Evento: ', dados[0])
    print('Data | Horário: ', dados[2])
    print ('Ingresso / Entrada: ', dados[3])
    print('Endereço: ', dados[4])
    print('Cidade: ', dados[5])
    print('Descrição: ', dados[6])

def remove_dadosE():
    id = int(input('ID a ser removido: '))
    con = sqlite3.connect('bd_eventos.sqlite')
    cursor = con.cursor()
    cursor.execute('DELETE FROM eventos WHERE id=?', (id,))
    con.commit()
    con.close()
    print('Dados removidos com sucesso!!')

#HOSPEDAGEM
def carrega_schemaH():
    arquivo = open ("schema_hospedagens.sql", "r")
    schema = ""
    for linha in arquivo.readlines():
        schema += linha
    arquivo.close()
    return schema

def cria_tabelaH():
    con = sqlite3.connect('bd_principal.sqlite')
    cursor = con.cursor()
    cursor.execute(carrega_schemaH())
    con.commit()
    con.close()
    print('Feity!!!')

def insere_dadosH(diretorio):
    con = sqlite3.connect('bd_hospedagem.sqlite')
    cursor = con.cursor()
    with open(diretorio, 'r') as f:
        dados_hosp = [linha for linha in f]
    cidade = dados_hosp [0]
    nome = dados_hosp[1]
    avaliacao = dados_hosp[2]
    preco = dados_hosp [3]
    endereco = dados_hosp[4]
    contato = dados_hosp[5]
    descricao = dados_hosp[6]
    cursor.execute('INSERT INTO hospedagem (cidade, nome, avaliacao, preco, endereco, contato, descricao) VALUES (?, ?, ?, ?, ?, ?, ?)', (cidade, nome, avaliacao, preco, endereco, contato, descricao))
    con.commit()
    con.close()
    print('Dados adicionados com sucesso.')

def transfere_bdH():
    con = sqlite3.connect('bd_hospedagem.sqlite')
    conn = sqlite3.connect('bd_principal.sqlite')
    cursor2 = conn.cursor()
    cursor = con.cursor()
    cursor.execute('SELECT *FROM hospedagem')
    for dados in cursor.fetchall():
        cursor2.execute('INSERT INTO hospedagens (cidade, nome, avaliacao, preco, endereco, contato, descricao) VALUES (?, ?, ?, ?, ?, ?, ?)', (dados[1], dados[2], dados[3], dados[4], dados[5], dados[6], dados[7]))
        conn.commit()
    conn.close()

    con.close()
    print('Feity!!!')

def testa_dadosH(diretorio):
    os.system('cls')
    with open(diretorio, 'r') as f:
        dados_hosp = [linha for linha in f]
    print('Cidade: ', dados_hosp[0])
    print('Nome: ', dados_hosp[1])
    print('Avaliação: ', dados_hosp[2])
    print('Preço: ', dados_hosp[3])
    print('Endereço: ', dados_hosp[4])
    print('Contato: ', dados_hosp[5])
    print('Descrição:', dados_hosp[6])

def remove_dadosH():
    id = int(input('ID a ser removido: '))
    con = sqlite3.connect('bd_hospedagem.sqlite')
    cursor = con.cursor()
    cursor.execute('DELETE FROM hospedagem WHERE id=?', (id,))
    con.commit()
    con.close()
    print('Dados removidos com sucesso.')

#PROGRAMA PRINCIPAL!!!
def menu_tabela():
    os.system('cls')
    print('#################################')
    print('## Ferramenta de Administrador ##')
    print('########## Menu Tabela ##########')
    print('#################################\n')

    print('1. Tabela Pontos Turísticos')
    print('2. Tabela Restaurantes')
    print('3. Tabela Eventos')
    print('4. Tabela Hospedagem')
    print('\n')
    opcao = int(input('Opção: '))
    print('\n')

    if opcao == 1:
        cria_tabelaPT()
    elif opcao == 2:
        cria_tabelaR()
    elif opcao == 3:
        cria_tabelaE()
    elif opcao == 4:
        cria_tabelaH()

def insere_dados(diretorio):
    os.system('cls')
    print('#################################')
    print('## Ferramenta de Administrador ##')
    print('########## Insere Dados ##########')
    print('#################################\n')

    print('1. Tabela Pontos Turísticos')
    print('2. Tabela Restaurantes')
    print('3. Tabela Eventos')
    print('4. Tabela Hospedagem')
    print('\n')
    opcao = int(input('Opção: '))
    print('\n')

    if opcao == 1:
        insere_dadosPT(diretorio)
    elif opcao == 2:
        insere_dadosR(diretorio)
    elif opcao == 3:
        cria_tabelaE(diretorio)
    elif opcao == 4:
        cria_tabelaH(diretorio)

def testa_dados(diretorio):
    os.system('cls')
    print('#################################')
    print('## Ferramenta de Administrador ##')
    print('######## Teste de Dados #########')
    print('#################################\n')

    print('1. Tabela Pontos Turísticos')
    print('2. Tabela Restaurantes')
    print('3. Tabela Eventos')
    print('4. Tabela Hospedagem')
    print('\n')
    opcao = int(input('Opção: '))
    print('\n')

    if opcao == 1:
        testa_dadosPT(diretorio)
    elif opcao == 2:
        testa_dadosR(diretorio)
    elif opcao == 3:
        testa_dadosE(diretorio)
    elif opcao == 4:
        testa_dadosH(diretorio)

def remove_dados():
    os.system('cls')
    print('#################################')
    print('## Ferramenta de Administrador ##')
    print('######### Remover Dados #########')
    print('#################################\n')

    print('1. Tabela Pontos Turísticos')
    print('2. Tabela Restaurantes')
    print('3. Tabela Eventos')
    print('4. Tabela Hospedagem')
    print('\n')
    opcao = int(input('Opção: '))
    print('\n')

    if opcao == 1:
        remove_dadosPT()
    elif opcao == 2:
        remove_dadosR()
    elif opcao == 3:
        remove_dadosE()
    elif opcao == 4:
        remove_dadosH()

def transfere_bd():
    os.system('cls')
    print('#################################')
    print('## Ferramenta de Administrador ##')
    print('#### Transferência de Dados #####')
    print('#################################\n')

    print('1. Tabela Restaurantes')
    print('2. Tabela Eventos')
    print('3. Tabela Hospedagem')
    print('\n')
    opcao = int(input('Opção: '))
    print('\n')

    if opcao == 1:
        transfere_bdR()
    elif opcao == 2:
        transfere_bdE()
    elif opcao == 3:
        transfere_bdH()

def volta_menu():
    voltarmenu = input("Deseja voltar ao menu principal? (S/N) ")
    if voltarmenu.upper() == 'S':
        menu()

def menu():
    os.system('cls')
    print('#################################')
    print('## Ferramenta de Administrador ##')
    print('######## Menu Principal #########')
    print('#################################\n')

    print('1. Criar Tabela')
    print('2. Inserir Dados')
    print('3. Teste de Input')
    print('4. Remover Dados')
    print('5. Transferência de Dados')
    print('\n')
    opcao = int(input('Opção: '))
    print('\n')

    if opcao == 1:
        menu_tabela()
        volta_menu()
    elif opcao == 2:
        diretorio = input('Digite o diretório do arquivo: ')
        insere_dados(diretorio)
        volta_menu()
    elif opcao == 3:
        diretorio = input('Digite o diretório do arquivo: ')
        testa_dados(diretorio)
        volta_menu()
    elif opcao == 4:
        remove_dados()
        volta_menu()
    elif opcao == 5:
        transfere_bd()
        volta_menu()

menu()
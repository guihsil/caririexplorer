import telebot
import sqlite3
import os

def main(token):

    bot = telebot.TeleBot(token)
    print(f'O bot está rodando a api: {token}')

    @bot.message_handler(commands=['start'])
    def start_message(message):
        bot.send_message(message.chat.id, 
'''🌍 Bem-vindo ao CaririExplorer, seu Guia Turístico no CRAJUBAR! 🌟

Estou aqui para tornar sua visita ao CRAJUBAR inesquecível! 🗺️ Explore pontos turísticos deslumbrantes, fique por dentro dos eventos locais, saboreie a culinária nos melhores restaurantes e encontre a hospedagem perfeita em hotéis acolhedores. 🍽️🛌

Para iniciar basta clicar aqui: /cidades   

Caso tenha entrado em alguma opção errada, você pode digitar o comando \n/reiniciar a qualquer momento para reiniciar sua aventura!
''')

    @bot.message_handler(commands=['cidades', 'reiniciar'])
    def credits_message(message):
        bot.send_message(message.chat.id, 'Selecione aqui a cidade que você deseja explorar:\n\n/Crato\n\n/Juazeiro\n\n/Barbalha')

    @bot.message_handler(content_types=['text'])
    def message_reply(message):
        if message.text == '/Crato':
            bot.send_photo(message.chat.id, photo = open('crato.jpg', 'rb'))
        
            texto = ""
            poema = open("textocrato.txt", "r")
            for linha in poema.readlines():
                texto += linha
            poema.close()
            bot.send_message(message.chat.id, texto)

            texto = """
        O que mais te interessa no momento?
        Saber sobre:"""
            
            msg = bot.send_message(message.chat.id, 'Por favor, clique na opção que você irá se aventurar:\n\n/pontos_turisticos\n\n/eventos\n\n/restaurantes\n\n/hospedagens')
            bot.register_next_step_handler(msg, crato)
        
        elif message.text == '/Juazeiro':
            bot.send_photo(message.chat.id, photo = open('jdn.jpg', 'rb'))
        
            texto = ""
            poema = open("textojdn.txt", "r")
            for linha in poema.readlines():
                texto += linha
            poema.close()
            bot.send_message(message.chat.id, texto)

            texto = """
        O que mais te interessa no momento?
        Saber sobre:"""
            
            msg = bot.send_message(message.chat.id, 'Por favor, clique na opção que você irá se aventurar:\n\n/pontos_turisticos\n\n/eventos\n\n/restaurantes\n\n/hospedagens')
            bot.register_next_step_handler(msg, juazeiro)
        
        elif message.text == '/Barbalha':
            bot.send_photo(message.chat.id, photo = open('barbalha.jpg', 'rb'))
        
            texto = ""
            poema = open("textobarbalha.txt", "r")
            for linha in poema.readlines():
                texto += linha
            poema.close()
            bot.send_message(message.chat.id, texto)

            texto = """
        O que mais te interessa no momento?
        Saber sobre:"""
            msg = bot.send_message(message.chat.id, 'Por favor, clique na opção que você irá se aventurar:\n\n/pontos_turisticos\n\n/eventos\n\n/restaurantes\n\n/hospedagens')
            bot.register_next_step_handler(msg, barbalha)
        
    def crato(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msg = message.text.split()
        if msg[0] == '/pontos_turisticos':
            cursor.execute(f"SELECT nome FROM pontos_turisticos WHERE cidade LIKE '%Crato%'")
            pontos_turisticos = cursor.fetchall()
            nomes = [e[0] for e in pontos_turisticos]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            mensag = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(mensag, pontos_turisticos_crato)
        elif msg[0] == '/eventos':
            cursor.execute(f"SELECT titulo FROM eventos WHERE cidade LIKE '%Crato%'")
            eventos = cursor.fetchall()
            titulos = [e[0] for e in eventos]
            mensagem = "\n\n".join([f"/{i+1} {titulo}" for i, titulo in enumerate(titulos)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, eventos_crato)
        elif msg[0] == '/restaurantes':
            cursor.execute(f"SELECT nome FROM restaurantes WHERE cidade LIKE '%Crato%'")
            restaurantes = cursor.fetchall()
            nomes = [e[0] for e in restaurantes]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, restaurantes_crato)
        elif msg[0] == '/hospedagens':
            cursor.execute(f"SELECT nome FROM hospedagens WHERE cidade LIKE '%Crato%'")
            hospedagens = cursor.fetchall()
            nomes = [e[0] for e in hospedagens]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, hospedagens_crato)
        else:
            bot.send_message(message.chat.id, 'Comando não encontrado! Por favor, reinicie sua pesquisa: /cidades')
        con.close()

    def juazeiro(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msg = message.text.split()
        if msg[0] == '/pontos_turisticos':
            cursor.execute(f"SELECT nome FROM pontos_turisticos WHERE cidade LIKE '%Juazeiro_%'")
            pontos_turisticos = cursor.fetchall()
            nomes = [e[0] for e in pontos_turisticos]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            mensag = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(mensag, pontos_turisticos_juazeiro)
        elif msg[0] == '/eventos':
            cursor.execute(f"SELECT titulo FROM eventos WHERE cidade LIKE '%Juazeiro_%'")
            eventos = cursor.fetchall()
            titulos = [e[0] for e in eventos]
            mensagem = "\n\n".join([f"/{i+1} {titulo}" for i, titulo in enumerate(titulos)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, eventos_juazeiro)
        elif msg[0] == '/restaurantes':
            cursor.execute(f"SELECT nome FROM restaurantes WHERE cidade LIKE '%Juazeiro%'")
            restaurantes = cursor.fetchall()
            nomes = [e[0] for e in restaurantes]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, restaurantes_juazeiro)
        elif msg[0] == '/hospedagens':
            cursor.execute(f"SELECT nome FROM hospedagens WHERE cidade LIKE '%Juazeiro_%'")
            hospedagens = cursor.fetchall()
            nomes = [e[0] for e in hospedagens]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, hospedagens_juazeiro)
        else:
            bot.send_message(message.chat.id, 'Por favor, reinicie sua pesquisa: /cidades')

    def barbalha(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msg = message.text.split()
        
        if msg[0] == '/pontos_turisticos':
            cursor.execute(f"SELECT nome FROM pontos_turisticos WHERE cidade LIKE '%Barbalha%'")
            pontos_turisticos = cursor.fetchall()
            nomes = [e[0] for e in pontos_turisticos]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            mensag = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(mensag, pontos_turisticos_barbalha)

        elif msg[0] == '/eventos':
            cursor.execute(f"SELECT titulo FROM eventos WHERE cidade LIKE '%Barbalha%'")
            eventos = cursor.fetchall()
            titulos = [e[0] for e in eventos]
            mensagem = "\n\n".join([f"/{i+1} {titulo}" for i, titulo in enumerate(titulos)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, eventos_barbalha)

        elif msg[0] == '/restaurantes':
            cursor.execute(f"SELECT nome FROM restaurantes WHERE cidade LIKE '%Barbalha%'")
            restaurantes = cursor.fetchall()
            nomes = [e[0] for e in restaurantes]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, restaurantes_barbalha)

        elif msg[0] == '/hospedagens':
            cursor.execute(f"SELECT nome FROM hospedagens WHERE cidade LIKE '%Barbalha%'")
            hospedagens = cursor.fetchall()
            nomes = [e[0] for e in hospedagens]
            mensagem = "\n\n".join([f"/{i+1} {nome}" for i, nome in enumerate(nomes)])
            bot.send_message(message.chat.id, mensagem)
            msgs = bot.send_message(message.chat.id, "Selecione a opção que desejar!")
            bot.register_next_step_handler(msgs, hospedagens_barbalha)
        else:
            bot.send_message(message.chat.id, 'Por favor, reinicie sua pesquisa: /cidades')


#Funções para puxar informações dos RESTAURANTES
    def restaurantes_crato(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msgs = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, nota, endereco, horariofunc, tipocomida, descricao FROM restaurantes WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, nota, endereco, horariofunc, tipocomida, descricao = resultados
            mensagem = f"Nome: {nome}\nNota: {nota}\nEndereço: {endereco}\nHorário de Funcionamento: {horariofunc}\nTipo de Comida: {tipocomida}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if msgs[0] == "/1":
            puxa_dados(6)
        elif msgs[0] == "/2":
            puxa_dados(7)
        elif msgs[0] == "/3":
            puxa_dados(8)
        elif msgs[0] == "/4":
            puxa_dados(9)
        elif msgs[0] == "/5":
            puxa_dados(10)
    def restaurantes_juazeiro(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msgs = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, nota, endereco, horariofunc, tipocomida, descricao FROM restaurantes WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, nota, endereco, horariofunc, tipocomida, descricao = resultados
            mensagem = f"Nome: {nome}\nNota: {nota}\nEndereço: {endereco}\nHorário de Funcionamento: {horariofunc}\nTipo de Comida: {tipocomida}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if msgs[0] == "/1":
            puxa_dados(1)
        elif msgs[0] == "/2":
            puxa_dados(2)
        elif msgs[0] == "/3":
            puxa_dados(3)
        elif msgs[0] == "/4":
            puxa_dados(4)
        elif msgs[0] == "/5":
            puxa_dados(5)

    def restaurantes_barbalha(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msgs = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, nota, endereco, horariofunc, tipocomida, descricao FROM restaurantes WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, nota, endereco, horariofunc, tipocomida, descricao = resultados
            mensagem = f'''Nome: {nome}\nNota: {nota}\nEndereço: {endereco}\n
            Horário de Funcionamento: {horariofunc}\nTipo de Comida: {tipocomida}\n
            Descrição: {descricao}\n\n/reiniciar para voltar ao inicio'''
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if msgs[0] == "/1":
            puxa_dados(11)
        elif msgs[0] == "/2":
            puxa_dados(12)
        elif msgs[0] == "/3":
            puxa_dados(13)
        elif msgs[0] == "/4":
            puxa_dados(14)
        elif msgs[0] == "/5":
            puxa_dados(15)

#Funções para puxar informações dos PONTOS TURÍSTICOS
    def pontos_turisticos_barbalha(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        mensag = message.text.split()
        def puxa_dados(id):
            cursor.execute(f'''SELECT nome, endereco, categoria, horariofunc, descricao 
            FROM pontos_turisticos WHERE id = ?''', (id,))
            resultados = cursor.fetchone()
            nome, endereco, categoria, horariofunc, descricao = resultados
            mensagem = f'''Nome: {nome}\nEndereço: {endereco}\nCategoria: {categoria}\n
            Horário de Funcionamento: {horariofunc}\n
            Descrição: {descricao}\n\n/reiniciar para voltar ao inicio'''
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if mensag[0] == "/1":
            puxa_dados(16)
        elif mensag[0] == "/2":
            puxa_dados(17)
        elif mensag[0] == "/3":
            puxa_dados(18)
        elif mensag[0] == "/4":
            puxa_dados(19)
        elif mensag[0] == "/5":
            puxa_dados(20)
        elif mensag[0] == "/6":
            puxa_dados(21)
    def pontos_turisticos_crato(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        mensag = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, endereco, categoria, horariofunc, descricao FROM pontos_turisticos WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, endereco, categoria, horariofunc, descricao = resultados
            mensagem = f"Nome: {nome}\nEndereço: {endereco}\nCategoria: {categoria}\nHorário de Funcionamento: {horariofunc}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if mensag[0] == "/1":
            puxa_dados(8)
        elif mensag[0] == "/2":
            puxa_dados(10)
        elif mensag[0] == "/3":
            puxa_dados(11)
        elif mensag[0] == "/4":
            puxa_dados(13)
        elif mensag[0] == "/5":
            puxa_dados(14)
        elif mensag[0] == "/6":
            puxa_dados(15)
    def pontos_turisticos_juazeiro(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        mensag = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, endereco, categoria, horariofunc, descricao FROM pontos_turisticos WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, endereco, categoria, horariofunc, descricao = resultados
            mensagem = f"Nome: {nome}\nEndereço: {endereco}\nCategoria: {categoria}\nHorário de Funcionamento: {horariofunc}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if mensag[0] == "/1":
            puxa_dados(1)
        elif mensag[0] == "/2":
            puxa_dados(2)
        elif mensag[0] == "/3":
            puxa_dados(3)
        elif mensag[0] == "/4":
            puxa_dados(4)
        elif mensag[0] == "/5":
            puxa_dados(5)
        elif mensag[0] == "/6":
            puxa_dados(6)

#Funções para puxar informações dos EVENTOS
#fazer interagir depois de selecionar a opção
    def eventos_crato(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        mensag = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT titulo, tipo, datahorario, custoentrada, endereco, descricao FROM eventos WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            titulo, tipo, datahorario, custoentrada, endereco, descricao = resultados
            mensagem = f"Título: {titulo}\nTipo: {tipo}\nData | Horário: {datahorario}\nIngresso | Entrada: {custoentrada}\nEndereço: {endereco}\nDescrição: {descricao}\n\nGostou? Bom evento!\n\nQuer voltar ao inicio? /reiniciar"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if mensag[0] == "/1":
            puxa_dados(1)
        elif mensag[0] == "/2":
            puxa_dados(2)
        elif mensag[0] == "/3":
            puxa_dados(3)
        elif mensag[0] == "/4":
            puxa_dados(4)
        elif mensag[0] == "/5":
            puxa_dados(5)

    def eventos_juazeiro(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        mensag = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT titulo, tipo, datahorario, custoentrada, endereco, descricao FROM eventos WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            titulo, tipo, datahorario, custoentrada, endereco, descricao = resultados
            mensagem = f"Título: {titulo}\nTipo: {tipo}\nData | Horário: {datahorario}\nIngresso | Entrada: {custoentrada}\nEndereço: {endereco}\nDescrição: {descricao}\n\nGostou? Bom evento!\n\nQuer voltar ao inicio? /reiniciar"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if mensag[0] == "/1":
            puxa_dados(6)
        elif mensag[0] == "/2":
            puxa_dados(7)
        elif mensag[0] == "/3":
            puxa_dados(8)
        elif mensag[0] == "/4":
            puxa_dados(9)
        elif mensag[0] == "/5":
            puxa_dados(10)
        elif mensag[0] == "/6":
            puxa_dados(11)

    def eventos_barbalha(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        mensag = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT titulo, tipo, datahorario, custoentrada, endereco, descricao FROM eventos WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            titulo, tipo, datahorario, custoentrada, endereco, descricao = resultados
            mensagem = f"Título: {titulo}\nTipo: {tipo}\nData | Horário: {datahorario}\nIngresso | Entrada: {custoentrada}\nEndereço: {endereco}\nDescrição: {descricao}\n\nGostou? Bom evento!\n\nQuer voltar ao inicio? /reiniciar"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if mensag[0] == "/1":
            puxa_dados(12)
        elif mensag[0] == "/2":
            puxa_dados(13)
        elif mensag[0] == "/3":
            puxa_dados(14)
        elif mensag[0] == "/4":
            puxa_dados(15)

#Funções para puxar informações dos HOSPEDAGEM
    def hospedagens_crato(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msgs = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, avaliacao, preco, endereco, contato, descricao FROM hospedagens WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, avaliacao, preco, endereco, contato, descricao = resultados
            mensagem = f"Nome: {nome}\nNota: {avaliacao}\nPreço: {preco}\nEndereço: {endereco}\nContato: {contato}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if msgs[0] == "/1":
            puxa_dados(5)
        elif msgs[0] == "/2":
            puxa_dados(6)
        elif msgs[0] == "/3":
            puxa_dados(7)
        elif msgs[0] == "/4":
            puxa_dados(8)
        elif msgs[0] == "/5":
            puxa_dados(9)
        elif msgs[0] == "/6":
            puxa_dados(10)
        elif msgs[0] == "/7":
            puxa_dados(11)
        elif msgs[0] == "/8":
            puxa_dados(12)

    def hospedagens_juazeiro(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msgs = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, avaliacao, preco, endereco, contato, descricao FROM hospedagens WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, avaliacao, preco, endereco, contato, descricao = resultados
            mensagem = f"Nome: {nome}\nNota: {avaliacao}\nPreço: {preco}\nEndereço: {endereco}\nContato: {contato}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if msgs[0] == "/1":
            puxa_dados(13)
        elif msgs[0] == "/2":
            puxa_dados(14)
        elif msgs[0] == "/3":
            puxa_dados(15)
        elif msgs[0] == "/4":
            puxa_dados(16)
        elif msgs[0] == "/5":
            puxa_dados(17)

    def hospedagens_barbalha(message):
        con = sqlite3.connect('bd_principal.sqlite')
        cursor = con.cursor()
        msgs = message.text.split()
        def puxa_dados(id):
            cursor.execute(f"SELECT nome, avaliacao, preco, endereco, contato, descricao FROM hospedagens WHERE id = ?", (id,))
            resultados = cursor.fetchone()
            nome, avaliacao, preco, endereco, contato, descricao = resultados
            mensagem = f"Nome: {nome}\nNota: {avaliacao}\nPreço: {preco}\nEndereço: {endereco}\nContato: {contato}\nDescrição: {descricao}\n\n/reiniciar para voltar ao inicio"
            bot.send_message(message.chat.id, mensagem)
            con.close()
        
        if msgs[0] == "/1":
            puxa_dados(1)
        elif msgs[0] == "/2":
            puxa_dados(2)
        elif msgs[0] == "/3":
            puxa_dados(3)
        elif msgs[0] == "/4":
            puxa_dados(4)
        


    bot.infinity_polling()

if __name__ == "__main__":
    os.system('cls')
    token = '6412842691:AAFT6yXT4ivibQPoeQZ8pYD2yZ0XW3iwBvk'
    main(token)



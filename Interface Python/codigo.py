import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']
    
    texto_cotacoes["text"]= f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}
    '''

# o Tk() é o codigo que cria a janela principal
janela = Tk()
janela.title("Cotação Atual das Moedas") 
janela.geometry("300x200")

texto_orientacao = Label(janela, text="Clique no botão para exibir a cotação das moedas")
texto_orientacao.grid(column=0,row=0,padx=10,pady=10)

botao = Button(janela, text="Buscar Cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1,padx=10,pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0,row=2,padx=10,pady=10)

#ultima linha de codigo, que mantem a janela em execução até a mesma ser fechada
janela.mainloop()
import speedtest
from tkinter import *

def teste_velocidade():
    teste = speedtest.Speedtest()
    teste.get_servers()
    teste.get_best_server()

    #print(f"Velocidade Download: {round(teste.download(threads=None)*(10**-6))}")
    #print(f"Velocidade Upload: {round(teste.upload(threads=None)*(10**-6))}")
    texto_download["text"] = f"Velocidade Download: {round(teste.download(threads=None)*(10**-6))}"
    texto_upload["text"] = f"Velocidade Upload: {round(teste.upload(threads=None)*(10**-6))}"

#Fazendo aqui a tela do programa
mainForm = Tk()
mainForm.title("Teste Rápido de Internet")
mainForm.geometry("300x200")

texto_base = Label(mainForm, text="Clique no botão para realizar o teste:")
texto_base.grid(column=0,row=0,padx=55,pady=10)

botao = Button(mainForm, text="Testar Velocidade", command=teste_velocidade)
botao.grid(column=0,row=1,padx=10,pady=10)

texto_download = Label(mainForm, text="A")
texto_download.grid(column=0,row=2,padx=10,pady=10)

texto_upload = Label(mainForm,text="A")
texto_upload.grid(column=0,row=3,padx=10,pady=10)
#ultima linha de código para manter a tela em execução
mainForm.mainloop()
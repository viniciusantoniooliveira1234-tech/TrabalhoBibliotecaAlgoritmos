import sistema
from tkinter import *

#renderizar antes para não bugar e duplicar o menu
def menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton):
    menuframe.pack()
    mntxt.pack()
    mntxt2.pack()
    cadastrobutton.pack()
    consultabutton.pack()
    alterarbutton.pack()
    removerbutton.pack()
    listarbutton.pack()
    emprestimobutton.pack()
    devolucaobutton.pack()
    sairbutton.pack()
    for i in lista:
        print(i.titulo,i.autor,i.ano,i.codigo,i.status)

def init(lista):
    janela = Tk()
    janela.title("Biblioteca muito legal")
    janela.geometry("720x520")
    menuframe = Frame(janela)
    mntxt = Label(menuframe,text="MENU")
    mntxt2 = Label(menuframe,text="Escolha uma das opções")
    cadastrobutton = Button(menuframe,text="Cadastrar livro",command=lambda:cadastrolivro(lista,menuframe))
    consultabutton = Button(menuframe,text="Consultar livro",command=lambda:consultalivro(lista,menuframe))
    alterarbutton = Button(menuframe,text="Alterar livro")
    removerbutton = Button(menuframe,text="Remover livro")
    listarbutton = Button(menuframe,text="Listar livros")
    emprestimobutton = Button(menuframe,text="Empréstimo de livro")
    devolucaobutton = Button(menuframe,text="Devolver Livro")
    sairbutton = Button(menuframe,text="Sair")

    menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton)

    #renderizar cadastro
    def cadastrolivro(lista,menuframe):
        cadastroframe = Frame(janela)
        menuframe.pack_forget()
        cadastroframe.pack()
        cdtxt= Label(cadastroframe,text="CADASTRAR LIVRO:")
        cdtxt.pack()
        tittxt = Label(cadastroframe,text="Título do Livro:")
        tittxt.pack()
        titentry = Entry(cadastroframe)
        titentry.pack()
        auttxt = Label(cadastroframe,text="Autor do Livro:")
        auttxt.pack()
        autentry = Entry(cadastroframe)
        autentry.pack()
        anotxt = Label(cadastroframe,text="Ano do livro:")
        anotxt.pack()
        anoentry = Entry(cadastroframe)
        anoentry.pack()
        codigotxt = Label(cadastroframe,text="Código do livro")
        codigotxt.pack()
        codigoentry = Entry(cadastroframe)
        codigoentry.pack()
        statustxt = Label(cadastroframe,text="Status do livro(1-Disponível/0-Emprestado)")
        statustxt.pack()
        statusentry = Entry(cadastroframe)
        statusentry.pack()
        salvar = Button(cadastroframe,text="Salvar livro",command=lambda:salvarcadastro(lista,cadastroframe,titentry,autentry,anoentry,codigoentry,statusentry))
        salvar.pack()
    
    #salvar cadastro
    def salvarcadastro(lista,cadastroframe,titentry,autentry,anoentry,codigoentry,statusentry):
        cadastroframe.pack_forget()
        titulo = titentry.get()
        autor = autentry.get()
        ano = anoentry.get()
        codigo = codigoentry.get()
        status = statusentry.get()
        resultados = sistema.cadastrar(lista,titulo,autor,ano,codigo,status)
        if resultados:
            print("Livro cadastrado com sucesso")
        else:
            print("Código do livro duplicado, tente novamente")
        menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton)
    
    #renderizar consulta
    def consultalivro(lista,menuframe):
        menuframe.pack_forget()
        consultaframe = Frame(janela)
        consultaframe.pack()
        constxt = Label(consultaframe,text="Busque os livros pelo código/autor")
        constxt.pack()
        codigotxt = Label(consultaframe,text="Código:")
        codigotxt.pack()
        codigoentry = Entry(consultaframe)
        codigoentry.pack()
        autortxt = Label(consultaframe,text="Autor:")
        autortxt.pack()
        autorentry = Entry(consultaframe)
        autorentry.pack()
        salvarbutton = Button(consultaframe,text="Consultar",command=lambda:consultarlivro(lista,codigoentry,autorentry,consultaframe))
        salvarbutton.pack()
    def consultarlivro(lista,codigoentry,autorentry,consultaframe):
        codigo = codigoentry.get()
        autor = autorentry.get()
        sistema.consultar(lista,autor,codigo)
        consultaframe.pack_forget()
        menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton)
    janela.mainloop()

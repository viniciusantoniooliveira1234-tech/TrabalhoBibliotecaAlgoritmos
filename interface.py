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
    alterarbutton = Button(menuframe,text="Alterar livro", command=lambda:alterarint(lista,menuframe))
    removerbutton = Button(menuframe,text="Remover livro", command=lambda:removerlivroint(lista,menuframe))
    listarbutton = Button(menuframe,text="Listar livros", command=lambda:listarlivrosint(lista))
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
            print("erro, tente novamente")
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
    #encontrar livros
    def consultarlivro(lista,codigoentry,autorentry,consultaframe):
        codigo = codigoentry.get()
        autor = autorentry.get()
        sistema.consultar(lista,autor,codigo)
        consultaframe.pack_forget()
        menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton)

    #interface alterar dados
    def alterarint(lista,menuframe):
        menuframe.pack_forget()
        alterarframe = Frame(janela)
        alterarframe.pack()
        alttxt = Label(alterarframe,text="Alterar dados(Digite o código do livro que deseja alterar)")
        alttxt.pack()
        codigotxt = Label(alterarframe,text="Código do livro:")
        codigotxt.pack()
        codigoentry = Entry(alterarframe)
        codigoentry.pack()
        titulotxt= Label(alterarframe, text="Título para ser alterado:")
        titulotxt.pack()
        tituloentry = Entry(alterarframe)
        tituloentry.pack()
        autortxt = Label(alterarframe,text="Autor para ser alterado:")
        autortxt.pack()
        autorentry = Entry(alterarframe)
        autorentry.pack()
        anotxt = Label(alterarframe,text="Ano para ser alterado:")
        anotxt.pack()
        anoentry = Entry(alterarframe)
        anoentry.pack()
        salvarbutton = Button(alterarframe,text="Salvar alterações",command=lambda:alterardados(lista,codigoentry,tituloentry,autorentry,anoentry,alterarframe))
        salvarbutton.pack()
    #alterar os dados
    def alterardados(lista,codigoentry,tituloentry,autorentry,anoentry,alterarframe):
        alterarframe.pack_forget()
        codigo = codigoentry.get()
        titulo = tituloentry.get()
        autor = autorentry.get()
        ano = anoentry.get()
        resultados = sistema.alterardados(lista,codigo,titulo,autor,ano)
        if resultados:
            print("livro alterado com sucesso")
        else:
            print("Código não encontrado, tente novamente")
        menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton)
    #interface para remover o livro
    def removerlivroint(lista,menuframe):
        menuframe.pack_forget()
        removerlivroframe = Frame(janela)
        removerlivroframe.pack()
        removetxt = Label(removerlivroframe,text="Digite o código do livro que deseja remover:")
        removetxt.pack()
        removeentry = Entry(removerlivroframe)
        removeentry.pack()
        salvarbutton = Button(removerlivroframe,text="Remover livro",command=lambda:removerlivro(lista,removerlivroframe,removeentry))
        salvarbutton.pack()
    #remover o livro
    def removerlivro(lista,removerlivroframe,removeentry):
        removerlivroframe.pack_forget()
        codigo = removeentry.get()
        resultados = sistema.removerlivro(lista,codigo)
        if resultados:
            print("Livro salvo com sucesso")
        else:
            print("Livro não encontrado")
        menuint(menuframe,mntxt,mntxt2,cadastrobutton,lista,consultabutton,alterarbutton,removerbutton,listarbutton,emprestimobutton,devolucaobutton,sairbutton)

    #interface para listar os livros
    def listarlivrosint(lista):
        sistema.listarlivros(lista)
    janela.mainloop()


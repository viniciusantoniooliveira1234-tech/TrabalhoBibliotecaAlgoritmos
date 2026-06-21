from livro import *
#parte lógica do programa

#cadastrar livro
def cadastrar(lista,titulo,autor,ano,codigo,status):
    livro = Livro()
    for i  in lista:
        if i.codigo == codigo:
            return False
    livro.titulo = titulo
    livro.autor = autor
    livro.ano = ano
    livro.codigo = codigo
    #dependendo do numero altera para disponivel ou emprestado
    if status == "1":
        livro.status = "disponivel"
    else:
        if status == "0":
            livro.status = "emprestado"
        else:
            return False
    lista.append(livro)
    return True

def consultar(lista,autor,codigo):
    resultados = []
    #achar o livro
    for i in lista:
        #verificar se o foi usado o codio ou o autor
        if i.autor ==autor and codigo == "":
            resultados.append(i.titulo)
        if i.codigo == codigo and autor == "":
            resultados.append(i.titulo)
    #mostrar livros encontrados(se tiver)
    if len(resultados) > 0:
        print("Livros encontrados:")
        for i in range(len(resultados)):
            print(resultados[i])
    else:
        print("Livro não encontrado")

def alterardados(lista,codigo,titulo,autor,ano):
    #encontrar livro
    for i in lista:
        #checar se o codigo existe e alterar dados
        if i.codigo == codigo:
            i.titulo = titulo
            i.autor = autor
            i.ano = ano
            return True
    return False

def removerlivro(lista,codigo):
    for i in lista:
        #remover livro pelo código se encontrar
        if i.codigo == codigo:
            lista.remove(i)
            return True
    return False
#Listar livros
def listarlivros(lista):
    print("Livros Encontrados:")
    for i in lista:
        print("Título:",i.titulo,"Ano:",i.ano)

#emprestimo e devolucao
def emprestimo(lista,codigo):
    for i in lista:
        if i.codigo == codigo:
            if i.status == "disponivel":
                i.status = "emprestado"
                return True
            if i.status =="emprestado":
                return False
def devolucao(lista,codigo):
    for i in lista:
        if i.codigo == codigo:
            if i.status == "emprestado":
                i.status = "disponivel"
                return True
            if i.status =="disponivel":
                return False
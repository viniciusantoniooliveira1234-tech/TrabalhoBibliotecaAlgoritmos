from livro import *

def cadastrar(lista,titulo,autor,ano,codigo,status):
    livro = Livro()
    for i  in lista:
        if i.codigo == codigo:
            return False
    livro.titulo = titulo
    livro.autor = autor
    livro.ano = ano
    livro.codigo = codigo
    if status == "1":
        livro.status = "Disponivel"
    else:
        if status == "0":
            livro.status = "Emprestado"
        else:
            return False
    lista.append(livro)
    return True

def consultar(lista,autor,codigo):
    resultados = []
    for i in lista:
        if i.autor ==autor and codigo == "":
            resultados.append(i.titulo)
        if i.codigo == codigo and autor == "":
            resultados.append(i.titulo)
    if len(resultados) > 0:
        print("Livros encontrados:")
        for i in range(len(resultados)):
            print(resultados[i])
    else:
        print("Livro não encontrado")

def alterardados(lista,codigo,titulo,autor,ano):
    for i in lista:
        if i.codigo == codigo:
            i.titulo = titulo
            i.autor = autor
            i.ano = ano
            return True
    return False
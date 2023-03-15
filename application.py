from conexaobd import BancoDeDados as bd

listaAlimentos = []
listaHigienePessoal = []
listaLimpeza = []
listaUtilidades= []
listaFolhas= []
listaFrutas= []
listaLegumes= []
listaTemperos= []
listaEscolhasUsuario= []

def buscarProdutosMercado(self, respostaTipoDeLista):
    if respostaTipoDeLista == '1':
        print("------------------------------------------------------- \n Categorias Mercado:")
        buscarMercado = bd.produtosMercado(None)
        for x in buscarMercado:
            if x[0] != 'id':
                print(x[0])
        desejaEscolherMercado = input("\nDeseja começar a escolher os produtos? s/n ")
        selecionarProdutosMercado(None, desejaEscolherMercado)

def selecionarProdutosMercado(self, desejaEscolherMErcado):
    global listaAlimentos
    global listaHigienePessoal
    global listaLimpeza
    global listaUtilidades
    if desejaEscolherMErcado == 's':

        print("\n---------------------------------------------------------\n Categoria Alimentos:")
        buscarCategoriaAlimentos = bd.buscarAlimentos(None)
        contador=0
        for x in buscarCategoriaAlimentos:
            listaAlimentos.append(x[0])
            print(contador, '-', x[0])
            contador +=1
        produtosEscolhidosAlimentos = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula): ")
        produtosEscolhidosAlimentos = produtosEscolhidosAlimentos.split(",")
        for i in range(len(produtosEscolhidosAlimentos)):
            listaEscolhasUsuario.append(listaAlimentos[int(produtosEscolhidosAlimentos[i])])
        listaAlimentos = []

        print("\n--------------------------------------------------------- \n Categoria Higiene Pessoal: ")
        buscarCategoriaHigienePessoal = bd.buscarHigienePessoal(None)
        contador=0
        for x in buscarCategoriaHigienePessoal:
            listaHigienePessoal.append(x[0])
            print (contador, '-', x[0])
            contador+=1
        produtosEscolhidosHigienePessoal = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosHigienePessoal = produtosEscolhidosHigienePessoal.split(",")
        for i in range(len(produtosEscolhidosHigienePessoal)):
            listaEscolhasUsuario.append(listaHigienePessoal[int(produtosEscolhidosHigienePessoal[i])])
        listaHigienePessoal = []

        print("\n---------------------------------------------------------- \n Categoria Limpeza: ")
        buscarCategoriaLimpeza = bd.buscarLimpeza(None)
        contador=0
        for x in buscarCategoriaLimpeza:
            listaLimpeza.append(x[0])
            print(contador, '-', x[0])
            contador +=1
        produtosEscolhidosLimpeza = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosLimpeza =produtosEscolhidosLimpeza.split(",")
        for i in range(len(produtosEscolhidosLimpeza)):
            listaEscolhasUsuario.append(listaLimpeza[int(produtosEscolhidosLimpeza[i])])
        listaLimpeza = []

        print("\n----------------------------------------------------------- \n Categoria Utilidades: ")
        buscarCategoriaUtilidades = bd.buscarUtilidades(None)
        contador=0
        for x in buscarCategoriaUtilidades:
            listaUtilidades.append(x[0])
            if x[0] != None:
                print(contador, '-', x[0])
                contador +=1
        produtosEscolhidosUtilidades = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosUtilidades =produtosEscolhidosUtilidades.split(",")
        for i in range(len(produtosEscolhidosUtilidades)):
            listaEscolhasUsuario.append(listaUtilidades[int(produtosEscolhidosUtilidades[i])])
        listaUtilidades = []

def buscarProdutosFeira(self, respostaTipoDeLista):
    if respostaTipoDeLista == '2':
        print("\n------------------------------------------------------- \n Categorias Feira Livre:")
        buscarFeira = bd.produtosFeiraLivre(None)
        for x in buscarFeira:
            if x[0] != 'id':
                print(x[0])
        desejaEscolherFeira = input("\nDeseja começar a escolher os produtos? s/n ")
        selecionarProdutosFeira(None, desejaEscolherFeira)

def selecionarProdutosFeira(self, desejaEscolherFeira):
    global listaFolhas
    global listaFrutas
    global listaLegumes
    global listaTemperos
    if desejaEscolherFeira == 's':

        print("\n-------------------------------------------------------- \n Categoria Folhas:")
        buscarCategoriaFolhas = bd.buscarFolhas(None)
        contador=0
        for x in buscarCategoriaFolhas:
            listaFolhas.append(x[0])
            print(contador , '-' , x[0])
            contador +=1
        #print("///////",buscarCategoriaFolhas.get_columns())
        produtosEscolhidosFolhas = input ("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosFolhas = produtosEscolhidosFolhas.split(",")
        for i in range(len(produtosEscolhidosFolhas)):
            listaEscolhasUsuario.append(listaFolhas[int(produtosEscolhidosFolhas[i])])
        listaFolhas = []

        print("\n-------------------------------------------------------- \n Categoria Frutas:")
        buscarCategoriaFrutas = bd.buscarFrutas(None)
        contador=0
        for x in buscarCategoriaFrutas:
            listaFrutas.append(x[0])
            print(contador, '-', x[0])
            contador +=1
        produtosEscolhidosFrutas = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosFrutas = produtosEscolhidosFrutas.split(",")
        for i in range (len(produtosEscolhidosFrutas)):
            listaEscolhasUsuario.append(listaFrutas[int(produtosEscolhidosFrutas[i])])
        listaFrutas = []

        print("\n-------------------------------------------------------- \n Categoria Legumes:")
        buscarCategoriaLegumes = bd.buscarLegumes(None)
        contador=0
        for x in buscarCategoriaLegumes:
            listaLegumes.append(x[0])
            print(contador , '-', x[0])
            contador +=1
        produtosEscolhidosLegumes = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosLegumes =produtosEscolhidosLegumes.split(",")
        for i in range (len(produtosEscolhidosLegumes)):
            listaEscolhasUsuario.append(listaLegumes[int(produtosEscolhidosLegumes[i])])
        listaLegumes = []

        print("\n--------------------------------------------------------  \n Categoria Temperos:")
        buscarCategoriaTemperos = bd.buscarTemperos(None)
        contador=0
        for x in buscarCategoriaTemperos:
            listaTemperos.append(x[0])
            print(contador, '-', x[0])
            contador +=1
        produtosEscolhidosTemperos = input("Digite o número correpondente aos produtos que você quer adicionar à lista (separe-os por vírgula):")
        produtosEscolhidosTemperos = produtosEscolhidosTemperos.split(",")
        for i in range (len(produtosEscolhidosTemperos)):
            listaEscolhasUsuario.append(listaTemperos[int(produtosEscolhidosTemperos[i])])
        listaTemperos = []

class MainPage ():
    print("Olá, vamos criar sua lista de compras?")
    respostaTipoDeLista = input("Insira: \n 1 para fazer lista de compras para o mercado. \n 2 para fazer a lista de compras da feira livre.\n Resposta:")
    buscarProdutosMercado(None, respostaTipoDeLista)
    buscarProdutosFeira(None, respostaTipoDeLista)
    print("------------------------------------------------------------------\n",
          "SUA LISTA DE COMPRAS É:")
    for i in listaEscolhasUsuario:
        print(i, end= ", ")
    print("\n---------------------------------------------------------------------")



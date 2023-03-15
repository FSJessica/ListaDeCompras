import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="lista_de_compras"
        )

class BancoDeDados:
    def produtosFeiraLivre(self):
        cursor = mydb.cursor()
        cursor.execute("Show columns from produtosFeiraLivre")
        return cursor

    def buscarFolhas(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct folhas from produtosFeiraLivre")
        return cursor

    def buscarFrutas(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct frutas from produtosFeiraLivre")
        return cursor

    def buscarLegumes(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct legumes from produtosFeiraLivre")
        return cursor

    def buscarTemperos(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct temperos from produtosFeiraLivre")
        return cursor

    def produtosMercado(self):
        cursor = mydb.cursor()
        cursor.execute("Show columns from produtosMercado")
        return cursor

    def buscarAlimentos(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct alimentos from produtosMercado")
        return cursor

    def buscarHigienePessoal(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct higienePessoal from produtosMercado")
        return cursor

    def buscarLimpeza(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct limpeza from produtosMercado")
        return cursor

    def buscarUtilidades(self):
        cursor = mydb.cursor()
        cursor.execute("Select distinct utilidades from produtosMercado")
        return cursor

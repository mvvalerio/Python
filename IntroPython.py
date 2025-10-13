# --Instrução condicional

# idade = int(input("Qual a sua idade ?"))
# 
# if idade < 18:
#     print("És maior de idade")
# elif idade == 18:
#     print("Acabaste de fazer 18 anos")
# else:
#     print("És menor de idade")

# --Laços de repetição

# for i in range(0, 10, 2):
#     print("Repetição", i)
# 
# i = 0
# while i < 10:
#     print("Repetição W", i)
#     i += 2

# --Funções

# def repetir():
#     i = 0
#     while i < 10:
#         print("Repetição", i)
#         i += 1
#     return
# 
# repetir()

# --Função com parâmetros

# def repetirVezes(vezes):
#     i = 0
#     while i < vezes:
#         print("Repetição", i)
#         i += 1
#     return
# 
# repetirVezes(5)

# --Funções com retorno

# def somar(a, b):
#     return a + b
# 
# resultado = somar(5, 3)
# print("Resultado =",resultado)

# --Livrarias 

# import math
# 
# raiz = math.sqrt(16)
# print("Raiz quadrada de 16 é:", raiz)
# potencia = math.pow(2,3)
# print("2 elevado a 3 é:", potencia)

# """
# Comentário de múltiplas linhas
# """

# --Experimentos

# y = int(5)
# y:int = 5

# Fruta = ["Banana", "Maca", "Laranja", "Uva", "Maracuja"]
# for i in Fruta:
#     print(i)

# idade = 18
# anoNascimento = 2007
# 
# txt = f"Eu tenho {idade} anos e nasci em {anoNascimento}."
# print(txt)

# --Listas

# frutas = ["maçã", "banana", "laranja"] para uso de dificuldade dificil
# frutas2 = frutas.copy()
# frutasN = []
# 
# for i in frutas:
#     if "n" in i:
#         frutasN.append(i)
# 
# print(frutasN)

# carros = ("BWM", "Audi", "Mercedes")  para uso de dificuldade moderada
# (marca1, marca2, marca3) = carros
# print (marca1)

# for carro in carros:
#     print(carro)

# ----------------

# mySet = {"maçã", "banana", "laranja"} para uso de dificuldade facilitada
# 
# for set in mySet:
#     print(set)

# ----------------

# thisDict = {
#     "brand": "Ford",
#     "model": "Mustang",
#     "year": 1964
# }
# 
# for key in thisDict:
#     print(thisDict[key]) # thisDict[key] - mostra o valor || key - mostra a chave

# Lmbda

# x = lambda a : a + 10
# print(x(5))

# class Carro:
#     def __init__(self, marca, modelo): # init e o construtor da classe
#         self.marca = marca  # atributos
#         self.modelo = modelo
#         print("O construtor foi inicializado")
# 
#     def mostraMarca(self): # obrigatório passar o self, métodos
#         print(self.marca)
# 
#     def mostraModelo(self):
#         print(self.modelo)
# 
# c1 = Carro("Ford", "Mustang")
# 
# c1.mostraMarca()
# c1.mostraModelo()

class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def printname(self):
        print(self.fname, self.lname)

class Student(Person):
    pass # passa os atributos e metodos que não foram usados
    def __init__(self, fname, lname, password):
        super().__init__(self, fname, lname) # super() vai buscar os metodos e atributos da classe superior
        self.password = password
        self.graduationyear = 2019

x = Student("Mike", "Miguel", "123456789")
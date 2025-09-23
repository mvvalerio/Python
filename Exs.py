# List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(List[11:16])

# -------------

# elemento = ""
#
# while elemento != "q":
#     elemento:str = input("Escreva uma letra: ") 
#     List.append(elemento)
# 
# print(List)

# -------------

# def fibonacci_recursivo(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)
# 
# n = int(input("Quantidade de vezes que quer repetir: "))
# print(f"Fibonacci({n}) = {fibonacci_recursivo(n)}")

# -------------

# list = ["maçã", "banana", "laranja"]
# 
# for i in list:
#     if i == "banana":
#         break 

# -------------

# x = lambda a : a*a*a

# a = 5
# x = a*a*a

# x = lambda : [print(i) for i in range(11)]
# x()

dict = {
    "carro" : "Citroen",
    "modelo" : "c3",
    "ano" : 2010
}

print(dict)
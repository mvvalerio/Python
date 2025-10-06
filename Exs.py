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

# dict = {
#     "carro" : "Citroen",
#     "modelo" : "c3",
#     "ano" : 2010
# }
# 
# print(dict)

# myTupl = (1,2,3,4)
# def funTupl(myTupl):
#     (a,b,c,d) = myTupl
# 
#     print(a,b,c,d)
# 
# funTupl(myTupl)

# list:int = [1,2,3,4,5]
# def funLi(list):
#     return print(sum(list))
# 
# funLi(list)

# dicti = {
#     "marca": "Ford",
#     "modelo": "Focus",
#     "ano": "2008"
# }
# 
# for key in dicti:
#     print(f"{key} : {dicti[key]}")

# set1:int = {1,2,3,4,5}
# set2:int = {6,7,8,9,10}
# 
# def setFun(set1, set2):
#     return print(set1.union(set2))
# 
# setFun(set1, set2)

# list = [[1,2,3],
#         [4,5,6],
#         [7,8,9]]
# x = 0
# 
# 
# def funLi(list):
#     for x in list:
#         for y in x:
#             print(f"{y:3}", end="")        
# 
# funLi(list) -- To Be Continued

# mySet1 = {1,2,3,4,5}
# mySet2 = set()
# 
# def funSet(mySet1):
#     mySet2.update(mySet1)
#     mySet1.clear()
#     print(mySet2)
# 
# funSet(mySet1)
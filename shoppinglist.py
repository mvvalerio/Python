Compras = ["sumo", "cereais", "carne"]
print(Compras)

tamanho = 1
tamanhoD = int(input("Quantos produtos deseja adicionar: "))

while tamanho <= tamanhoD:
    produto = (input("Adiciona um produto novo à lista: "))
    Compras.append(produto)
    tamanho += 1

txt = f"A tua lista de compras tem {len(Compras)} produtos: "
print(txt)

itens =", ".join(Compras)
print(itens)
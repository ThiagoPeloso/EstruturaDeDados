
# cardapio = {
# "mussarela": 44.99,
# "pepperoni": 49.99,
# "calabresa": 49.99,
# "portuguesa": 54.99,
# "frango com catupiry": 54.99,
# }

# escolhas = []
# print("Bem vindo a Pizzaria Sabores!")
# while True:
#     pedido = input("Escolha um sabor ou digite 'sair' para sair:")
#     if pedido.lower() == "sair":
#         break
#     elif pedido.lower() in cardapio:
#         escolhas.append(pedido)
#         print(f"Pizza de {pedido} adicionada.")
#
# total = 0
# for pedido in escolhas:
#     total += cardapio[pedido]
#
# print("Resumo da Ópera:")
# if pedido:
#     x = 1
#     for pedido in escolhas:
#         print(f"{x}. {pedido}: R$ {cardapio[pedido]:.2f}")
#         x+=1
#     print(f"Total a pagar: R${total:.2f}")
def exibir_cardapio():
    cardapio = {
        "mussarela": 44.99,
        "pepperoni": 49.99,
        "calabresa": 49.99,
        "portuguesa": 54.99,
        "frango com catupiry": 54.99,
    }
    for pizza, preço in cardapio.items():
        print(f"Sabor: {pizza} | Preço: {preço:.2f}R$")

exibir_cardapio()
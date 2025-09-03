def fazer_pedido():
    cardapio = {
        "mussarela": 44.99,
        "pepperoni": 49.99,
        "calabresa": 49.99,
        "portuguesa": 54.99,
        "frango com catupiry": 54.99,
    }

    escolhas = []
    print("Bem vindo a Pizzaria Sabores!")
    while True:
        pedido = input("Escolha um sabor ou digite 'sair' para sair:")
        if pedido.lower() == "sair":
            break
        elif pedido.lower() in cardapio:
            escolhas.append(pedido)
            print(f"Pizza de {pedido} adicionada.")
    total = 0
    for sabor in pedido:
        total += cardapio[escolhas]

fazer_pedido()

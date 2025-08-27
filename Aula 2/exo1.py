def fazer_pedido():
    sabores = ["mussarela","pepperoni","quatro queijos","calabresa","frango com catupiry","chocolate","romeu e julieta"]
    saboresEscolhidos = []
    pedido = input("Escolha um sabor ou digite 'sair' para sair:")
    pedido = pedido.lower()
    while pedido != "sair":
        if pedido in sabores:
            saboresEscolhidos.append(pedido)
            print(f"Pizza de {pedido} adicionada.")
        else:
            print("Tente outra vez.")
        pedido = input("Escolha um sabor ou digite 'sair' para sair:")
    print("Pedido finalizado.")
    print(f"Seus sabores são:{saboresEscolhidos}")

fazer_pedido()
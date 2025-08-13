def fazer_pedido():
    sabores = ["Mussarela","Pepperoni","Quatro Queijos","Calabresa","Frango com Catupiry","Chocolate","Romeu e Julieta"]
    saboresEscolhidos = []
    pedido = input("Escolha um sabor ou digite 'sair' para sair:")
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
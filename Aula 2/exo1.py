def fazer_pedido():
    x = 0
    sabores = ["Mussarela","Pepperoni","Quatro Queijos","Calabresa","Frango com Catupiry","Chocolate","Romeu e Julieta"]
    saboresEscolhidos = []
    pedido = input("Escolha um sabor ou digite 'sair' para sair:")
    while pedido != "sair":
        if pedido in sabores:
            saboresEscolhidos.append(pedido)
            print(f"Pizza de {pedido} adicionada.")
        else:
            print("erro")
        pedido = input("Escolha um sabor ou digite 'sair' para sair:")
    print("vc saiu :P")
    print(f"Seus sabores são:{saboresEscolhidos}")

fazer_pedido()
def att1():
    nome = input("Digite seu nome:")
    idade = int(input("Digite sua idade:"))
    print(f"Olá {nome}, você tem {idade} anos")
#att1()

def att2():
    idade = int(input("Digite sua idade:"))
    if (idade >= 18):
        print("Você é maior de idade")
    else:
        print("Você é menor de idade")
#att2()

def att3():
    nums = [1, 2, 3, 4, 5]
    soma = int(0)
    for n in nums:
        soma += n
        print(n)
    print (f"Soma final: {soma}")
#att3()

def att4():
    nums = [1,2,3,4,5,6,7,8,9,10]
    resultado = []
    for n in nums:
        if (n % 2 ==0):
            resultado.append(n)
    print(resultado)
#att4()

def att5():
    nums = [1,2,3,4,5,6,7,8,9,10]
    resultado = [n for n in nums if n % 2 == 0]
    print(resultado)

#att5()

def att6():
    user = {
        "nome": input("Digite seu nome:"),
        "idade": int(input("Digite sua idade:")),
        "linguagem": input("Digite sua linguagem favorita:")
    }
    print(f"Olá {user['nome']}, você tem {user['idade']} anos e sua linguagem favorita é {user['linguagem']}")
#att6()

def att7():
    produto = {
        "nome" : "Notebook",
        "preco" : 4500,
        "estoque" : 3
    }
    for (x, y) in produto.items():
        print(f"{x}: {y}")
#att7()

def att8():
    produto = {
        "nome" : "Notebook",
        "preco" : 4500,
        "estoque" : 3
    }
    print(f"Produto: {produto['nome']}, Estoque: {produto['estoque']}")
    def comprar(produto, quantidade):
        produto['estoque'] -= quantidade
    quant = int(input("Digite a quantidade que deseja comprar:"))
    if (quant > produto['estoque']):
        print("Quantidade indisponível")
    else:comprar(produto, quant)
    print(f"Produto: {produto['nome']}, Estoque: {produto['estoque']}")
#att8()

def att9():
    produtos = [
        {"nome": "Notebook", "preco": 4500, "estoque": 3},
        {"nome": "Smartphone", "preco": 2500, "estoque": 5},
        {"nome": "Tablet", "preco": 1500, "estoque": 2}
    ]

    def Fprint (produtos):
        for i, produto in enumerate(produtos):
            print(f" {i} - {produto['nome']} (estoque: {produto['estoque']}) ")

    Fprint(produtos)
    
    pedido = int(input("Digite o número do produto que deseja comprar:"))
    if (pedido >= len(produtos) or pedido < 0):
        print("Produto inválido")
        return
    quant = int(input("Digite a quantidade que deseja comprar:"))
    for produto in produtos:
        if (produtos.index(produto) == pedido):
            print(f"Compra do produto: {produto['nome']} realizada!")
            if (quant > produto['estoque']):
                print("Quantidade indisponível")
            else:
                produto['estoque'] -= quant
    Fprint(produtos)
        

#att9()

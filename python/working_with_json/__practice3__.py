import json

def att1():
    with open("jsons/user.json", "r") as f:
        user_data = json.load(f)
    print(user_data)
    print(user_data["nome"])
#att1()

def att2():
    
    user = {
        "nome" : "Alec",
        "idade" : 19,
        "cidade" : "Santa Cruz do Sul"
    }
    with open("jsons/user2.json", "w") as f:
        json.dump(user,f, indent=4)
#att2()

def att3():
    user = []
    with open("jsons/user.json", "r") as f:
        user.append(json.load(f))
    with open("jsons/user2.json", "r") as f:
        user.append(json.load(f))
    with open("jsons/users.json", "w") as f:
        json.dump(user, f, indent=4)
        
#att3()

def att4():
    with open("jsons/produto.json", "r") as f:
        produto_data = json.load(f)
    print(f"Produto: {produto_data['Nome']}")
    print(f"Preço: R${produto_data['preco']}")
#att4()

def att5():
    found = False
    with open("jsons/produto.json", "r") as f:
        produto_data = json.load(f)
    for produto in produto_data:
        print(f"Produto ID: {produto['id']}")
        print(f"Produto: {produto['Nome']}")
        print(f"Preço: R${produto['preco']}")
        print("-----")
    pedido = int(input("Digite o ID do produto que deseja comprar: "))
    for produto in produto_data:
        if produto['id'] == pedido:
            found = True
            quantidade = int(input("Digite a quantidade desejada: "))
            if quantidade > produto['estoque']:
                print("Sem estoque suficiente!")
                break
            else:
                total = produto['preco'] * quantidade
                print(f"Total a pagar: R${total}")
                produto['estoque'] = produto['estoque'] - quantidade

    if found == False:
        print("Não achamos esse produto :C")


    with open("jsons/produto.json", "w") as f:
        json.dump(produto_data, f, indent=4)  
#att5()
        
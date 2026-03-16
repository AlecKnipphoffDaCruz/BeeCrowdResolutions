import pandas as pd
import matplotlib.pyplot as plt

def att1():
    data = {
    "nome": ["Ana", "Carlos", "Maria"],
    "idade": [20, 25, 22],
    "cidade": ["SP", "RJ", "RS"]
}

    df = pd.DataFrame(data)

    print(df)
    print("----------------")
    print(df.head())
    print("----------------")
    print(df.tail())
    print("----------------")
    print(df.info())
    print("----------------")
    print(df.describe())
    print("----------------")
    print(df["nome"])
    print("----------------")
    print(df[df["idade"] > 21])
#att1()

def att2():
    idades = [20, 25, 22]
    
    plt.plot(idades)

    plt.title("Idades")
    
    plt.show()
#att2()

def att3():
    data = {
    "nome": ["Ana", "Carlos", "Maria"],
    "idade": [20, 25, 22],
    "cidade": ["SP", "RJ", "RS"]
}
    df = pd.DataFrame(data)
    plt.title("Idades do csv")
    df["idade"].plot()
    df.plot(x="nome", y="idade", kind="bar")
    plt.show()
#att3()
 
def att4():
    data = {
        "produto" : ["Notebook", "Mouse", "Teclado"],
        "vendas" : [50, 150, 100]
    }   
    df = pd.DataFrame(data)
    df.plot(x="produto", y="vendas", kind="bar")
    plt.title("Produto x Vendas")
    plt.show()
#att4()
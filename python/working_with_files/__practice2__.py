def escrever_arquivo(): 
    with open("files/arq.txt", "r") as arquivo:
        for linha in arquivo:
            print(linha.strip())
#escrever_arquivo()

def armazenar_dados():
    dados = []
    with open("files/arq.txt", "r") as arquivo:
        for linha in arquivo:
            dados.append(int(linha.strip()))

    print(dados)
#armazenar_dados()

def calcular_media():
    notas = []
    with open("files/notas.txt", "r") as arquivo:
        for linha in arquivo:
            notas.append(float(linha.strip()))
    media = sum(notas) /len(notas)
    print(notas)
    print(f" Média: {media}")

#calcular_media()

def calcular_media2():
    with open ("files/notas.txt", "r") as arquivo:
        notas = [float(linha.strip())for linha in arquivo]
    media = sum(notas) / len(notas)
    print(f" Média: {media}")
#calcular_media2()

def listComprehension():
    nomes = ["Alice", "Bob", "Charlie", "David", "Eve"]
    nome_upper = [nome.upper() for nome in nomes if nome.upper().startswith(("A" , "E"))]
    print(nome_upper)
#listComprehension()

def att1():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    nm = [ n ** 3 for n in numeros if n % 2 != 0]
    print(nm)
#att1()

def att2():
    nomes = ["ana", "joao", "maria", "carlos"]
    nm = [nome.capitalize() for nome in nomes]
    print(nm)
#att2()

def att3():
    nums = [10,15,20,25,30]
    metade_nums = list(map(lambda x: x / 2, nums))
    
    print(metade_nums)
    
#att3()

def att4():
    nums = [2,4,6,8]  
    nm = list(map(lambda x: x ** 2, nums))
    print(nm)
att4()
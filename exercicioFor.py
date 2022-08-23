def exe1():
  for i in range(1, 101):
      print(i)
      
def exe2():
  valorA = int(input("Digite um número: "))
  valorB = int(input("Digite outro número: "))
  incremento = 1 if valorA < valorB else -1
  for i in range(valorA, valorB, incremento):
    print(i)

def exe3(): 
  num = int(input("digite um número: "))
  for i in range(1, 11):
    print((i*num))
    
def exe4():
  vogais = ["a", "e","i", "o", "u"]
  num = 0
  for letra in input("Digite um frase: "):
    if vogais.__contains__(letra):
      num += 1
  print(num)

def exe5():
  quant = int(input("Digite uma quantidade de produtos: "))
  produtos = []
  for produto in range(0, quant):
    produto = input("Digite o produto: ")
    produtos.append(produto)
  print(produtos)
  
def exe6():
  solteiras = []
  casadas = []
  divorciadas = []
  viuvas = []

  for nome in range(0, 20):
    nome = input("Qual o seu nome? ")
    estado = input("Qual o seu estado civil?")
    if estado == "solteira":
        solteiras.append(nome)
    elif estado == "casada":
        casadas.append(nome)
    elif estado == "divorciada":
        divorciadas.append(nome)
    elif estado == "viuva":
        viuvas.append(nome)
  print("Solteiras: ", solteiras, "Casadas: ", casadas, "Divorciadas: ", divorciadas, "Viuvas: ",viuvas)

def exe7():
  sucesso = False
  for senha in range(0, 6):
    senha = input("Digite sua senha: ")
    if len(senha) >= 5 and len(senha) <= 10 and senha.isdigit:
        print("Senha válida!")
        sucesso = True
        break
    else:
        print("Tente novamente.")
  if sucesso == False:
    print("Falha!")

def exe8():
  joioETrigo = ["joio", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "trigo", "joio", "joio", "joio", "joio", "joio", "joio", "joio", "trigo", "trigo", "trigo", "joio", "trigo", "joio", "joio", "joio"]
  joio = []
  trigo = []
  for item in joioETrigo:
    if item == "joio":
        joio.append(item)
    elif item == "trigo":
        trigo.append(item)
  print(joio, trigo)

def exe9A():
  for nome in range(0, 13):
    input("Digite um nome: ")

    def exe9B():
    for num in range(1, 1001):
        print(num)

def exe9C():
    for num in range(1, 2001):
        print(num)   
  
def exe9D():
    for num in range(1000, 0, -1):
        print(num)

def exe9E():
    numGremio = 0
    for time in range(0, 10):
        time = input("Qual o seu time? ")
        if time == "gremio":
            numGremio += 1
    print(numGremio)

def exe9F():
    num = []
    for numero in range(0, 20):
        num.append(float(input("Digite um ponto flutuante: ")))
    print(num)

def exe9G():
    num = 0
    for i in range(0, 10):
        num += int(input("Digite um número: "))
    print(num)

def exe9H():
    quant = int(input("Quantos numeros deseja digitar? "))
    i = 0
    for vez in range(0, quant):
        numero = int(input("Digite um numero: "))
        if numero < 0: 
            print("Número negativo")
        elif numero == 0:
            print("O número é 0")
        else:
            print("Número positivo")
        quant -= 1
def exe9I():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    incrementador = 1 if num1 < num2 else -1
    for num in range(num1, num2, incrementador):
        if num % 2 == 0:
            print(num)

def exe9J():
    numero = 0
    for num in range(1, 199):
        numero += num
    print(numero)

def exe9K():
    num1 = int(input("Digite um valor: "))
    num2 = int(input("Digite outro valor: "))
    impar = 0
    par = 0
    incrementador = 1 if num1 < num2 else -1
    for num in range(num1, num2, incrementador):
        if num % 2 == 0:
            par += num
        else:
            impar += num
    print("Impar: ", impar)
    print("Par: ", par)


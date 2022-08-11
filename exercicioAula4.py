# Exercício 1. 
def exe1():
  preco = float(input("Informe um valor: "))
  qtd = int(input("informe a quantidade: "))
  if preco < 0 or qtd < 0:
    print("Erro")
  else:
    print("Valor compra R$ %.2f" % (preco*qtd))

# Exercício 2

def exe2():
  preco = float(input("Informe um valor: "))
  qtd = int(input("informe a quantidade: "))
  if preco < 0 or qtd < 0:
    print("Erro")
  elif qtd >= 3 and qtd <= 4:
    preco -= preco*0.1
  elif qtd >= 5 and qtd <= 10:
    preco -= preco*0.15
  elif qtd > 10:
    preco -= preco*0.2
  print("Valor compra R$ %.2f" % (preco*qtd))

# Exercício 3
def exe3():
  senha = (input("Digite seu nome: ") + "9876")

  resposta = input("Digite sua senha: ")

  if resposta == senha:
    print("Login foi realizado com sucesso.")
  else: 
    print("Erro")

# Exercício 4

def exe4():
  nome = input("Informe seu nome: ")
  altura = float(input("Informe sua altura: "))
  peso = float(input("Digite seu peso: "))

  imc = (peso/(altura**2))

  if imc < 18.5:
    print(nome, "abaixo do peso")
  elif imc >= 18.5 and imc <= 24.9:
    print(nome, "peso normal")
  elif imc > 24.9 and imc <= 29.9:
    print(nome, "pré-obeso")
  elif imc >= 30.0 and imc <= 34.9:
    print(nome, "obeso grau 1")
  elif imc >= 35.0 and imc <= 39.9:
    print(nome, "obeso grau 2")
  elif imc >= 40:
    print("Obesidade grau 3")
  else:
    print("Erro")

# Exercício 5

  def exe5():
    a = int(input("Digite um número inteiro: "))
    b = int(input("Digite um número inteiro: "))
    c = int(input("Digite um número inteiro: "))

    moduloBmenosC = b - c
    if moduloBmenosC < 0:
      moduloBmenosC *= -1
    moduloAmenosB = a - b
    if moduloAmenosB < 0:
      moduloAmenosB *= -1
    moduloAmenosC = a - c
    if moduloAmenosC < 0:
      moduloAmenosC *= -1

    if (moduloBmenosC < a and a < (b+c)) and ((moduloAmenosC < b) and b < (a+c)) and ((moduloAmenosB <c) and c < (a+b)) == True:
      if a == b == c:
        print("TRIÂNGULO EQUILÁTERO")
      elif a == b or a == c or b == c:
        print("TRIÂNGULO ISÓSCELES")
      else:
        print("TRIÂNGULO ESCALENO")
    else:
      print("NÃO FORMA UM TRIÂNGULO")

# Exercício 6

def exe6():
  jogadorA = input("Escolha par ou ímpar: ")

  if jogadorA == "impar":
    jogadorB = "par"
  else:
    jogadorB = "impar"

  a = int(input("Jogador A informe um número: "))
  b = int(input("Jogador B informe um número: "))

  if ((a+b) % 2 == 0 and jogadorA == "par") or((a+b) % 2 != 0 and jogadorB == "par"): 
    print("Jogador A venceu")
  else: 
    print("Jogador B venceu")

# Exercício 7 
def exe7():
  ano = int(input("Informe o ano: "))
  if ano >= 0 and ano <= 2022:
    mes = int(input("Informe o mes: "))
    if mes >= 1 and mes <= 12:
      dia = int(input("Digite um dia: "))
      if (dia >= 1 and dia <= 31) and ((mes%2 == 0 and dia == 31 and mes <=5) or not(mes==2 and dia > 28)) or not(mes%2 != 0 and dia == 31 and mes >=6):
        if (ano%4==0 and ano%100!=0) or (ano%400==0):
          print('Bissexto')
        else:
          print('Não é bissexto')
      else:
        print("Erro")
    else:
      print("Erro")
  else:
    print("Erro")

# Exercício 8
  def exe8():
    saldo = float(input("Digite o saldo: "))
    operacao = int(input("Realizar Saque: (1)\nRealizar Depósito: (2)\n"))
    valor = float(input("Digite o valor da operação: "))
    if (operacao == 1 and valor > 300.00) or valor > saldo:
      input("Operação inválida")
    elif operacao == 1:
      saldo -= valor
      print("Operação Válida\nSaldo", saldo)
    elif operacao == 2:
      saldo += valor
      print("Operação Válida\nSaldo", saldo)

 # Exercício 9
    def exe9():
      nomeA = input("Digite seu nome: ")
      nomeB = input("Digite seu nome: ")
      escolhaA = input(nomeA+" escolha entre: Pedra, papel, tesoura, lagarto, Spock: ")
      escolhaB = input(nomeB+" escolha entre: Pedra, papel, tesoura, lagarto, Spock: ")
      if escolhaA == escolhaB:
        print("Empate!")
      else:
        if escolhaA == "pedra":
          if escolhaB == "papel" or escolhaB == "spock":
            print(nomeB+" venceu!")
          else:
            print(nomeA+" venceu!")
        elif escolhaA == "papel":
          if escolhaB == "tesoura" or escolhaB == "lagarto":
            print(nomeB+" venceu!")
          else:
            print(nomeA+" venceu!")
        elif escolhaA == "tesoura":
          if escolhaB == "pedra" or escolhaB == "spock":
            print(nomeB+" venceu!")
          else:
            print(nomeA+" venceu!")
        elif escolhaA == "spock":
          if escolhaB == "lagarto" or escolhaB == "papel":
            print(nomeB+" venceu!")
          else:
            print(nomeA+" venceu!")
        elif escolhaA == "lagarto":
          if escolhaB == "pedra" or escolhaB == "tesoura":
            print(nomeB+" venceu!")
          else:
            print(nomeA+" venceu!")

# Exercício 10
def exe10():
  idade = int(input("Qual a sua idade: "))

  if idade < 18:
    print("Você não pode tirar a carteira!")
  else:
    acertos = 0
    if input("1  – Ao prestar socorro à vítima de um acidente, NÃO se deve:\na) acionar imediatamente o Corpo de Bombeiros\nb) dar água, comida ou qualquer substância para a vítima cheirar\nc) conversar com a vítima para saber de suas condições gerais\nd) deixar a vítima confortável até a chegada do socorro especializado\n") == "b":
      acertos += 1
    if input("2 – Ao se deparar com uma sinaleira na cor vermelha, você deve:\na) rir dela\nb) passar mais rápido, pois é perigoso parar\nc) dobrar a direita, pois vermelho indica direita\nd) parar\n") == "d":
      acertos += 1 
    if input("3 – Segundo a direção defensiva, quando você está em uma via e um pedestre vai atravessar você:\na) buzina muito forte para que o pedestre se assuste\nb) atropela o pedestre, pois lugar de pedestre é na calçada\nc) para e dá uma carona para o pedestre, pois é uma lei de trânsito\nd) para e aguarda ele atravessar\n") == "d":
      acertos += 1
    if acertos >= 2:
      print("Você esta apto")
    else:
      print("Você esta inapto")
  










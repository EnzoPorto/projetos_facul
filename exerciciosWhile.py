def exe1():
  i = 0 
  while i < 13:
    input("Qual o seu nome?\n")
    i += 1
    
def exe2():
  i = 0
  while i <= 1000:
    print(i)
    i += 1

def exe3():
  i = 0
  while i <= 2000:
    if i % 2 == 0:
    print(i)
    i += 1
  
def exe4():
  i = 1000
  while i >= 0:
    print(i)
    i -= 1

def exe5():
  i = 0
  gremio = 0
  while i < 10:
    if input("Qual o seu time?\n") == "Gremio":
      gremio += 1
    i += 1
  print("Gremio tem", gremio, "torcedores")
  
def exe6():
  numeros = ""
  i = 0
  while i < 20:
      numeros += str(float(input("Digite 20 números com ponto flutuante: "))) + ", "
      i += 1
  print(numeros)
  
def exe7(): 
  i = 0
  numero = 0
  while i < 10:
    numero += int(input("Digite um número: "))
    i += 1
  print(numero)
  
def exe8():
  quant = int(input("Quantos numeros deseja digitar? "))
  i = 0
  while quant > 0:
    numero = int(input("Digite um numero: "))
    if numero < 0: 
      print("Número negativo")
    elif numero == 0:
      print("O número é 0")
    else:
      print("Número positivo")
    quant -= 1
    
def exe9():
  num1 = int(input("Digite o primeiro valor: "))
  num2 = int(input("Digite o segundo valor: "))
  if num1 >= 0 and num2 >=0:
    if num1 < num2:
      while num1 < num2:
        if num1 % 2 == 0:
          print(num1)
        num1 += 1
    if num2 < num1:
      while num2 < num1:
        if num2 % 2 == 0:
          print(num2)
        num2 +=1

def exe10():
  i = 0
  numero = 0
  while i <= 198:
    numero += i
    i += 1
  print(numero)
    
def exe11():
  num1 = int(input("Digite um valor: "))
  num2 = int(input("Digite outro valor: "))
  impar = 0
  par = 0
  if num1 < num2:
    while num1 <= num2:
      if num1 % 2 == 0:
        par += num1
      else:
        impar += num1
      num1 += 1
  elif num2 <= num1:
    while num2 < num1:
      if num2 % 2 == 0:
        par += num2
      else:
        impar += num2
      num2 += 1
  print("Impar: ", impar)
  print("Par: ", par)

def exe12():
  numero = 0
  i = 1 
  while True:
    res = int(input("Digite um número: "))
    if  res >= 0:
      numero += res
      i += 1
    else:
      i += 1
      numero = float(numero/i)
      break
  print(numero)

def exe13(): 
  numero = int(input("Digite um numero: "))
  fatorial = 1
  while numero != 0:
    fatorial *= numero
    numero -= 1
  print(fatorial)

def exe14():
  while True: 
  num = int(input("Digite um número: "))
  if (num == 1 or num % 2 == 0 or num % 3 == 0 or num%4 == 0 or num%5 == 0 or num%7 == 0 or num%11 == 0) and (num != 1 and num != 2 and num != 3 and num != 5 and num != 7 and num != 11):
    print("Número não é primo")
  else:
    print("Número é primo")
    
def exe15():
  num = 0
  soma = 0
  while num <= 200: 
    if not((num == 1 or num % 2 == 0 or num % 3 == 0 or num%4 == 0 or num%5 == 0 or num%7 == 0 or num%11 == 0) and (num != 2 and num != 3 and num != 5 and num != 7 and num != 11)):
      soma += num
    num += 1
  print(soma)
    
    
    
    
    
    

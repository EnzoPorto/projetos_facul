a = float(input("Digite o valor A: "))
b = float(input("Digite o valor B: "))
c = float(input("Digite o valor C: "))

delta = ((b**2)-(4*a*c))**(1/2)
bhaskaraPositiva = (-b+(delta))/(2*a)
bhaskaraNegativa = (-b-(delta))/(2*a)

print("Resultado x =", bhaskaraPositiva)
print("Resultado X' =", bhaskaraNegativa)

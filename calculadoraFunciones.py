print("Programador: Manuel Dolores Cruz")

# Se definen las funciones
def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def producto(a,b):
    return a * b
def division(a,b):
    return a / b
def divisionEntera(a,b):
    return a // b
def exponente(a,b):
    return a ** b
def modulo(a,b):
    return a % b
def num_1():
    a = int(input("Ingresa el operando a: "))
    return a
def num_2():
    b = int(input("Ingresa el operando b: "))
    return b

while True:
    print("""¿Qué operación quieres hacer?, escribe:
      '+' -> Suma
      '-' -> Resta
      '*' -> Producto
      '/' -> División
      '//' -> División entera
      '**' -> Exponente
      '%' -> Modulo o Residuo
      '2' -> Salir
        """)
      
    operacion = input("Ingresa alguna opción: \n")
    
    if operacion == '+':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"+",b," : ", suma(a,b))
    elif operacion == '-':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"-",b," : ", resta(a,b))
    elif operacion == '*':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"*",b," : ",producto(a,b))
    elif operacion == '/':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"/",b," : ", division(a,b))
    elif operacion == '//':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"//",b," : ", divisionEntera(a,b))
    elif operacion == '**':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"**",b," : ", exponente(a,b))
    elif operacion == '%':
        a = num_1()
        b = num_2()
        print("Resultado ",a,"%",b," : ",modulo(a,b))
    elif operacion == '2':
        break
    else:
        print("Opción no válida vuelve a intentarlo...")


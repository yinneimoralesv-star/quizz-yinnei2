longitudes1 = int(input("primer numero para formar el triangulo"))
longitudes2 = int(input("segundo numero para formar el triangulo"))
longitudes3 = int(input("tercer numero para formar el triangulo"))
if longitudes1 + longitudes2 + longitudes3 and longitudes2 + longitudes1 + longitudes3 and longitudes3 + longitudes1 + longitudes2:
    if longitudes1 == longitudes2 == longitudes3:
        print("el triangulo es equilatero")
    elif longitudes1 == longitudes2 or longitudes1 == longitudes3 or longitudes2 == longitudes3:
        print("el triangulo es isosceles")
    else:
        print(" el triangulo es escaleno") 
    else:
        print(" no se forma un triangulo")
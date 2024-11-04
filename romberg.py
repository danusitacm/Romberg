def funcion(valor):
    return (2/((valor)**2 - 4))

def regla_trapezoidal_compuesta(limite_superior,limite_inferior,n):
    h=(limite_superior-limite_inferior)/n
    return (h/2)*(funcion(limite_inferior) + sumatoria_regla_trapezoidal(limite_inferior,h,n)+ funcion(limite_superior))

def sumatoria_regla_trapezoidal(limite_inferior,h,n):
    suma=0
    for j in range(1,n):
        x=limite_inferior+j*h
        suma+=funcion(x)
    return 2*suma

def Romberg(limite_superior, limite_inferior,fila,columna):
    m=[]
    n=1
    for i in range (0,fila):
        x=[]
        for j in range (0,columna):
            if(j==0):
                x.append(regla_trapezoidal_compuesta(limite_superior,limite_inferior,n))
            elif(i<j):
                x.append(0)
            else:
                x.append(x[j-1]+(1/((4**(j))-1))*(x[j-1]-m[i-1][j-1]))
        m.append(x)
        n*=2  
    Mostrar(m) 

def Mostrar(matriz):
    for fila in matriz:
        for valor in fila:
            ##print("\t",valor, end=" ")
            print("\t{0:.7f}".format(valor), end=" ")
        print()

Romberg(0.35,0,4,4)

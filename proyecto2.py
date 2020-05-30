import pandas as pd
import numpy as np


url = 'https://docs.google.com/spreadsheets/d/1AjZpofZv3Y5U6QRUFtpI_XQgvjJpWXk_6oxGnb2te3o/export?format=csv&gid=1067477951'

url1 = "https://forms.gle/ZvXUaycQtQVJLUQg8"

def GradientD(fila,col,verd):
    fila=fila+0.1*col*(verd-np.dot(fila,col))
    col=col+0.1*fila*(verd-np.dot(fila,col))
    return(fila,col)

def menu():
    o=0
    while o!=3:
        print("buenos dias, desea: ")
        print("1. probar el sistema de recomendaciones? ")
        print("2. Alterar la base de datos? ")
        print("3. salir del programa")
        o = int(input(""))
        if o==1:
            ans = "no"
            while "si" not in ans:
                print("Por favor, llene la siguiente encuesta:\n ",url1)
                ans = input("ya la lleno? ingrese si cuando ya la haya llenado por favor\n")
            data = pd.read_csv(url)
            data = data.drop(columns=['Timestamp'])
            dataMatrix = data.to_numpy()    
            f,c = np.shape(dataMatrix)
            caracteristicas = 10 ##caracteristicas de restaurantes
            u=np.random.rand(f,caracteristicas)
            v=np.random.rand(caracteristicas,c)
            for k in range(1000):###NUMERO DE ITERACIONES
                for i in range(f):
                    for j in range(c):
                        if isinstance(dataMatrix[i][j], (int,float)):
                            fila=u[i]
                            col=v[:,j]
                            fila,col=GradientD(fila,col,dataMatrix[i][j])
                            u[i]=fila
                            v[:,j]=col
            prediccion = np.dot(u,v).astype(int)
            ultimo = prediccion[-1]
            ultra = []
            for i in range(len(dataMatrix[-1])):
                if dataMatrix[-1][i]=='no lo conozco':
                    ultra.append(i)
            print('Se le recomienda ir a los siguientes restaurantes: \n')
            for n in ultra:
                if ultimo[n]>=np.mean(ultimo):
                    print(data.columns[n])
                if ultra==[]:
                    print('Ya conoce todos los restaurantes')
        elif o==2:
            data = pd.read_csv(url)
            data = data.drop(columns=["Timestamp"])
            n = len(data)
            print("Quiere:")
            print("1. Quitar el dato ingresado por un usuario especifico? ")
            print("2. Quitar el ultimo dato")
            o=int(input(""))
            if o==1:
                print("Que numero de dato quisiera quitar, (de 1 a ",n-1," ?")
                print("Donde 1 es el primer dato ingresado.")
                o = int(input(""))
                data = data.drop([o])
            else:
                data = data.drop([n-1])
            print(data.head())
        else:
            print("gracias por usar el programa")
            o=3

menu()
print("Bienvenid@") 
Estudiantes=[]
 
class Estudiante(): 
    Nombre="" 
    Codigo=0 
    Edad=0 
 
def Llenar(): 
    n=input("Ingrese el nombre del estudiante: ") 
    c=input("Ingrese el código del estudiante: ") 
    e=input("Ingrese la edad del estudiante: ") 
    return n,c,e
 
def Mostrar(n,c,e): 
    print("El nombre del estudiante es ",n) 
    print("El código del estudiante es ",c) 
    print("La edad del estudiante es ",e) 
 
for i in range(1, 6): 
    E=Estudiante()
    E.Nombre,E.Codigo,E.Edad=Llenar()
    Estudiantes.append(E)
 
for i in range(0, 5):
    print("Nombre ",i,": ",Estudiantes[i].Nombre)
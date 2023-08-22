class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []
    def ingresarPaciente(self,pac)
        self.__lista_pacientes.append(pac) 
    def VerDatosPaciente(self,c):
        for p in self.__lista_pacientes:
            if c == p.VerCedula():
                return p 
    def VerNumeroPacientes(self):
        print("En el sistema hay:"+str(len(self.__lista_pacientes))+ "pacientes")
    
    def verDatosPaciente(self):
        cedula = int(input("Ingrese la cedula a buscar: "))

    def Verificar(self):
        cedula = int(input("Ingrese la cedula: "))   
        if cedula in self.__lista_pacientes:
            print("El paciente ya está en el sistema")
        else:
            print("A continuación se solicitaran los datos...")
            cedula = int(input("Ingrese la cedula: "))
            nombre = input("Ingrese el nombre: ") 
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            pac = Paciente()
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarNombre(nombre)
            pac.asignarServicio(servicio)
            sis.ingresarPaciente(pac)
      
def main():
    sis = Sistema()
    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. Salir:  \n"))
        if opcion == 1:
            sis.Verificar()
        elif opcion == 2:
            c= int(input("Ingrese la cedula a buscar:"))
            p = sis.verDatosPaciente(c)
            print("Nombre:"+p.verNombre)
            print("Cedula:"+ str(p.verCedula()))
            print("Genero:" + p.verGenero())
            print("Servicio:"+ p.verServivio())
        elif opcion == 3:
            mi_sistema.verDatosPaciente()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")


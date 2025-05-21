class Profesor:
   
    #Esta clase denominada Profesor es una superclase que representa un profesor genérico.
   
    def imprimir(self):
     
        #Método que imprime en pantalla un texto específico identificando
        #que el objeto es un Profesor
     
        print("Es un profesor.")

class ProfesorTitular(Profesor):

   # Esta clase denominada ProfesorTitular es una subclase de Profesor

    def imprimir(self):
       
       # Método que sobreescribe el método imprimir heredado de la clase
       # padre Profesor
       
        print("Es un profesor titular.")

if __name__ == "__main__":

    # Creando un Profesor pero instanciando la clase ProfesorTitular
    profesor1 = ProfesorTitular()
    profesor1.imprimir()  # Output: Es un profesor titular.
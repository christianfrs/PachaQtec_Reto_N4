class Persona():
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad

class Docente(Persona):
    def __init__(self, dni, nombre, edad):
        super().__init__(dni, nombre, edad)

class Alumno(Persona):
    def __init__ (self, dni, nombre, edad, nota, nota_min, nota_max, nota_prom):
        super().__init__(dni, nombre, edad)
        self.nota = nota
        self.nota_min = nota_min
        self.nota_max = nota_max
        self.nota_prom = nota_prom
    
class Archivo():
    def __init__(self, archivo_nombre):
        self.archivo_nombre = archivo_nombre

    def mostrar_archivo(self):
        try:
            file = open (self.archivo_nombre, mode='r', encoding='utf-8')
            print(f'\n')
            for linea in file.readlines():
                print(linea)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print(f'Se visualiza el archivo {self.archivo_nombre}')
    
    def agregar_docente(self, docent):
        try:
            file = open(self.archivo_nombre, mode='a')
            docentes = f'Docente: {docent.dni}, {docent.nombre}, {docent.edad}\n'
            file.write(docentes)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print(f'Se visualiza el docente {docent.nombre}')

    def agregar_alumno(self, alum):
        try:
            file = open(self.archivo_nombre, mode='a')
            alumnos = f'Alumno: {alum.dni}, {alum.nombre}, {alum.edad}, {alum.nota}, {alum.nota_min}, {alum.nota_max}, {alum.nota_prom}\n'
            file.write(alumnos)
        except Exception as e:
            print(f'{str(e)}')
        finally:
            if(file):
                file.close()
                print(f'Se visualiza el alumno {alum.nombre}')
 
#Modulo de registro
while True:
    print(''' Indique a qué tipo de persona va a registrar:
        1.- DOCENTE
        2.- ALUMNO
    ''')

    seleccion = int(input('Número: ')) 

    if seleccion == 1:    
        cant_docentes = int(input('¿Qué cantidad de docentes registrará?: '))

        for a in range(cant_docentes):
            print(f'Ingresa los datos del docente N° {a+1}')
            docentes_nombre = input('Nombre: ')
            docentes_dni = input('DNI: ')    
            docentes_edad = int(input('Edad: '))

            docentes = Docente( docentes_dni, docentes_nombre, docentes_edad)
            archivo = Archivo('docentes.txt')
            archivo.agregar_docente(docentes)
        archivo.mostrar_archivo()
        break    

    elif seleccion == 2:
        cant_alumnos = int(input('¿Qué cantidad de alumnos registrará?: '))
        lista_alumno = []
        lista_nota = []
        nombre_alum = []
        dni_alum = []
        edad_alum = []
        for b in range(cant_alumnos):
            print(f'Ingresa los datos del alumno N° {b+1}')
            nombre = input('Nombre: ')
            dni = input('DNI: ')
            edad = int(input('Edad: '))
            while True: 
                n_notas = int(input('Del 1 al 4 ¿cuántas notas desea ingresar?: '))
                if  n_notas >= 0 and n_notas <= 4:
                        for n in range(n_notas):
                            while True:
                                notas = int(input(f"Ingrese la nota {n + 1}:"))
                                if  notas >= 0 and notas <= 20:
                                    lista_nota.append(notas)
                                    break
                                else:
                                    print('Ingresar una nota entre 00 al 20')
                        lista_alumno.append({
                            'alumno': {
                                'nombre': nombre,
                                'dni': dni,
                                'edad': edad
                            },
                            'notas': lista_nota
                        })
                        lista_nota=[]
                        break
                else:
                    print('Ingresar un número del 1 al 4')
       

        for c in lista_alumno:
            alumnos = Alumno(f"{c['alumno']['dni']}",f"{c['alumno']['nombre']}",f"{c['alumno']['edad']}", f"{c['notas']}", f"{min(c['notas'])}", f"{max(c['notas'])}", f"{sum(c['notas'])/len(c['notas'])}")
            archivo = Archivo('alumnos.txt')
            archivo.agregar_alumno(alumnos)

        archivo.mostrar_archivo()
        break
        

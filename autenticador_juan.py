import socket
from datetime import datetime

class Usuario:
    def __init__(self, ID, nombre, correo, contrasena, tipo):
        self.ID = ID
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.tipo = tipo

class Orden:
    def __init__(self, orden, usuario, fecha, estado, ip):
        self.orden = orden
        self.usuario = usuario
        self.fecha = fecha
        self.estado = estado
        self.ip = ip

class Sistema:
    def __init__(self):
        self.usuarios = []
        self.ordenes = []
        self.fuerza_bruta = Fuerza_bruta()
        self.cache = Cache()

    def crear_orden(self):
        correo = input("ingrese su correo: ").lower()
        contrasena = input("ingrese su contrasena: ")
        if Verificar_usuario.autenticardor(correo, contrasena):
          if Verificar_usuario.autenticar_admin(correo):
            print("Bienvenido administrador")
          else:
            print("Bienvenido usuario")
          orden = input("Ingrese la orden: ")
          orden_nueva = Orden(orden, correo, datetime.now(), "Pendiente", socket.gethostbyname(socket.gethostname()))
          if self.verificar(orden_nueva) is None:
            return
          else:
            self.ordenes.append(orden_nueva)
            print("Orden Creada.")

    def verificar(self,orden):
        if Sondeo.verificar_vacios(orden) == False:
          return
        if self.fuerza_bruta.verificar_ip(orden) == False:
          return
        if self.cache.validar_cache(orden)==False:
          return
        else:
          return True


class Verificar_usuario:
    def autenticardor(correo, contrasena):
        for usuario in sistema.usuarios:
            if usuario.correo == correo and usuario.contrasena == contrasena:
                print(f"Usuario {usuario.nombre} autenticado correctamente.")
                return True
        print("Autenticación fallida.")
        return False

    def autenticar_admin(correo):
        for usuario in sistema.usuarios:
            if usuario.correo == correo:
              return usuario.tipo.lower() == "admin"

class Sondeo:
    def verificar_vacios(orden):
        return orden.orden is not None and orden.orden.strip() != ''

class Fuerza_bruta:
    def __init__(self):
        self.ip_registradas = []

    def verificar_ip(self, orden):
        if orden.ip not in self.ip_registradas:
            contador = 0
            for orden in sistema.ordenes:
                if orden.ip == orden.ip:
                    contador += 1
            if contador >= 3:
                self.ip_registradas.append(orden.ip)
            return True
        else:
            return False

class Cache:
    def __init__(self):
        self.cache = {
            "mal internet":"Reinicie el router",
            "mi gato no come":"Llevelo al veterinario",
            "quiero arroz chino": "+57#numero arroz chino"
        }

    def validar_cache(self,orden):
        if orden.orden.lower() in self.cache:
            print(f"orden ya en cache, respuesta rapida: {self.cache[orden.orden.lower()]}")
            return False
        else:
            return True

if __name__ == "__main__":
    sistema = Sistema()

    # Crear usuarios
    admin = Usuario("492242", "Carlos", "carliños777@gmail.com", "soycarlos", "Admin")
    usuario = Usuario("25992221", "marta", "martuski@gmail.com", "solomillos", "Cliente")
    sistema.usuarios.extend([admin, usuario])

    while True:

      print("Que Desea hacer?")
      print("1. Agregar Orden")
      print("2. salir")

      opcion = input("Ingrese una opción: ")

      if opcion == "1":
          sistema.crear_orden()
      elif opcion == "2":
          break
      else:
          print("Opción inválida. Por favor, elija una opción válida.")
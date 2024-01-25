#se crea clase para instanciar objeto carrito

class carrito:
    #METODO CONSTRUCTO DE La CLASE
    def __init__(self, request):
        self.request=request;#se almacena la peticion actual para ser luego utilizada
        self.session=request.session;#de igual manera se almacena la sesion o se inicia
        carro=self.session.get("carro")# Es el constructor se construye uncarro de la compr pra esta sesion el cual ha iniciado un usuario
        #EL CARRO SERA UN DICCIONARIO
        if not carro:# si no hay carro se crea, el carro sera un diccionario que hace alusion  cada producto
            carro=self.session["carro"]={}
            print("carro creado")
        
        self.carro=carro #si ya habia carro se le reconoce
        print("nada de nada")
    def agregar(self, publicaciones):#se agrega el producto al carrito si es que no se ha agregado
        if(str(publicaciones.id_producto.id_producto) not in self.carro.keys()):
            self.carro[publicaciones.id_producto.id_producto]={
                "producto_id":publicaciones.id_producto.id_producto,
                "nombre":publicaciones.id_producto.nombre_producto,
                "precio":str(publicaciones.id_producto.valor),
                "cantidad":1,

                
                "usuario":publicaciones.id_usuario.username,
                
                "correo":publicaciones.id_usuario.email,
                "descripcion":publicaciones.id_producto.descripcion,
                "publicacion_id":publicaciones.id_publicacion,
        
            }
            #print("nueevo ingreso   ")
        else:
            for key, value in self.carro.items():
                if key ==str(publicaciones.id_producto.id_producto):
                    value["cantidad"]=value["cantidad"]+1
                    value["precio"]=float(value["precio"])+float(publicaciones.id_producto.valor)
                    #print("cambio")
                    break
        self.guardar_carro()

#Se guarda o actualiza el carro
    def guardar_carro(self): #guarada el carro si ya habia sido agregado
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, publicaciones):
        publicaciones.id_producto.id_producto=str(publicaciones.id_producto.id_producto)
        if publicaciones.id_producto.id_producto in self.carro:
            del self.carro[publicaciones.id_producto.id_producto]
            self.guardar_carro()

    def restar_carro(self, publicaciones):
        for key, value in self.carro.items():
            if key ==str(publicaciones.id_producto.id_producto):
                value["cantidad"]=value["cantidad"]-1;
                value["precio"]=float(value["precio"])-float(publicaciones.id_producto.valor)
                if value["cantidad"]<1:
                    self.eliminar(publicaciones)
                break
        self.guardar_carro();

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True;
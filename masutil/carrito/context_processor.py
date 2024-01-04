def importe_total_carrito(request):
    total=0;
    #if request.user.is_authenticated:
    for key, value in request.session["carro"].items():
        total=total+(float(value["precio"]));
    return {"importe_total_carrito":total}
#PARA QUE SEA ACCESIBLE DESDE CUALQUIER LUGAR DEL PROYECTO SE DEBE
# IR A SETTINGS Y REGISTRARLO EN CONTEXT PROCESSORS

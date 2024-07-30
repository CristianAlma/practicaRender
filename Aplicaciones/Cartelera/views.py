from django.http import JsonResponse
from django.shortcuts import redirect, render
from .models import Genero
from .models import Pelicula
from .models import Director
from .models import Pais
from .models import Cine
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,"home.html")

#Rendirizando el template de listadoGeneros
def listadoGeneros(request):
    generosBdd=Genero.objects.all()
    return render(request,"listadoGeneros.html", {'generos':generosBdd})

def listadoPelicula(request):
    peliculaBdd=Pelicula.objects.all()
    return render(request,"listadoPelicula.html",{'pelicula':peliculaBdd})

def listadoDirector(request):
    directorBdd=Director.objects.all()
    return render(request,"listadoDirector.html",{'director':directorBdd})

def listadoPais(request):
    paisBdd=Pais.objects.all()
    return render(request,"listadoPais.html",{'pais':paisBdd})

def eliminarGenero(request,id):
    generoEliminar=Genero.objects.get(id=id)
    generoEliminar.delete()
    messages.success(request,"Género eliminado exitosamente")
    return redirect('listadoGeneros')

#Renderisando formulario de nuevo genero
def nuevoGenero(request):
    return render(request,'nuevoGenero.html')

#Insertando generos en la base de datos
def guardarGenero(request):
    nom=request.POST["nombre"]
    des=request.POST["descripcion"]
    fot=request.FILES.get("foto")
    nuevoGenero=Genero.objects.create(nombre=nom,descripcion=des,foto=fot)
    messages.success(request,"Género registrado exitosamente.")
    return redirect('listadoGeneros')

#Renderizando formulario de actualizacion 
def editarGenero(request,id):
    generoEditar=Genero.objects.get(id=id)
    return render(request,'editarGenero.html',{'generoEditar':generoEditar})


#Actualizando los nuevos datos en la BDD
def procesarActualizacionGenero(request):
    id=request.POST['id']
    nom=request.POST['nombre']
    desc=request.POST['descripcion']
    
    generoConsultado=Genero.objects.get(id=id)
    generoConsultado.nombre=nom
    generoConsultado.descripcion=desc
    generoConsultado.save()
    messages.success(request,'Genero actualizado exitosamente.')
    return redirect('listadoGeneros')

#Configurar PAIS para editar
def editarPais(request,id):
    paisEditar=Pais.objects.get(id=id)
    return render(request,'editarPais.html',{'paisEditar':paisEditar})

def procesarActualizacionPais(request):
    id=request.POST['id']
    nom=request.POST['nombre']
    con=request.POST['continente']
    cap=request.POST['capital']
    paisConsultado=Pais.objects.get(id=id)
    paisConsultado.nombre=nom
    paisConsultado.continente=con
    paisConsultado.capital=cap
    paisConsultado.save()
    messages.success(request,'Pais actualizado exitosamente.')
    return redirect('listadoPais')


#Configurar DIRECTOR para editar
def editarDirector(request,id):
    directorEditar=Director.objects.get(id=id)
    return render(request,'editarDirector.html',{'directorEditar':directorEditar})

def procesarActualizacionDirector(request):
    id=request.POST['id']
    ced=request.POST['dni']
    ape=request.POST['apellido']
    nom=request.POST['nombre']
    fot=request.FILES.get("foto")
    es = 'estado' in request.POST and request.POST['estado']=='on'
    directorConsultado=Director.objects.get(id=id)
    directorConsultado.dni=ced
    directorConsultado.apellido=ape
    directorConsultado.nombre=nom
    directorConsultado.estado=es
    directorConsultado.foto=fot
    directorConsultado.save()
    messages.success(request,'Director actualizado exitosamente.')
    return redirect('listadoDirector')

#Configurar PELICULA para editar
def editarPelicula(request,id):
    peliculaEditar=Pelicula.objects.get(id=id)
    genero=Genero.objects.all()
    director=Director.objects.all()
    return render(request,'editarPelicula.html',{'peliculaEditar':peliculaEditar,'generos':genero, 'directors':director})

def procesarActualizacionPelicula(request):
    id=request.POST['id']
    tit=request.POST['titulo']
    dur=request.POST['duracion']
    sin=request.POST['sinopsis']
    gen=request.POST['genero']
    dir=request.POST['director']
    peliculaConsultado=Pelicula.objects.get(id=id)
    peliculaConsultado.titulo=tit
    peliculaConsultado.duracion=dur
    peliculaConsultado.sinopsis=sin
    #Instaciar
    genero_instancia = Genero.objects.get(id=gen)
    director_instancia= Director.objects.get(id=dir)
    peliculaConsultado.genero=genero_instancia
    peliculaConsultado.director=director_instancia
    peliculaConsultado.save()
    messages.success(request,'Pelicula actualizada exitosamente.')
    return redirect('listadoPelicula')




#Renderisando formulario de nuevo genero
def nuevoDirector(request):
    return render(request,'nuevoDirector.html')

#Insertando generos en la base de datos
def guardarDirector(request):
    dni=request.POST["dni"]
    ape=request.POST["apellido"]
    nom=request.POST["nombre"]
    fot=request.FILES.get("foto")
    nuevoDirector=Director.objects.create(dni=dni, apellido=ape, nombre=nom, foto=fot)
    messages.success(request,"Director registrado exitosamente.")
    return redirect('listadoDirector')

def eliminarDirector(request,id):
    directorEliminar=Director.objects.get(id=id)
    directorEliminar.delete()
    messages.success(request,"Director eliminado exitosamente")
    return redirect('listadoDirector')


#CINES
def gestionCines(request):
    return render(request,'gestionCines.html')

#Insertando cines mediante AJAX en la Base de Datos
@csrf_exempt
def guardarCine(request):
    nom=request.POST["nombre"]
    dir=request.POST["direccion"]
    tel=request.POST["telefono"]
    nuevoCine=Cine.objects.create(nombre=nom,direccion=dir,telefono=tel)    
    return JsonResponse({
        'estado': True,
        'mensaje': 'Cine registrado exitosamente.'
    })


def listadoCines(request):
    cinesBdd=Cine.objects.all()
    return render(request,"listadoCines.html", {'cines':cinesBdd})


#DIRECTOR
def gestionDirectores(request):
    return render(request,'gestionDirector.html')

#Insertando cines mediante AJAX en la Base de Datos
#CON AJAX
# @csrf_exempt
# def guardarDirector(request):
#     dni=request.POST["dni"]
#     ape=request.POST["apellido"]
#     nom=request.POST["nombre"]
#     es = 'estado' in request.POST and request.POST['estado']=='on'
#     fot=request.FILES.get("foto")
#     nuevoDirector=Director.objects.create(dni=dni, apellido=ape, nombre=nom,estado=es, foto=fot)    
#     return JsonResponse({
#         'estado': True,
#         'mensaje': 'Director registrado exitosamente.'
#     })
@csrf_exempt
def guardarDirector(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        dni = request.POST.get("dni")
        apellido = request.POST.get("apellido")
        nombre = request.POST.get("nombre")
        estado = request.POST.get("estado", False) == 'on'  # Convertir a booleano
        foto = request.FILES.get("foto")

        try:
            # Crear una nueva instancia de Director
            nuevoDirector = Director.objects.create(
                dni=dni,
                apellido=apellido,
                nombre=nombre,
                estado=estado,
                foto=foto
            )

            return JsonResponse({
                'estado': True,
                'mensaje': 'Director registrado exitosamente.'
            })
        except Exception as e:
            # Manejar cualquier excepción que pueda ocurrir durante la creación
            return JsonResponse({
                'estado': False,
                'mensaje': f'Error al registrar el director: {str(e)}'
            })
    else:
        # Si no es una solicitud POST, retornar un error
        return JsonResponse({
            'estado': False,
            'mensaje': 'Método no permitido.'
        })

#CON AJAX
def listadoDirectores(request):
    directoresBdd = Director.objects.all()
    return render(request, "listadoDirectores.html", {'directores': directoresBdd})


#PELICULA
def gestionPeliculas(request):
    director = Director.objects.all()
    genero = Genero.objects.all()
    return render(request,'gestionPelicula.html',{'directores':director,'generos':genero})

#Insertando cines mediante AJAX en la Base de Datos
@csrf_exempt
def guardarPelicula(request):
    tit = request.POST["titulo"]
    dur = request.POST["duracion"]
    sip = request.POST["sinopsis"]

    gen = request.POST["genero"]
    genero_instancia = Genero.objects.get(id=gen)

    dir = request.POST["director"]
    director_instancia = Director.objects.get(id=dir)

    nuevaPelicula = Pelicula.objects.create(
        titulo=tit, duracion=dur, sinopsis=sip,
        genero=genero_instancia, director=director_instancia
    )

    return JsonResponse({
        'estado': True,
        'mensaje': 'Película registrada exitosamente.'
    })

    

def listadoPeliculas(request):
    peliculasBdd=Pelicula.objects.all()
    return render(request,"listadoPelicula.html", {'peliculas':peliculasBdd})

# def exportCines(request):
#     dataCines = Cine.objects.all()
#     return render(request,"exportCines.html", {'cines': dataCines})

# def exportCinesPDF(request):
#     #llamar a todos los datos del modelo cina
#     cines = Cine.objects.all()
#     #llamar al template con el render string
#     html_string = render_to_string('exportCines.html', {'cines': cines})
#     #almacenar como un archivo html
#     html = HTML(string=html_string)
#     #leer todo el html guardado y convvertirlo en un pdf
#     pdf = html.write_pdf()
#     #dar una respuesta como pdf(archivo)
#     response = HttpResponse(pdf, content_type='application/pdf')
#     #nombrar y dar una extension al archivo expotado
#     response['Content-Disposition'] = 'attachment; filename="reporte_cines.pdf"'
#     #exportar archivo
#     return response

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.db.models import F

@csrf_exempt
def robot_motion_post(request):
    if request.method == 'POST':
        data = []
        motion = request.body.decode('utf-8')
        etiqueta = Etiquetas.objects.get(nombre=motion)
        etiqueta_data = {
            'nombre':etiqueta.nombre,
            'descripcion':etiqueta.descripcion,
            'movimientos':[]
        }
        movimientos = etiqueta.movimientos.all()
        for movimiento in movimientos:
            movimiento_data = {
                'id_movimiento': movimiento.id,
                'descripcion_movimiento': movimiento.descripcion,
                'submovimientos': []
            }
            submovimientos = Submovimientos.objects.filter(id_movimiento=movimiento.id)
            for submovimiento in submovimientos:
                submovimiento_data = {
                    'join_1': str(submovimiento.join_1),
                    'join_2': str(submovimiento.join_2),
                    'join_3': str(submovimiento.join_3),
                    'join_4': str(submovimiento.join_4),
                    'join_5': str(submovimiento.join_5),
                    'velocidad': str(submovimiento.velocidad)
                }
            # Agregar el diccionario del submovimiento a la lista de submovimientos del movimiento actual
                movimiento_data['submovimientos'].append(submovimiento_data)
        # Agregar el diccionario del movimiento a la lista de movimientos de la etiqueta actual
            etiqueta_data['movimientos'].append(movimiento_data)
    # Agregar el diccionario de la etiqueta a la lista de datos
        data.append(etiqueta_data)
        response_data = {
            'message': 'Petición recibida correctamente',
            'Data': list(data)
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Metodo no permitido")

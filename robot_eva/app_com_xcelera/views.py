from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.db.models import F
from robot_eva_controller.app_robot_controller import Robot 


def get_json_data(etiqueta):
    data = []
    etiqueta_data = {
        'nombre': etiqueta.nombre,
        'descripcion': etiqueta.descripcion,
        'movimientos': []
    }
    movimientos = etiqueta.movimientos.all()
    for movimiento in movimientos:
        movimiento_data = {
            'id_movimiento': movimiento.id,
            'descripcion_movimiento': movimiento.descripcion,
            'orden': movimiento.orden,
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
            movimiento_data['submovimientos'].append(submovimiento_data)
        etiqueta_data['movimientos'].append(movimiento_data)
    data.append(etiqueta_data)
    return data


@csrf_exempt
def robot_motion_post(request, motion):
    if request.method == 'POST':
        # motion = request.body.decode('utf-8')
        etiqueta = Etiquetas.objects.get(nombre=motion)
        data = get_json_data(etiqueta)
        response_data = {
            'message': 'Petición recibida correctamente',
            'Data': list(data)
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Metodo no permitido")

@csrf_exempt
def robot_go_zero(request):

    robot = Robot()
    if request.method == 'GET':
        robot.go_zero()
        response_data = {
            'message': 'Petición recibida correctamente',
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Metodo no permitido")





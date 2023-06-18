
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.db.models import F

@csrf_exempt
def robot_motion_post(request):
    if request.method == 'POST':
        motion = request.body.decode('utf-8')
        result = Movimientos.objects.filter(id_etiqueta__nombre__icontains=motion).values(
            'id',
            'id_etiqueta__nombre',
            'submovimientos__join_1',
            'submovimientos__join_2',
            'submovimientos__join_3',
            'submovimientos__join_4',
            'submovimientos__join_5',
            'submovimientos__velocidad',
            'orden',
            'descripcion'
        )
        response_data = {
            'message': 'Petición recibida correctamente',
            'Data': list(result)
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Metodo no permitido")

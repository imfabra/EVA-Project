
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from app_crud.models import Etiqueta, Movimiento, Submovimiento

@csrf_exempt
def robot_motion_post(request):
    if request.method == 'POST':
        motion = request.body.decode('utf-8')
        label = Etiqueta.objects.filter(nombre=motion)
        response_data = {
            'message': 'Petición recibida correctamente',
            'Data': list(label.values())
        }
        return JsonResponse(response_data)
    else:
        return HttpResponse("Metodo no permitido")

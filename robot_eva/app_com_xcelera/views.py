
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
from django.db.models import F

@csrf_exempt
def robot_motion_post(request):
    if request.method == 'POST':
        motion = request.body.decode('utf-8')
        # response_data = {
        #     'message': 'Petición recibida correctamente',
        #     'Data': list(result)
        # }
        # return JsonResponse(response_data)
    else:
        return HttpResponse("Metodo no permitido")

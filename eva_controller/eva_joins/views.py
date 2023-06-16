
from django.shortcuts import render

def joins(request):
    if request.method == 'POST':
        values = []
        for i in range(5):
            value = request.POST.get('range{}'.format(i))
            values.append(value)
        return render(request, 'eva_joins/joins.html', {'values': values})
    return render(request, 'eva_joins/joins.html')

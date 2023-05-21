from django.shortcuts import render

def joins(request):
    if 'counter' not in request.session:
        request.session['counter'] = 0

    if request.method == 'POST':
        if 'increment' in request.POST:
            request.session['counter'] += 1
        elif 'decrement' in request.POST:
            request.session['counter'] -= 1

    context = {'number': '123', 'counter': request.session['counter']}

    return render(request, 'eva_joins/joins.html', context)

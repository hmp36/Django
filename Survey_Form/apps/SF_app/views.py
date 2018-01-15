from django.shortcuts import render, redirect, HttpResponse

# Create your views here.


def index(request):
    return render(request,'SF_app/index.html')


def process(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['language'] = request.POST['language']
    request.session['comment'] = request.POST['comment']
    return redirect('result.html')


def result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'count': request.session['count']
    }
    return render(request,'result.html', context)


def reset(request):
    request.session['count'] = 0
    return redirect('SF_app/index.html')

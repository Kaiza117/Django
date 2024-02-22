from django.shortcuts import render, redirect, HttpResponse

def index(request):
    return render(request, 'servey_index.html')

def result(request):
    if request.method == 'POST':
        print(request.POST)
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
    
        return redirect('/result')
    
    elif request.method == 'GET':
        return redirect('/result')

def result(request):
    return render(request, 'result.html')
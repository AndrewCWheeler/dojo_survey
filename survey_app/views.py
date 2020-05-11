from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def result(request, yourName, yourLocation, yourLanguage, yourComments):
    context = {
        'your_name' : yourName,
        'location' : yourLocation,
        'fav_language' : yourLanguage,
        'comments' : yourComments,
    }

    return render(request, 'result.html', context)

def process(request):
    yourName = request.POST['your_name']
    yourLocation = request.POST['location']
    yourLanguage = request.POST['fav_language']
    yourComments = request.POST['comments']
    print(f'I am {yourName}, and I live in {yourLocation}. My favorite language is {yourLanguage}. Here is what I think about Coding Dojo so far: {yourComments}')
    return redirect(f'/result/{yourName}/{yourLocation}/{yourLanguage}/{yourComments}')

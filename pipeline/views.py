from django.http import HttpResponse
from django.shortcuts import render,redirect
import time

def index(request):
    name = request.GET.get('name')
    greet = request.GET.get('greeting')
    sex = request.GET.get('sex')
    hy=''
    if sex == 'male' :
        hy='Sir'
    else :
        hy='Madam'
    # cu={'name':'neko','place':'nekoland'}
    imo = {"nome":name,'greet':greet,"gen":hy}
    return render(request,'2index.html',imo)
    # return HttpResponse("Home")


def analyze(request):
    dtext = request.GET.get('text','default')
    removep = request.GET.get('removep','off')
    capitalize = request.GET.get('capitalize','off')
    linerem = request.GET.get('linerem','off')
    spacerem = request.GET.get('spacerem','off')
    print(dtext)
    print(removep)
    print(linerem)
    print(spacerem)
    analyzed = ""
    # analyzed = dtext
    if removep == 'on':
        punctuations = ''';-][{]}-_+=!@#$'%^&*\()/,.:;><"'''
        analyzed = ""
        for char in dtext:
            if char not in punctuations:
                analyzed = analyzed + char
                params = {'purpose':'Remove Punctuation','analyzed_text':analyzed}
                dtext=analyzed
         
    if (capitalize == "on"):
        analyzed = ""
        for char in dtext:
            analyzed = analyzed + char.upper()
            params = {'purpose':'Change to uppercase','analyzed_text':analyzed}
            dtext = analyzed
            
    if (linerem == "on"):
        analyzed = ""
        for char in dtext:
            if char !="/n" and char != '/r':
                analyzed = analyzed + char 
                params = {'purpose':'New line remover','analyzed_text':analyzed}
                dtext = analyzed
                
    if (spacerem == "on"):
        analyzed = ""
        for index, char in enumerate(dtext):
            if not(dtext[index] == " " and dtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}  
                 
    if (removep != 'on' and capitalize != 'on' and linerem !='on' and spacerem !='on'):
        return render(request,'error.html')             
                
    return render(request,'2analyze.html',params)             
              
                       
    
                
            
    

def greeting(request):
    current_time = int(time.strftime('%H'))
    greeting_message = ""

    if current_time < 12:
        greeting_message = "Good morning"
    elif current_time < 18:
        greeting_message = "Good afternoon"
    else:
        greeting_message = "Good evening"

    if request.method == 'POST':
        name = request.POST['name']
        sex = request.POST['sex']
        return redirect('/index/?name={}&greeting={}&sex={}'.format(name, greeting_message,sex))
    else:
        context = {'greeting': greeting_message}
        return render(request, 'greeting.html', context)


# def capfirst(request):
#     return HttpResponse("Capitalize first <a href='/'>back</a>")


# def first(request):
#     return HttpResponse("Initialize <a href='/'>back</a>")


# def last(request):
#     return HttpResponse("Space <a href='/'>back</a>")



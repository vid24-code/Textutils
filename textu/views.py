# I have created this file - vidhan
from django.http import HttpResponse
from django.shortcuts import render
"""
def index(request):
   return HttpResponse('''<h1>Vidhan</h1> <a href="https://www.youtube.com/
    watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7"> 
    Django CodewithVidhan</a>''')

def about(request):
    return HttpResponse("About Vidhan Bhai")

"""
"""
def index(request):
    params = {'name':'Vidhan','place':'Saturn'}
    return render(request, 'index.html', params)
    #return HttpResponse("Home")
"""
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("Home")

"""
def ex1(request):
    return HttpResponse('''<center><h1>Web Site Directory</h1><table border='1'>
     <tr><td>Web Site Name</td><td>Information</td></tr>
     <tr><td><a href='https://www.google.co.in/?gws_rd=ssl'>Google</a></td><td>A google
      is a web based tool that enables user to locate information on the World Wide Web</td></tr>
      <tr><td><a href='https://www.facebook.com/'>Facebook</a></td><td>Facebook
      is a social networking site that makes it easy to connect and share with family and friend online </td></tr>
      <tr><td><a href='https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12'>CodeWithHarry</a></td><td>
      Code with Harry channel is the esiest way to master in python</td></tr>
      </table></center>''')
"""

def analyze(request):
    djtext = request.POST.get('text','default')


    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    # analyzed = djtext
    if removepunc == 'on':
         punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
         analyzed = ""
         for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
         params = {'purpose':'Removed Punctuations','analyzed_text': analyzed}
         djtext=analyzed
         #return render(request, 'analyze.html',params)
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index]==" " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}


    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremover !="on"):
        return HttpResponse("Please select the operation")
    return render(request, 'analyze.html', params)


"""
def capfirst(request):
    return HttpResponse("capitalize first<a href ='/'>back</a>")

def newlineremove(request):
    return HttpResponse("newlineremove <a href ='/'>back</a>")

def spaceremove(request):
    return HttpResponse("space remover <a href ='/'>back</a>")

def charcount(request):
    return HttpResponse("charcount <a href ='/'>back</a>")
"""
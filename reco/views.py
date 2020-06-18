from django.shortcuts import render
from django.http import HttpResponse
from .models import upload
from .forms import forupload
import os
from django.core.files.storage import FileSystemStorage,File
from django.utils.datastructures import MultiValueDictKeyError
import speech_recognition as sr

def delete(request):
    if request.method=='POST':
        pk=int(request.POST['idval'])
        upload.objects.get(id=pk).delete()
        up=upload.objects.all()
        return render(request, 'home.html',{'up':up})
def home(request):
    if request.method=='POST':

        gettxt=''
         
        if 'Submit' in request.POST:
            fo = request.FILES['fo1']
            fs=FileSystemStorage()
            x=fs.get_available_name(fo.name)
            fs.save(x,fo)  
            gettxt=gettxtbyfile(fs,x)
            fs.delete(x)
        elif 'Speak' in request.POST:
            gettxt=gettxtbyvoice()
        
        f=open('media/gen.txt','w')
        f.write(gettxt)        
        return render(request, 'home.html',{'go':'http://127.0.0.1:8000/media/gen.txt','gettxt':gettxt})
    else:
        form = forupload()
        return render(request, 'home.html',{'form':form})

def gettxtbyfile(file,name):
    r1=sr.Recognizer()
    filename=str(file.location) + '\\'+name
    with sr.AudioFile(filename) as source:
        audio=r1.listen(source)
    try:
        return r1.recognize_google(audio)
    except Exception:
        return 'Something went wrong'
def gettxtbyvoice():
    r1=sr.Recognizer()
    with sr.Microphone() as source:
        audio=r1.listen(source)
    try:
        return r1.recognize_google(audio)
    except Exception:
        return 'Something went wrong'
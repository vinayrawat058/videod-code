from django.shortcuts import render,redirect
from pytube import YouTube
import os

url = ''

# Create your views here.
def ytb_down(request):
    return render(request,'ytb_main.html')

#Creating function for yt_download

def yt_download(request):
    global url
    try:
        url = request.GET.get('url')
        #createing an object of youtube 
        obj = YouTube(url)

        resolutions = []

        strm_all = obj.streams.all()
        for i in strm_all:
            resolutions.append(i.resolution)
        resolutions = list(dict.fromkeys(resolutions))
        embed_link = url.replace("watch?v=", 'embed/')
        path = 'D:\\'

        return render(request, 'yt_download.html',{'rsl':resolutions, 'embd':embed_link, 'path':path})
    except:
        return render(request,'sorry.html')



def download_complete(request,res):
    global url
    homedir  = os.path.expanduser("~")
    dirs = homedir + '/Downloads'
    print(f'DIRECT :', f'{dirs}/Downloads')
    if request.method == 'POST':
        YouTube(url).streams.first().download(homedir + '/Downloads')
        return render(request,'download_complete.html')
    else:
        return render(request, 'sorry.html')

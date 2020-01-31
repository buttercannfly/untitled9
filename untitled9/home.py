import json
import os

from django.http import FileResponse
from django.shortcuts import render

from untitled9.func import get_flv_by_url


def index(request):
    context = {}
    path = os.path.abspath('.')
    video_dir = str(path) + r"\bilibili_video"
    dirs = os.listdir(video_dir)
    context['list'] = dirs
    if request.method == 'POST':
        url = request.POST['input']
        get_flv_by_url(url)
        template = "index.html"
        return render(request, template, context)
    template = "index.html"
    return render(request, template, context)


def download(request):
    movie = request.GET.get('movie')
    print(movie)
    path = 'bilibili_video/' + movie + '/' + movie + '.mp4'
    file = open(path, 'rb')
    response = FileResponse(file)
    response['Content-Type'] = 'video/mpeg4'
    response['Content-Disposition'] = 'attachment; filename="1.mp4"'
    return response


def get_list(request):
    context = {}
    path = os.path.abspath('.')
    video_dir = str(path) + r"\bilibili_video"
    dirs = os.listdir(video_dir)
    context['list'] = dirs
    template = "videos.html"
    return render(request, template, context)
import json

from django.shortcuts import render

from untitled9.func import get_flv_by_url


def index(request):
    context = {}
    if request.method == 'POST':
        url = request.POST['input']
        get_flv_by_url(url)
        template = "index.html"
        return render(request, template, context)
    template = "index.html"
    return render(request, template, context)


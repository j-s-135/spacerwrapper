from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse
from django.template import loader
import base64
import os
from spacerwrapper.configuration import HOST_URL_AND_PORT

def tree(request):
    context = {"url": HOST_URL_AND_PORT}
    template = loader.get_template("tree/tree.html")
    return HttpResponse(template.render(context))

def trees(request):
    context = {}
    template = loader.get_template("tree/trees.html")
    return HttpResponse(template.render(context))

def encode(request):
    img = "no response"
    if request.method == "POST":
        file = request.FILES["image"]
        file.seek(0)
        binary = file.read()
        enc = base64.b64encode(binary)
        enc = enc.decode()
        name = file.name
        ext = os.path.splitext(name)[1]
        ext = ext[1:]
        img = f"<img src='data:img/{ext};base64,"
        img += enc
        img += "'>"
    return HttpResponse(img, content_type="text/plain")

def download(request):
    if request.method == "POST":
        file = request.FILES["upload"]
        file.seek(0)
        response = HttpResponse(file.read(), mimetype="text/plain")
        response['Content-Disposition'] = 'inline;filename=file.txt'
        return response

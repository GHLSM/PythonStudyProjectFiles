from django.shortcuts import render, HttpResponse


def handle(request):
    request.GET.get("msg")
    return HttpResponse("hi")

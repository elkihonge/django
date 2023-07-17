from django.shortcuts import render, redirect


def aboutpage(request):
    return render(request, "About.html")


def servicespage(request):
    return render(request, "Services.html")


def projectpage(request):
    return render(request, "projects.html")


def blogpage(request):
    return render(request, "blog.html")

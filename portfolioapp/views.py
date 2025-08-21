from django.shortcuts import render

def portfolio(request):
    return render(request, "portfolio.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

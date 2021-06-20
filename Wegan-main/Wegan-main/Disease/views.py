from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")


def disease(request):
    return render(request, "disease.html")
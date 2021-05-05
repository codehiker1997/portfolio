from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("This is Faizan Tanveer")
    
    return render(request, 'index.html')


def about(request):
    # return HttpResponse("about")
    return render(request, 'about.html')


def project(request):
    # return HttpResponse("Project")
    return render(request, 'project.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        sce = request.POST['sce']
        print(name, email , sce)
        ins = Contact(name= name, email= email, sce= sce)
        ins.save()
        print("the data has been written to the db")
    return render(request, 'contact.html')

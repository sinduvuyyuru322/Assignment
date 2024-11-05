from django.shortcuts import render,HttpResponse
from .models import Delivary_address,address

# Create your views here.
def firstpage(request):
    return render(request,"firstpage.html")

def homepage(request):
    if request.method == "POST":
        emailid = request.POST['emailid']
        passward = request.POST['passward']
    
        delivary = Delivary_address(emailid=emailid,passward=passward)
        delivary.save()
    return render(request,"homepage.html")
def create(request):
    if request.method == "POST":
        emailid = request.POST['emailid']
        passward = request.POST['passward']
        conform = request.POST['passward']
    
        delivary = address(emailid=emailid,passward=passward,conform=conform)
        delivary.save()
    return render(request,"create.html")
def login(request):
    detail = Delivary_address.objects.all()
    return render(request,"data.html",{"data":detail})

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import Reg
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegView(View):
    def post(self,request):
        fn=request.POST["t1"]
        ln=request.POST["t2"]
        un=request.POST["t3"]
        pwd=request.POST["t4"]
        cpwd=request.POST["t5"]
        mobno=request.POST["t6"]
        email=request.POST["t7"]
        r1=Reg(firstname=fn,lastname=ln,username=un,password=pwd,cpassword=cpwd,mobno=mobno,email=email)
        r1.save()
        return HttpResponse("registration success")



from django.shortcuts import render
from .models import place
# Create your views here.
def web2(request):
    obj=place.objects.all
    return render(request,'index.html',{'result':obj})
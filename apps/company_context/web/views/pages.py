from django.http import HttpResponse
from django.shortcuts import render

def company_created(request): return render(request,'company_context/company_created.html')

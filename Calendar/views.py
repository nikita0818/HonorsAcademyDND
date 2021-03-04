from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'Calendar/home.html',{})

# def index(request):
# 	return render(request, 'Calendar/index.html',{})

def initial(request):
	return HttpResponse('input')

def final(request):
	return HttpResponse('output')
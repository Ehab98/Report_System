<<<<<<< HEAD
from django.shortcuts import render
from django.http import HttpResponse

from repair.models import Enquiry

# Create your views here.

def homepage(request):
	return render(request,'index.html')
=======
from django.shortcuts import render
from django.http import HttpResponse

from repair.models import Enquiry

# Create your views here.

def homepage(request):
	return render(request,'index.html')
>>>>>>> 82835c48c97b5622541c6cb9e52efcec4ece4bb2
	#monospace
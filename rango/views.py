from django.shortcuts import render

from django.http import HttpResponse

# Import the Category model
from rango.models import Category

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    
    context_dict = {'categories': category_list}
    # Render the response and send it back!
return render(request, 'rango/index.html', context_dict)
<<<<<<< HEAD
def about(request):
	return HttpResponse('rango says this is the about page')  

def rangImage(request):
	return HttpResponse('rango says here is the immage')   
=======
    
>>>>>>> 2a624b6a079f0b36308200f492c8ead6f59515ea

# Create your views here.

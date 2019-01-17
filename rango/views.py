from django.http import HttpResponse
from django.shortcuts import render


def index(request):
	# Construct a dictionary to pass to the template engine as its context.
	context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
	# boldmessage is linked to the "boldmessage" seen in the index.html file
	return render(request, 'rango/index.html', context=context_dict)


# Creating the view for the index page and adding a link to the about page
#return HttpResponse("Rango says hey there partner! <br/> <a href= ' /rango/about/'> Click for About Page! </a>")

# Creating the view for the about page and adding a link back to index page
def about(request):
	return HttpResponse("Rango says here is the about page. <br/> <a href=' /rango/'> Index Page </a>")



from django.http import HttpResponse

# Creating the view for the index page and adding a link to the about page
def index(request):
	return HttpResponse("Rango says hey there partner! <br/> <a href= ' /rango/about/'> Click for About Page! </a>")

# Creating the view for the about page and adding a link back to index page
def about(request):
	return HttpResponse("Rango says here is the about page. <br/> <a href=' /rango/'> Index Page </a>")



from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category


def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"}
    # boldmessage is linked to the "boldmessage" seen in the index.html file

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)


# Creating the view for the index page and adding a link to the about page
# return HttpResponse("Rango says hey there partner!
# <br/> <a href= ' /rango/about/'> Click for About Page! </a>")


# Creating the view for the about page and adding a link back to index page
def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Ashleigh"}
    return render(request, 'rango/about.html', context=context_dict)

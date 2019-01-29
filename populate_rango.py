import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page


def populate():

    python_pages = [
        {"title": "Official Python Tutorial",
            "url": "http://docs.python.org/2/tutorial/",
            "views": 22},
        {"title": "How to Think like a Computer Scientist",
            "url": "http://www.greenteapress.com/thinkpython/",
            "views": 68},
        {"title": "Learn Python in 10 Minutes",
            "url": "http://www.korokithakis.net/tutorials/python/",
            "views": 125}]

    django_pages = [
        {"title": "Official Django Tutorial",
            "url": "https://docs.djangoproject.com/en/1.9/intro/tutorial01/",
            "views": 279},
        {"title": "Django Rocks",
            "url": "http://www.djangorocks.com/",
            "views": 55},
        {"title": "How to Tango with Django",
            "url": "http://www.tangowithdjango.com/",
            "views": 187}]

    other_pages = [
        {"title": "Bottle",
            "url": "http://bottlepy.org/docs/dev/",
            "views": 32},
        {"title": "Flask",
            "url": "http://flask.pocoo.org",
            "views": 241}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 128, "likes": 64},
            "Other Frameworks": {"pages": other_pages,
                "views": 32, "likes": 64}
            }

# if you want to add more catergories or pages,
# add them to the dictionaries above

# The code below goes through the cats dictionary, then adds each category,
# and then adds all the associated pages for that category

# Using the .items returns the key and the value. In this case the key is
# "Python", "Django" or "Other Frameworks" and the value (cat_data)
# is the corresponding dictionary in cats.

    for cat, cat_data in cats.items():
        # Updated the population script to pass through the specific values
        # for views and likes
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out what we have added to the user
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    p.url = url
    p.views = views
    # Save the changes we made
    p.save()
    return p


# Added likes and views and set to 0
def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here
if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()

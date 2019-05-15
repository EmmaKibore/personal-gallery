from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Image, Location, Category

# Create your views here.
def index(request):

    '''
    view function to display landing page
    '''

    images = Image.objects.all()

    return render(request, 'index.html', {"images": images})


def search_page(request):

    '''
    view function to open search page and display searched images
    '''

    if 'search' in request.GET and request.GET["search"]:
        search_term = request.GET.get("search")
        images = Image.search_image(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "images": images})

    else:
        message = "You haven't searched for any item"
        return render(request, 'search.html',{"message":message})

def sortby_locations(request):

    '''
    view function to display images sorted by Location
    '''

    images = Image.filter_by_location()

    return render(request, 'location.html', {"images":images})

def single_image(request, image_id):

    '''
    view function to display a single image and its details
    '''

    image = Image.get_image_by_id(image_id)
    return render(request, 'single_image.html', {"image":image})
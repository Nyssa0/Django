from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse

from .forms import ProductForm
from .models import Product


# Create your views here.
def index(request):
    return render(request, 'app/index.html')


def create(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "app/create.html", context)


def read(request):
    # dictionary for initial data with
    # field names as keys
    context = {"dataset": Product.objects.all()}

    # add the dictionary during initialization

    return render(request, "app/read.html", context)


# pass id attribute from urls
def read_detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {"data": Product.objects.get(pk=id)}

    # add the dictionary during initialization

    return render(request, "app/read_detail.html", context)


def delete(request, id):
    context = {"data": Product.objects.get(pk=id)}

    context["data"].delete()

    return HttpResponseRedirect('../read')

def update(request, id):

    context = {"data": Product.objects.get(pk=id)}
    template = loader.get_template('app/update.html')
    return HttpResponse(template.render(context, request))

def updateproduct(request, id):
  name = request.POST['name']
  description = request.POST['description']
  image = request.POST['image']
  price = request.POST['price']
  stock = request.POST['stock']
  data = Product.objects.get(pk=id)
  data.name = name
  data.description = description
  data.image = image
  data.price = price
  data.stock = stock
  data.save()
  context = {"data": Product.objects.get(pk=id)}
  return render(request, "app/read_detail.html", context)


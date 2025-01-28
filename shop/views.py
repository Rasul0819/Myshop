from django.shortcuts import render,get_object_or_404


from . import models

# Create your views here.
def homepage(request):
    products = models.Product.objects.all()

    return render(request,'shop/home.html',{'products':products})


def detail(request,id):

    detail = get_object_or_404(models.Product,id=id)
    reviews = models.Reviews.objects.all()
    return render(request,'shop/detail.html',{'detail':detail,
                                         'reviews':reviews})

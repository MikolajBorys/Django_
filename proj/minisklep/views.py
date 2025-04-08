from django.shortcuts import render, redirect
from .models import Produkt
# Create your views here.


def add_prod(request):
    if request.method == "POST":
        Name = request.POST.get("Name")
        Price = request.POST.get("Price")


        produkt = Produkt(
            Name = Name,
            Price = Price,
        )
        produkt.save()

        return redirect("table_prod")

    return render(request, 'add_prod.html')


def table_prod(request):
    produkty = Produkt.objects.all()
    return render(request, 'table_prod.html', {'produkty': produkty})

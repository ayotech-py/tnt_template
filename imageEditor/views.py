from django.http import HttpResponse
from django.shortcuts import render
from .forms import PropertyForm
from PIL import Image
import urllib.request
from .edit import *


def image_editor(request):
    return HttpResponse("""
                        <h1>Auction Link</h1>
                        <h2><a href="auction">Auction Editing</a></h2>
                        <h1>Property Link</h1>
                        <h2><a href="property">Property Editing</a></h2>
                        <h1>Amend Link</h1>
                        <h2><a href="amend">Amending Auctions</a></h2>
                        """)


def property_image(request):
    if request.method == "POST":
        property_form = PropertyForm(request.POST, request.FILES)
        if property_form.is_valid():
            logo = property_form.cleaned_data['logo']
            big_card_img = property_form.cleaned_data['big_card_img']
            card_01_img = property_form.cleaned_data['card_01_img']
            card_02_img = property_form.cleaned_data['card_02_img']
            card_03_img = property_form.cleaned_data['card_03_img']
            about_property = property_form.cleaned_data['about_property']
            location = property_form.cleaned_data['location']
            price = property_form.cleaned_data['price']
            option = property_form.cleaned_data['option']
            property_form.save()
            img_files = property_form.instance
            print(img_files.big_card_img.url)

        template = Image.open("projectfiles/Bgr_img.jpg")
        template = template.resize((2451, 3255))

        img_url = "http://127.0.0.1:2222/media/"+img_files.big_card_img.url
        urllib.request.urlretrieve(img_url, "img.jpeg")
        template = template_image(template=template, big_card_img="img.jpeg")
        template.show()

    else:
        property_form = PropertyForm()
        return render(request, 'property.html', {'form': property_form})

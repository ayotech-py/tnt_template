from django.http import HttpResponse
from django.shortcuts import render
from .forms import PropertyForm
from PIL import Image
import urllib.request
import requests
from io import BytesIO
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
        #img_files = "hello"
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

        app_url = "https://ayotech-tnt-template.onrender.com"

        bgr_img_url = app_url+img_files.big_card_img.url
        print(bgr_img_url)
        response = requests.get(bgr_img_url, stream=True).raw
        print(response)
        template = template_image(
            template=template, big_card_img=response)

        print(template)

        price_h = 0
        if "sale" in option:
            content = "projectfiles/content_img_png.png"
            price_h = 1760
        elif "rent" in option:
            content = "projectfiles/rent_img_png.png"
            price_h = 1720

        template = content_image(template=template, content_img=content)

        if logo:
            logo_img_url = app_url+img_files.logo.url
            logo_res = requests.get(logo_img_url, stream=True).raw
            template = logo_image(template=template, logo=logo_res)

        else:
            template = logo_image(
                template=template, logo="projectfiles/logo.jpg")

        card_01_url = app_url+img_files.card_01_img.url
        card_01_res = requests.get(card_01_url, stream=True).raw
        card_02_url = app_url+img_files.card_02_img.url
        card_02_res = requests.get(card_02_url, stream=True).raw
        card_03_url = app_url+img_files.card_03_img.url
        card_03_res = requests.get(card_03_url, stream=True).raw

        template = card_image(
            template=template, card_01=card_01_res, card_02=card_02_res, card_03=card_03_res)

        template = detail_texts(
            template=template, about_property=about_property, location=location, price=price, price_h=price_h)

        template.save("media/property.jpeg")
        print(template)
        template_url = app_url+"/media/property.jpeg"
        property_form = PropertyForm()
        return render(request, 'property.html', {'form': property_form, "picture": template_url})

    else:
        property_form = PropertyForm()
        return render(request, 'property.html', {'form': property_form})

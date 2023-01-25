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
        for field in property_form:
            print(field.errors)
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

        bgr_img_url = "http://127.0.0.1:8000"+img_files.big_card_img.url
        print(bgr_img_url)
        urllib.request.urlretrieve(bgr_img_url, "img.jpeg")
        template = template_image(template=template, big_card_img="img.jpeg")

        price_h = 0
        if "sale" in option:
            content = "projectfiles/content_img_png.png"
            price_h = 1760
        elif "rent" in option:
            content = "projectfiles/rent_img_png.png"
            price_h = 1720

        template = content_image(template=template, content_img=content)

        if logo:
            logo_img_url = "http://127.0.0.1:8000"+img_files.logo.url
            urllib.request.urlretrieve(logo_img_url, "logo.jpeg")
            template = logo_image(template=template, logo="logo.jpeg")

        else:
            template = logo_image(
                template=template, logo="projectfiles/logo.jpg")

        card_01_url = "http://127.0.0.1:8000"+img_files.card_01_img.url
        urllib.request.urlretrieve(card_01_url, "card_01")
        card_02_url = "http://127.0.0.1:8000"+img_files.card_02_img.url
        urllib.request.urlretrieve(card_02_url, "card_02")
        card_03_url = "http://127.0.0.1:8000"+img_files.card_03_img.url
        urllib.request.urlretrieve(card_03_url, "card_03")

        template = card_image(
            template=template, card_01="card_01", card_02="card_02", card_03="card_03")

        template = detail_texts(
            template=template, about_property=about_property, location=location, price=price, price_h=price_h)

        template.save("media/property.jpeg")
        print(template)
        template_url = "http://127.0.0.1:8000/media/property.jpeg"
        property_form = PropertyForm()
        return render(request, 'property.html', {'form': property_form, "picture": template_url})

    else:
        property_form = PropertyForm()
        return render(request, 'property.html', {'form': property_form})

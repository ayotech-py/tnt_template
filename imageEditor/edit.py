from PIL import Image, ImageFont, ImageDraw
import textwrap

template = Image.open("projectfiles/Bgr_img.jpg")
b_img = "projectfiles/banner.jpeg"
content = "projectfiles/content_img_png.png"
card01 = "projectfiles/card01.jpeg"
card02 = "projectfiles/card02.jpeg"
card03 = "projectfiles/card03.jpeg"


def p_align_text(astr, font, MAX_W, im):
    para = textwrap.wrap(astr, width=14)
    draw = ImageDraw.Draw(im)
    if len(astr) <= 30:
        text_h = 2020
    elif len(astr) <= 71:
        text_h = 2020
    elif len(astr) <= 108:
        text_h = 2020
    else:
        text_h = 2050
    print(len(astr))
    current_h, pad = text_h, 0
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text((MAX_W, current_h), line, font=font, fill="white")
        current_h += h + pad
    return im


def template_image(template, big_card_img):
    img = Image.open(big_card_img)
    img_w, img_h = img.size
    new_img_h = int((img_h * 2451) / img_w)
    if new_img_h < 1800:
        new_img_h = 1800
    else:
        pass
    new_img = img.resize((2451, new_img_h))
    template.paste(new_img, (0, 0))
    return template


def content_image(template, content_img):
    img = Image.open(content_img)
    img_w, img_h = img.size
    new_img_h = int((img_h * 2451) / img_w)
    new_img = img.resize((2451, new_img_h))
    bottom = 3255 - new_img_h
    template.paste(new_img, (0, bottom), new_img)
    return template


def card_image(template, card_01, card_02, card_03):
    pic_w_list = [118, 800, 1485]
    pic_list = [card_01, card_02, card_03]
    for i in range(3):
        img = Image.open(pic_list[i])
        new_img = img.resize((570, 400))
        template.paste(new_img, (pic_w_list[i], 2465))
    return template


def detail_texts(template, about_property, location, price):
    font = ImageFont.truetype("projectfiles/Comic.ttf", 100)
    price_font = ImageFont.truetype("projectfiles/Comic.ttf", 61)
    abt_p_loc_w = 70
    abt_p_loc_h = 2000

    img_text = p_align_text(astr=about_property.upper(), font=font,
                            MAX_W=abt_p_loc_w, im=template)
    img_text.show()


template = template_image(template=template, big_card_img=b_img)
template = content_image(template=template, content_img=content)
template = card_image(template=template, card_01=card01,
                      card_02=card02, card_03=card03)
detail_texts(template=template, about_property="4bedroom Terrace House for sale",
             location="fdfdf", price="12million")

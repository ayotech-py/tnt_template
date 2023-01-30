from PIL import Image, ImageFont, ImageDraw
import textwrap

app_url = '/home/aaayotech/tnt_template'

def p_align_text(astr, font, MAX_W, im):
    para = textwrap.wrap(astr, width=22)
    draw = ImageDraw.Draw(im)
    if len(astr) <= 52:
        text_h = 2050
    else:
        text_h = 2020

    current_h, pad = text_h, 0
    for line in para:
        w, h = draw.textsize(line, font=font)
        draw.text((MAX_W, current_h), line, font=font, fill=(0, 0, 0, 0))
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


def logo_image(template, logo):
    logo = Image.open(logo)
    logo_w, logo_h = logo.size
    tmp_h = 200
    tmp_w = int((tmp_h * logo_w) / logo_h)
    logo = logo.resize((tmp_w, tmp_h))
    template_w, template_h = template.size
    left_x = int((template_w - tmp_w) / 2)
    template.paste(logo, (left_x, 80))
    return template


def card_image(template, card_01, card_02, card_03):
    pic_w_list = [118, 800, 1485]
    pic_list = [card_01, card_02, card_03]
    for i in range(3):
        img = Image.open(pic_list[i])
        new_img = img.resize((570, 400))
        template.paste(new_img, (pic_w_list[i], 2465))
    return template


def detail_texts(template, about_property, location, price, price_h):
    font = ImageFont.truetype(app_url+"/projectfiles/Comic.ttf", 80)
    price_font = ImageFont.truetype(app_url+"/projectfiles/LeagueSpartan-Bold.otf", 100)
    abt_p_loc_w = 70
    location_w = 850

    img_text = p_align_text(astr=about_property.title(), font=font,
                            MAX_W=abt_p_loc_w, im=template)

    img_text = p_align_text(astr=location.title(), font=font,
                            MAX_W=location_w, im=img_text)
    draw = ImageDraw.Draw(img_text)
    draw.text((1400, price_h), price.upper(), font=price_font, fill=(180, 0, 36, 160))

    return img_text

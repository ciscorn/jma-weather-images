from PIL import Image


WIDTH = 150
HEIGHT = 90


BASE_IMAGES = {
    'sun': Image.open('srcimgs/sun.png'),
    'cloud': Image.open('srcimgs/cloud.png'),
    'rain': Image.open('srcimgs/rain.png'),
    'snow': Image.open('srcimgs/snow.png'),
    'mist': Image.open('srcimgs/mist.png'),
    'rain_thunder': Image.open('srcimgs/rain_thunder.png'),
    'snow_thunder': Image.open('srcimgs/snow_thunder.png'),
    'rain_heavy': Image.open('srcimgs/rain_heavy.png'),
    'snow_heavy': Image.open('srcimgs/snow_heavy.png'),
    'rain_wind': Image.open('srcimgs/rain_wind.png'),
    'snow_wind': Image.open('srcimgs/snow_wind.png'),
    'rain_heavy_wind': Image.open('srcimgs/rain_heavy_wind.png'),
    'rain_or_snow': Image.open('srcimgs/rain_and_snow.png'),
    'snow_or_rain': Image.open('srcimgs/rain_and_snow.png'),
    'rain_and_snow': Image.open('srcimgs/rain_and_snow.png'),
    'night_fair': Image.open('srcimgs/fair_night.png'),
}

MOD_TR_IMG = Image.open('srcimgs/tr.png')


def composite(src, dst, pos, size=None):
    layer = Image.new('RGBA', dst.size, (0, 0, 0, 0))
    if size:
        src = src.resize(size, Image.ANTIALIAS)
    layer.paste(src, pos)
    return Image.composite(layer, dst, layer)


def make_one(weather):
    out = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 0))
    img1 = BASE_IMAGES[weather]
    left = int((WIDTH - HEIGHT) / 2)
    return composite(img1, out, (left, 0), (HEIGHT, HEIGHT))


def make_two(weather_from, weather_to):
    out = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 0))
    img1 = BASE_IMAGES[weather_to]
    out = composite(img1, out, (WIDTH - HEIGHT, 0), (HEIGHT, HEIGHT))
    img2 = BASE_IMAGES[weather_from]
    out = composite(img2, out, (0, 0), (HEIGHT, HEIGHT))
    return out


def draw_modifier(mod, img):
    left = int((WIDTH - HEIGHT) / 2)
    if mod == "tr":
        return composite(MOD_TR_IMG, img, (left, 0), (HEIGHT, HEIGHT))
    else:
        return img


def make_weather_image(spec):
    b = spec.get('b')
    m = spec.get('m')
    t = spec.get('t')

    if t:
        img = make_two(b, t)
    else:
        img = make_one(b)

    if m:
        img = draw_modifier(m, img)

    return img


import json
with open('codes.json', encoding='utf-8') as f:
    data = json.load(f)
    for code, spec in data.items():
        make_weather_image(spec).save("output/" + code + '.png')

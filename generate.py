import sys
from PIL import Image


WIDTH = 260
HEIGHT = 145
COLORMODE = "RGBA"
EXTENSION = ".png"

srcdir = sys.argv[1]


BASE_IMAGES = {
    'sun': Image.open(f'{srcdir}/sun.png'),
    'cloud': Image.open(f'{srcdir}/cloud.png'),
    'rain': Image.open(f'{srcdir}/rain.png'),
    'snow': Image.open(f'{srcdir}/snow.png'),
    'mist': Image.open(f'{srcdir}/mist.png'),
    'rain_thunder': Image.open(f'{srcdir}/rain_thunder.png'),
    'snow_thunder': Image.open(f'{srcdir}/snow_thunder.png'),
    'rain_heavy': Image.open(f'{srcdir}/rain_heavy.png'),
    'snow_heavy': Image.open(f'{srcdir}/snow_heavy.png'),
    'rain_wind': Image.open(f'{srcdir}/rain_wind.png'),
    'snow_wind': Image.open(f'{srcdir}/snow_wind.png'),
    'rain_heavy_wind': Image.open(f'{srcdir}/rain_heavy_wind.png'),
    'rain_or_snow': Image.open(f'{srcdir}/rain_and_snow.png'),
    'snow_or_rain': Image.open(f'{srcdir}/rain_and_snow.png'),
    'rain_and_snow': Image.open(f'{srcdir}/rain_and_snow.png'),
    'night_fair': Image.open(f'{srcdir}/fair_night.png'),
}

MOD_TR_IMG = Image.open(f'{srcdir}/tr.png')


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


def make_two(weather_from, mod, weather_to):
    out = Image.new('RGBA', (WIDTH, HEIGHT), (255, 255, 255, 0))
    img1 = BASE_IMAGES[weather_to]
    d = 0 if mod == "tr" else HEIGHT // 8
    out = composite(img1, out, (WIDTH - HEIGHT + d//2, d), (HEIGHT-2*d, HEIGHT-2*d))
    img2 = BASE_IMAGES[weather_from]
    out = composite(img2, out, (d+d//2, 0), (HEIGHT, HEIGHT))
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
        img = make_two(b, m, t)
    else:
        img = make_one(b)

    if m:
        img = draw_modifier(m, img)

    return img


import json
with open('codes.json', encoding='utf-8') as f:
    data = json.load(f)
    for code, spec in data.items():
        make_weather_image(spec).convert(COLORMODE).save("output/" + code + EXTENSION, quality=95)

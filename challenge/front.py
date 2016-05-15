import io
import random

from flask import send_file
from PIL import ImageDraw, ImageColor

from . import app
from .challenge1 import text_to_image


@app.route("/")
def index():
    return send_file("index.html")


@app.route("/straight/<text>")
def straight(text):
    image = io.BytesIO()
    text_to_image(text, height=30).save(image, format="PNG")
    image.flush()
    image.seek(0)

    return send_file(image,
                     attachment_filename=u"{}.png".format(text),
                     mimetype="image/png")


@app.route("/rotate/<text>/<int:degree>")
def rotate(text, degree):
    image = io.BytesIO()
    text_to_image(text, height=30).rotate(degree, expand=1).save(image, format="PNG")
    image.flush()
    image.seek(0)

    return send_file(image,
                     attachment_filename=u"{}.png".format(text),
                     mimetype="image/png")


@app.route("/cross/<text>/<int:number>")
def cross(text, number):
    output = io.BytesIO()
    image = text_to_image(text, size=5, height=60)
    width, height = image.size
    draw = ImageDraw.Draw(image)
    for _ in xrange(number):
        draw.line((0, random.randint(0, height), width, random.randint(0, height)), fill=128, width=3)
    image.save(output, format="PNG")
    output.flush()
    output.seek(0)

    return send_file(output,
                     attachment_filename=u"{}.png".format(text),
                     mimetype="image/png")

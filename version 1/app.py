import os

from flask import Flask, request, render_template, send_from_directory

__author__ = 'narmada'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("search.html")


@app.route("/search", methods=["POST"])
def search():
    search_text = request.form['search_place']
    print('search text: ', search_text)

    search_loc = os.path.join(search_text, 'real')
    generated_loc = os.path.join(search_text, 'fake')

    real_imgs = os.listdir(os.path.join(search_text, 'real'))
    fake_imgs = os.listdir(generated_loc)

    return render_template("search.html", image_names=real_imgs, fake_images=fake_imgs, loc=search_loc, fake_loc=generated_loc, location=search_text)


@app.route('/<loc>/<filename>')
def send_image_real(filename, loc):
    return send_from_directory(loc, filename)


@app.route('/<fake_loc>/<filename>')
def send_image_fake(filename, fake_loc):
    return send_from_directory(fake_loc, filename)


if __name__ == "__main__":
    app.run(port=4555, debug=True)

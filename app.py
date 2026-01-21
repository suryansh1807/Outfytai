# from flask import Flask, render_template, request
# from genai import generate_outfit_suggestion
# from mltagging import tag_clothing_image
# import os


# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('home.html')

# @app.route('/about')
# def about():
#     return render_template('aboutus.html')

# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     if request.method == "POST":
#         files = request.files.getlist("images")

#         wardrobe_summary = ""

#         for file in files:
#             path = os.path.join("uploads", file.filename)
#             file.save(path)

#             tags = tag_clothing_image(path)
#             wardrobe_summary += f"{file.filename}: {tags}\n"

#         suggestion = generate_outfit_suggestion(wardrobe_summary)

#         return render_template("upload.html", suggestion=suggestion)

#     return render_template("upload.html")
# if __name__ == '__main__':
#     app.run(debug=True,port=5050)

from flask import Flask, render_template, request
import os

from genai import generate_outfit_cards
from mltagging import tag_clothing_image

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        files = request.files.getlist("images")

        wardrobe_summary = ""

        for file in files:
            from werkzeug.utils import secure_filename
            filename = secure_filename(file.filename)
            path = os.path.join(UPLOAD_FOLDER, filename)

            file.save(path)

            tags = tag_clothing_image(path)
            wardrobe_summary += f"{file.filename}: {tags}\n"

        outfits = generate_outfit_cards(wardrobe_summary)

        return render_template("upload.html", outfits=outfits)

    return render_template("upload.html")

if __name__ == "__main__":
    app.run(debug=True)

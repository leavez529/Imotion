from app import app
from flask import render_template, request, Flask
# from server.image_captioning import image2caption
# from server.text_to_emotion.txt_to_emo import txt_to_emo

emotion = 'PUT YOUR EMOTION HERE'

@app.route("/", methods=["POST", "GET"])
def image2emotion():
    if request.method == "POST":
        img = request.form.get("img")
        print(img)
        # img_caption = image2caption(img)
        # emotion = txt_to_emo(img_caption)
        # TODO: Put caption to emotion-box in index.html
        emotion = img
    return render_template("index.html", title="Imotion", emotion=emotion)

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title="Imotion", emotion=emotion)

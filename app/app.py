from flask import Flask, render_template, request
import os

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template("upload.html")
@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'static/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for upload_file in request.files.getlist('file'):
        print(upload_file)
        filename = upload_file.filename
        destination = "/".join([target, filename])
        print(destination)
        upload_file.save(destination)

    return render_template("complete.html", image=filename)


@app.route("/mail")
def send_mail():
   msg = Message('Hello', sender='bitruschoji4real@gmail.com', recipients = ['kimkazong@gmail.com'])
   msg.body = "Hello Flask message sent from Flask-Mail"
   mail.send(msg)
   return "Sent"


if __name__ == "__main__":
    app.run(debug=True)
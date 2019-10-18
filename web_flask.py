from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    a = 3
    b = 4
    c = a + b
    return 'This is home page, '+str(c)


@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)


if __name__ == "__main__":
    app.run()
else:
    print("Server launch fail.")
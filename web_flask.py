from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    a = 3
    b = 4
    c = a + b
    return 'This is home page, '+str(c)


if __name__ == "__main__":
    app.run()
else:
    print("Server launch fail.")
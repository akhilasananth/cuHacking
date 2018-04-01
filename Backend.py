from flask import Flask
from Compare import compare

app = Flask(__name__)

@app.route('/')
def res():
    compare()
    


if __name__ == '__main__':
    app.run()

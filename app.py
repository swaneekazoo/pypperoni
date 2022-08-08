from flask import Flask, render_template
import xmltodict

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return 'index'


@app.route('/scores')
def scores():  # put application's code here
    f = open('data/cases.xml', mode='rb')
    o = xmltodict.parse(f.read())
    f.close()
    return o


if __name__ == '__main__':
    app.run()

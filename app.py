from flask import Flask, render_template
import xmltodict

app = Flask(__name__)


@app.route('/')
def index():
    return 'index'


@app.route('/scores')
def scores():
    f = open('data/cases.xml', mode='rb')
    o = xmltodict.parse(f.read())
    f.close()
    return o


if __name__ == '__main__':
    app.run()

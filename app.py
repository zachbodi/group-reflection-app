from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker

app = Flask(__name__, template_folder='templates')
Bootstrap(app)
colorpicker(app)

@app.route('/')
def home():
    return render_template('index.html', test='abc', color='#a000a0')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

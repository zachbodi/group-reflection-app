from flask import Flask, render_template, escape, redirect, request
from flask_bootstrap import Bootstrap
from flask_colorpicker import colorpicker
from datetime import datetime
import uuid
import json
import os
import random

app = Flask(__name__, template_folder='templates')
Bootstrap(app)
colorpicker(app)

@app.route('/')
def home():
    try:
        thoughts = os.listdir('thoughts')
        filename = random.choice(thoughts)
        
        with open('thoughts/{}'.format(filename)) as f:
            data = f.read()

        thought_info = json.loads(data)
        thought, color = thought_info['thought'], thought_info['color']

    except IndexError:
        thought, color = 'I got an internship I\'m hyped for!', '#ff4500'

    return render_template('index.html', thought=thought, color=color)

@app.route('/submit', methods=['POST'])
def submit():
    thought, color = escape(request.form['thought']), escape(request.form['color'])

    thought_filename = str(uuid.uuid4())

    with open('thoughts/{}'.format(thought_filename), 'w') as f:
        f.write(json.dumps({'thought': thought, 'color': color, 'stamp': str(datetime.now())}))

    return redirect('/')

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port='8080')

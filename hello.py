# -*- coding: utf-8 -*-
# Hey, little fatty

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'hello world'

@app.route('/item/<id>')
def item(id):
    return 'item: {}'.format(id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)

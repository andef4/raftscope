from bottle import request, route, run, template
import os

@route('/', method='POST')
def index():
    filename = request.forms.get('filename')
    svg = request.forms.get('svg')
    if not filename:
        return ''

    if not os.path.exists(filename):
        os.mkdir(filename)

    files = os.listdir(filename)
    if files:
        files = [int(f.split('.')[0]) for f in files]
        new_filename = sorted(files)[-1] + 1
    else:
        new_filename = 1
    with open('{}/{}.svg'.format(filename, new_filename), 'w') as f:
        f.write(svg)

    return ''

run(host='localhost', port=3000)

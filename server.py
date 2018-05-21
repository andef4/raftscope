from bottle import request, route, run, template
import os
import lxml.etree as et

@route('/', method='POST')
def index():
    filename = request.forms.get('filename')
    svg = request.forms.get('svg')
    save_data = request.forms.get('saveData') == 'true'
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

    with open('svg-style.css') as f:
        style = f.read()

    svg = svg.replace('<defs>', style + '<defs>')

    xml = et.fromstring(svg)
    if not save_data:
        logs = xml.find('.//{http://www.w3.org/2000/svg}g[@class="logs"]')
        logs.getparent().remove(logs)
    svg = et.tostring(xml)

    with open('{}/{}.svg'.format(filename, new_filename), 'w') as f:
        f.write(svg)

    os.system('svgo {}/{}.svg --enable=inlineStyles  --config \'{{ "plugins": [ {{ "inlineStyles": {{ "onlyMatchedOnce": false }} }}] }}\''.format(filename, new_filename))

    return ''

run(host='localhost', port=3000, reloader=True)

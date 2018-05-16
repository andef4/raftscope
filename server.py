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
    #output_dir = filename + '-scaled'
    #if not os.path.exists(output_dir):
    #    os.mkdir(output_dir)

    files = os.listdir(filename)
    if files:
        files = [int(f.split('.')[0]) for f in files]
        new_filename = sorted(files)[-1] + 1
    else:
        new_filename = 1

    with open('svg-style.css') as f:
        style = f.read()

    if not save_data:
        svg = svg.replace('<defs>', style + '<defs>')
        xml = et.fromstring(svg)
        logs = xml.find('.//{http://www.w3.org/2000/svg}g[@class="logs"]')
        logs.getparent().remove(logs)
        svg = et.tostring(xml)

    with open('{}/{}.svg'.format(filename, new_filename), 'w') as f:
        f.write(svg)

    #os.system('inkscape -D -z --file={}/{}.svg --export-png={}/{}.png'.format(
    #    filename, new_filename, output_dir, new_filename
    #))

    return ''

run(host='localhost', port=3000, reloader=True)

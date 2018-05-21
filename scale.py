import os
import sys
import shutil
import re

def main():
    if len(sys.argv) != 2:
        print('Usage: python scale.py <directory>')

    input_dir = sys.argv[1].rstrip(os.path.sep)
    output_dir = input_dir + '-scaled'
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.mkdir(output_dir)

    files = sorted(os.listdir(input_dir))
    for f in files:
        os.system('inkscape -D -z --file={} --export-pdf={} --export-latex'.format(
            os.path.join(input_dir, f),
            os.path.join(output_dir, f.replace('svg', 'pdf'))
        ))

        output_file = os.path.join(output_dir, f.replace('svg', 'pdf_tex'))
        with open(output_file) as f:
            text = f.read()

        for match in re.finditer(r'\\put\(\d\.\d{8},(\d\.\d{8})\)', text):
            x = float(match.group(1))
            x -= 0.02
            if x < 0:
                x = '{0:.7f}'.format(x)
            else:
                x = '{0:.8f}'.format(x)
            text = text[:match.start(1)] + x + text[match.end(1):]

        text = re.sub(r'(\d+.pdf)', input_dir + r'/\1', text)

        with open(output_file, 'w') as f:
            f.write(text)


if __name__ == '__main__':
    main()

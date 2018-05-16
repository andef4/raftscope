import os
import sys
import shutil

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

if __name__ == '__main__':
    main()

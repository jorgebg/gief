import argparse
import os

from .gief import __doc__, app


parser = argparse.ArgumentParser(prog='gief', description=__doc__)

parser.add_argument('path', nargs='?', default=os.getcwd(),
                    help='Folder where files will be uploaded to (CWD by default)')
parser.add_argument('-H', '--host', default='0.0.0.0')
parser.add_argument('-p', '--port', type=int, default=5000)

args = parser.parse_args()
app.config['path'] = args.path
app.run(args.host, args.port)

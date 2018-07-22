__author__ = 'George Stepiko'
from model.record import Record
import random
import string
import os.path
import jsonpickle
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['records count', 'target file'])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/records.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = str(a)


def random_string(prefix, maxlength, phone=False):
    symbols = string.digits + ' +-()asd' if phone else string.ascii_letters + string.digits  # + ' '*10
    # fixme: work with multi-space
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [
   Record(
       firstname=random_string('firstname', 10),
       lastname=random_string('lastname', 10),
       home=random_string('', 10, phone=True),
       email=random_string('n', 10)+'@'+random_string('d', 8)+'.morg',
       address=random_string('address: ', 50),
       bmonth=random.randrange(13),
   )
   for i in range(5)
] + \
[
    Record()
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as outfile:
    # in my implementation Group object has no __dict__ so build dictionary by myself
    jsonpickle.set_encoder_options('json', indent=2)
    outfile.write(jsonpickle.encode(testdata))
    # outfile.write(json.dumps(testdata, default=lambda x: {s: getattr(x, s, None) for s in x.__slots__}, indent=2))

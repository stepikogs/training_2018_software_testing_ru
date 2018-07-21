__author__ = 'George Stepiko'
from model.group import Group
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], 'n:f:', ['groups count', 'target file'])
except getopt.GetoptError as err:
    print(err)
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/group.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = str(a)


def random_string(prefix, maxlength):
    symbols = string.ascii_letters + string.digits  # + ' '*10 fixme: work with multi-space
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlength))])


testdata = [
    # Group(group_name="testgroup",                    # full group
    #       group_header="testheader",
    #       group_footer="testfooter"),
    Group(),                                         # default group
    # Group(group_name="name_assigned",                # group with invalid input
    #       jeegurda='incorrect',
    #       group_header='header_assigned'),
    # Group(group_name="",                             # group with empty values
    #       group_header="",
    #       group_footer="")
    ] + [
    Group(group_name=random_string('name', 10),      # group with random values
          group_footer=random_string('footer', 10),
          group_header=random_string('header', 10))
    for i in range(n)                                # 5 random groups in total
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
with open(file, 'w') as outfile:
    # in my implementation Group object has no __dict__ so build dictionary by myself
    outfile.write(json.dumps(testdata, default=lambda x: {s: getattr(x, s, None) for s in x.__slots__}, indent=2))

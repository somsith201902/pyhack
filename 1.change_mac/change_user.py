# ປ້ອນ username ໂດຍໃຊ້ subprocess + optparse ແລ້ວ login ໂດຍໃຊ້ຄຳສັ່ງ su

from subprocess import *
from optparse import *

# function get arguments
def get_arguments():
    parser = OptionParser()
    parser.add_option("-u","--username", dest="username", help="your Username")
    (options, arguments) = parser.parse_args()
    return options

def login(username):
    call(["su", username])

options = get_arguments()
login(options.username)

     
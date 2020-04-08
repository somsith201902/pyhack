from optparse import *
from subprocess import *

def get_arguments():
    parser = OptionParser()
    parser.add_option("-n", "--name", dest="name", help="Your name")
    parser.add_option("-a", "--age", dest="age", help="your age")
    (options, arguments) = parser.parse_args()
    if not options.name:
        options.error("[-] Please input name")
    if not options.age:
        options.error("[-] Please input age")
    return options

def show_info(name, age):
    print(f"My name is {name} and your {age} years old")


def login(username, password):
    if (username == "admin") and (password == "admin"):
        print("login Success!")
    else:
        print("xxxxinvalid userxxxx")
    
#value in options contain in here
options = get_arguments()

# show_info(options.name, options.age)
login(options.name, options.age)

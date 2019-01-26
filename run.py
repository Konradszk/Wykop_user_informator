import sys

from main import main

argv = sys.argv
if len(argv) < 2:
    print('Enter user name as command line argument', file=sys.stderr)
    sys.exit()

username = argv[1]
url = "https://www.wykop.pl/ludzie/{0}/strona/".format(username)
main(url, username)

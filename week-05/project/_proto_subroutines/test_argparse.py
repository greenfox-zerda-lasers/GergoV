import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-l', '--list', action='store_true', help='List todo items')
parser.add_argument('-a', '--add', action='store_true', help='Add item')
parser.add_argument('-r', '--remove', action='store_true', help='Remove item')
parser.add_argument('-c', '--check', action='store_true', help='Mark item checked')
args = parser.parse_args()
if args.list:
    print('Listing items')
if args.add:
    print('Add item')
if args.remove:
    print('Remove item')
if args.check:
    print('Check item')

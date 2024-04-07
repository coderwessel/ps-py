import argparse
from art import text2art

parser = argparse.ArgumentParser(
		description			= "PS> python %(prog)s piet, calls out piet",
		epilog				= '',
		add_help			= True
	)
parser.add_argument('--version', action='version', version='%(prog)s 0.001')
parser.add_argument('name', nargs='?')
args = parser.parse_args()

if args.name==None:
    name = input("Enter your name: ")
else:
    name=args.name
print(text2art("Hello, " + name))        


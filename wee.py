import argparse, sys

parser = argparse.ArgumentParser(description='WeeChat Cheatsheet')
parser.add_argument('pos', help="action that you need!")

if len(sys.argv) < 2:
    parser.print_help()
else:    
    arg = parser.parse_args()

    if arg.pos == 'swap_buffer':
        print('Ctrl-n')
    elif arg.pos == 'swap_window':
        print('F7')
    elif arg.pos == 'split_window':
        print('> /window splith\n> /window splitv')


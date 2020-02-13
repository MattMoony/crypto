import os
import re

def list_algorithms():
    bp = os.path.dirname(os.path.realpath(__file__))
    return [ {'name': x, 'complete': False if not os.path.isfile(os.path.join(bp, x, 'complete')) else bool(open(os.path.join(bp, x, 'complete')).read())} for x in os.listdir(bp) if os.path.isdir(os.path.join(bp, x)) and not re.match(r'^[\._].*$', x) ]

def main():
    print('''
                                           /$$              
                                          | $$              
  /$$$$$$$  /$$$$$$  /$$   /$$  /$$$$$$  /$$$$$$    /$$$$$$ 
 /$$_____/ /$$__  $$| $$  | $$ /$$__  $$|_  $$_/   /$$__  $$
| $$      | $$  \__/| $$  | $$| $$  \ $$  | $$    | $$  \ $$
| $$      | $$      | $$  | $$| $$  | $$  | $$ /$$| $$  | $$
|  $$$$$$$| $$      |  $$$$$$$| $$$$$$$/  |  $$$$/|  $$$$$$/
 \_______/|__/       \____  $$| $$____/    \___/   \______/ 
                     /$$  | $$| $$                          
                    |  $$$$$$/| $$                          
                     \______/ |__/                          
    ''')

    print('\nAlgorithms:\n-----------')
    print(' done?\tname')
    print('\n'.join(' {}\t '.format('✅' if d['complete'] else '❌') + d['name'] for d in list_algorithms()))
    print()

if __name__ == '__main__':
    main()
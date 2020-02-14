import os
from string import ascii_lowercase

class CaesarCipher(object):
    def __init__(self, shift, d=ascii_lowercase):
        self.shift = shift
        self.d = d if d else ascii_lowercase

    def __shift(self, c):
        if c in self.d.lower():
            return self.d.lower()[(self.d.lower().index(c)+self.shift)%len(self.d)]
        elif c in self.d.upper():
            return self.d.upper()[(self.d.upper().index(c)+self.shift)%len(self.d)]
        return c

    def __unshift(self, c):
        if c in self.d.lower():
            return self.d.lower()[(self.d.lower().index(c)-self.shift)%-len(self.d)]
        elif c in self.d.upper():
            return self.d.upper()[(self.d.upper().index(c)-self.shift)%-len(self.d)]
        return c

    def enc(self, msg):
        return ''.join([ self.__shift(c) for c in msg ])

    def dec(self, msg):
        return ''.join([ self.__unshift(c) for c in msg ])

    def pwn(self, msg, keywords=None, lang=None):
        if not keywords and not lang:
            raise Exception('Missing keywords / lang.')
        if lang:
            keywords = keywords if keywords else []
            with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', '__dicts', '{}.txt'.format(lang)), 'rb') as f:
                keywords += [ l.decode('utf-8').strip().lower() for l in f.readlines() ]
        matches = []
        for shift in range(1, 26):
            self.shift = shift
            dec = self.dec(msg)
            if any([ w.lower() in keywords for w in dec.split(' ') ]):
                matches.append((shift, dec))
        return matches

def main():
    print('''
........................................................................................................
..%%%%....%%%%...%%%%%%...%%%%....%%%%...%%%%%............%%%%...%%%%%%..%%%%%...%%..%%..%%%%%%..%%%%%..
.%%..%%..%%..%%..%%......%%......%%..%%..%%..%%..........%%..%%....%%....%%..%%..%%..%%..%%......%%..%%.
.%%......%%%%%%..%%%%.....%%%%...%%%%%%..%%%%%...........%%........%%....%%%%%...%%%%%%..%%%%....%%%%%..
.%%..%%..%%..%%..%%..........%%..%%..%%..%%..%%..........%%..%%....%%....%%......%%..%%..%%......%%..%%.
..%%%%...%%..%%..%%%%%%...%%%%...%%..%%..%%..%%...........%%%%...%%%%%%..%%......%%..%%..%%%%%%..%%..%%.
........................................................................................................
    ''')

    import os
    from argparse import ArgumentParser
    import colorama as clr
    clr.init()
    parser = ArgumentParser('Caesar Cipher')

    parser.add_argument('-d', action='store_true', dest='dec', help='[flag] decrypt')
    parser.add_argument('-e', action='store_true', dest='enc', help='[flag] encrypt')
    parser.add_argument('-p', action='store_true', dest='pwn', help='[flag] pawn / break')
    parser.add_argument('-s', type=int, dest='shift', help='Shift value', default=8)
    parser.add_argument('-a', type=str, dest='alphabet', help='Alphabet')
    parser.add_argument('--keywords', type=str, dest='keywords', help='Keywords separated by `,`')
    parser.add_argument('--lang', type=str, dest='lang', help='Target language')
    parser.add_argument('msg', help='Message')

    args = parser.parse_args()

    if not (bool(args.dec) ^ bool(args.enc) ^ bool(args.pwn)):
        print(clr.Fore.RED + '[-] Invalid parameters: Please provide either `dec`, `enc` or `pwn` flag!' + clr.Fore.RESET)
        os._exit(1)

    cipher = CaesarCipher(args.shift, args.alphabet)
    if args.dec or args.enc:
        res = cipher.enc(args.msg) if args.enc else cipher.dec(args.msg)
        print('[+] {} mesage: {}{}'.format('Encrypted' if args.enc else 'Decrypted', clr.Fore.GREEN, res))
    else:
        if not args.keywords and not args.lang:
            print(clr.Fore.RED + '[-] Invalid parameters: Missing `keywords` / `lang`!' + clr.Fore.RESET)
            os._exit(1)
        matches = cipher.pwn(args.msg, args.keywords.split(',') if args.keywords else None, args.lang)
        print('[+] Pwn result: ')
        print('\n'.join([ ' |- {}{:02d}{} --> {}{}'.format(clr.Fore.LIGHTBLACK_EX, m[0], clr.Fore.RESET, clr.Fore.LIGHTBLUE_EX, m[1]) 
                + clr.Fore.RESET for m in matches ]))

    print()

if __name__ == '__main__':
    main()
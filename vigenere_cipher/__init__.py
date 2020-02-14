from string import ascii_lowercase

class VigenereCipher(object):
    def __init__(self, key, d=ascii_lowercase):
        self.key = key.lower()
        self.d = ((d if d else ascii_lowercase) * 2).lower()

    def encipherc(self, i, c):
        ret = self.d[self.d.index(c.lower()):][self.d.index(self.key[i])]
        if c in self.d.lower():
            return ret
        else:
            return ret.upper()

    def enc(self, msg):
        return ''.join([ self.encipherc(i%len(self.key), c) for i, c in enumerate([ l for l in msg if l.lower() in self.d ]) ])

    def decipherc(self, i, c):
        ret = self.d[self.d[self.d.index(self.key[i]):].index(c.lower())]
        if c in self.d.lower():
            return ret
        else:
            return ret.upper()
        
    def dec(self, msg):
        return ''.join([ self.decipherc(i%len(self.key), c) for i, c in enumerate([ l for l in msg if l.lower() in self.d ]) ])

def main():
    print('''
........................................................................................................................
.%%..%%..%%%%%%...%%%%...%%%%%%..%%..%%..%%%%%%..%%%%%...%%%%%%...........%%%%...%%%%%%..%%%%%...%%..%%..%%%%%%..%%%%%..
.%%..%%....%%....%%......%%......%%%.%%..%%......%%..%%..%%..............%%..%%....%%....%%..%%..%%..%%..%%......%%..%%.
.%%..%%....%%....%%.%%%..%%%%....%%.%%%..%%%%....%%%%%...%%%%............%%........%%....%%%%%...%%%%%%..%%%%....%%%%%..
..%%%%.....%%....%%..%%..%%......%%..%%..%%......%%..%%..%%..............%%..%%....%%....%%......%%..%%..%%......%%..%%.
...%%....%%%%%%...%%%%...%%%%%%..%%..%%..%%%%%%..%%..%%..%%%%%%...........%%%%...%%%%%%..%%......%%..%%..%%%%%%..%%..%%.
........................................................................................................................
    ''')

    import os
    from argparse import ArgumentParser
    import colorama as clr
    clr.init()
    parser = ArgumentParser('Vigenère Cipher')

    parser.add_argument('-d', action='store_true', dest='dec', help='[flag] decrypt')
    parser.add_argument('-e', action='store_true', dest='enc', help='[flag] encrypt')
    parser.add_argument('-k', type=str, dest='key', help='Specify key', required=True)
    parser.add_argument('-a', type=str, dest='alphabet', help='Alphabet')
    parser.add_argument('msg', help='Message')
    
    args = parser.parse_args()

    if not (bool(args.dec) ^ bool(args.enc)):
        print(clr.Fore.RED + '[-] Invalid parameters: Please provide either `dec` or `enc` flag!' + clr.Fore.RESET)
        os._exit(1)

    cipher = VigenereCipher(args.key, args.alphabet)
    print('[*] Alphabet: {}`{}` {}// Please note that any characters not present in the alphabet will be lost in translation!'\
            .format(clr.Fore.YELLOW, cipher.d, clr.Fore.LIGHTBLACK_EX) + clr.Fore.RESET)
    print('[+] {} message: {}{}'.format('Encrypted' if args.enc else 'Decrypted', clr.Fore.GREEN, cipher.enc(args.msg) if args.enc else cipher.dec(args.msg)) 
            + clr.Fore.RESET)

    print()

if __name__ == '__main__':
    main()
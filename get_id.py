#!/usr/bin/python
from hashlib import sha256
from bitcoin import encode as _encode
import math
import sys

def get_args():
    args = []
    for arg in sys.argv[1:]:
        try:
            arg = eval(arg)
        except:
            pass
        args.append(arg)
    return args

def encode(thingy):
    if type(thingy) in [int, long]:
        return _encode(thingy, 256, 32)
    if type(thingy) == str:
#        return thingy.ljust(32*int(math.ceil(len(thingy)/32.)), '\x00')
        return thingy
    if type(thingy) == list and all(type(e) in [int, long] for e in thingy):
        return ''.join(map(encode, thingy))
    return ''

def main():
    print get_args()
    print map(encode, get_args())
    print `''.join(map(encode, get_args()))`
    print '0x' + sha256(''.join(map(encode, get_args()))).hexdigest()

if __name__ == '__main__':
    main()

DEFAULT_ALPHABET = 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
DEFAULT_BLOCK_SIZE = 24
MIN_LENGTH = 5
import short_url

class UrlEncoder(object):
    def __init__(self, alphabet=DEFAULT_ALPHABET, block_size=DEFAULT_BLOCK_SIZE):
        self.alphabet = alphabet
        self.block_size = block_size
        self.mask = (1 << block_size) - 1
        self.mapping = list(range(block_size))
        #self.mapping.
    def encode_url(self, n, min_length=MIN_LENGTH):
        return self.enbase(self.encode(n), min_length)
    def decode_url(self, n):
        return self.decode(self.debase(n))
    def encode(self, n):
        return (n & ~self.mask) | self._encode(n & self.mask)
    def _encode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if n & (1 << i):
                result |= (1 << b)
        return result
    def decode(self, n):
        return (n & ~self.mask) | self._decode(n & self.mask)
    def _decode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if n & (1 << b):
                result |= (1 << i)
        return result
    def enbase(self, x, min_length=MIN_LENGTH):
        result = self._enbase(x)
        padding = self.alphabet[0] * (min_length - len(result))
        return '%s%s' % (padding, result)
    def _enbase(self, x):
        x = int(x)
        n = len(self.alphabet)
        if x < n:
            return self.alphabet[x]
        #return self._enbase(x / n) + self.alphabet[x % n]
        return self.enbase(x / n) + self.alphabet[x % n]
    def debase(self, x):
        n = len(self.alphabet)
        result = 0
        for i, c in enumerate(reversed(x)):
            result += self.alphabet.index(c) * (n ** i)
        return result

DEFAULT_ENCODER = UrlEncoder()

def encode(n):
    return DEFAULT_ENCODER.encode(n)

def decode(n):
    return DEFAULT_ENCODER.decode(n)

def enbase(n, min_length=MIN_LENGTH):
    return DEFAULT_ENCODER.enbase(n, min_length)

def debase(n):
    return DEFAULT_ENCODER.debase(n)

def encode_url(n, min_length=MIN_LENGTH):
    return DEFAULT_ENCODER.encode_url(n, min_length)

def decode_url(n):
    return DEFAULT_ENCODER.decode_url(n)
def convert_text_to_digits(value):
    pass
if __name__ == '__main__':
    #url = short_url.encode_url('ruthzilber')
    #print(url)
    print(encode('89333333333333'))
    # for a in range(0, 200000, 37):
    #     b = encode(a)
    #     c = enbase(b)
    #     d = debase(c)
    #     e = decode(d)
    #     print(b)
    #     #assert a == e
    #     #assert b == d
    #     c = (' ' * (7 - len(c))) + c
    #     print( '%6d %12d %s %12d %6d' % (a, b, c, d, e))
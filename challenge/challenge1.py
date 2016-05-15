from PIL import Image

BYTE_LEN = 8
BIT_MAP = {
    '0': '\x00',
    '1': '\xff',
}


def left_pad(string, lenght=BYTE_LEN, char='0'):
    return char * (BYTE_LEN - len(string)) + string


def char_to_byte(char):
    return left_pad(bin(ord(char))[2:])


def text_to_bytes(text, size, height):
    output = ''
    for _ in xrange(size * height):
        for char in text:
            for bit in char_to_byte(char):
                output += BIT_MAP[bit] * size
    return output


def text_to_image(text, size=10, height=10):
    return Image.frombytes('L', (len(text) * size * BYTE_LEN, size * height), text_to_bytes(text, size, height))

import string
import random


class OneTimePadForSerious:

    YESLIST = ["y", "yes"]
    NOLIST = ["n", "no"]
    SCREENSAVE = ["screen", "save"]
    ENCODEDECODE = ["encode", "decode"]

    def make_encode_dict(self):
        numberlist = list(range(1, 27))

        twodigits = []

        for x in numberlist:
            twodigits.append("{0:0=2d}".format(x))

        letters = list(string.ascii_uppercase[:27])

        encodedict = dict(zip(letters, twodigits))
        return encodedict

    def screen_or_save(self, inputlist, filename):
        screen_save = input("Would you like to save to a file or print on the screen? 'screen' or 'save' \n: ")
        stringdata = (''.join(str(x) for x in inputlist))
        while screen_save not in self.SCREENSAVE:
            screen_save = input("you have to enter 'screen' or 'save' \n: ")

        if screen_save == "screen":
            print(stringdata)
        else:
            file = open(filename + ".txt", "w")
            file.write(stringdata)
        return None

    def driver(self):

        encode_dict = self.make_encode_dict(self)
        decode_dict = {v: k for k, v in encode_dict.items()}

        newpad = input("Would you like to generate a one-time pad now? \n: ").lower()

        generated_pad = []
        pad = []

        if newpad in self.YESLIST:
            padlength = int(input("How many letters would you like to encode? \n: "))
            for i in range(0, (padlength * 2)):
                generated_pad.append(random.randint(0, 9))

            self.screen_or_save(self, generated_pad, "onetimepad")

            usenow = input("would you like to use this pad to encode a message now? \n: ")
            if usenow in self.YESLIST:
                pad = (''.join(str(x) for x in generated_pad))
        else:
            pad = input("please enter your one time pad now \n: ")

        encode_decode = input("would you like to encode or decode a message? \n: ")
        while encode_decode not in self.ENCODEDECODE:
            encode_decode = input("you have to enter 'encode' or 'decode' \n: ")

        if encode_decode == "encode":
            to_encode = input("what text would you like to encode? No spaces, use X for period, "
                              "spell out any other punctuation \n: ")
            to_encode = to_encode.upper()
            to_encode_list = list(to_encode)
            encoded = []
            for x in to_encode_list:
                encoded.append(encode_dict[x])

            self.screen_or_save(self, encoded, "encoded_message")

        if encode_decode == "decode":
            to_decode = input("enter your coded message with no spaces or punctuation \n: ")
            decoded = []

            to_decode_pairs = [i+j for i,j in zip(to_decode[::2], to_decode[1::2])]

            for x in to_decode_pairs:
                decoded.append(decode_dict[x])

            self.screen_or_save(self, decoded, "decoded_message")

OneTimePadForSerious.driver(OneTimePadForSerious)
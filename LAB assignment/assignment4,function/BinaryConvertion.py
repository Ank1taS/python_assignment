'''
    to convert a decimal number to binary using recussion function dec_to_bin()
    file name   :   BinaryConvertion1.py
    date        :   07/10/2020
'''
#recursion function dec_to_bin()
def dec_to_bin(decNum):
    if decNum == 0:
        return 0
    else:
        return (decNum % 2 + 10 * dec_to_bin(decNum // 2))

# main()
while True:
    dec = input("Enter a decimal integer = ")
    if isinstance(dec, int) != 0:
        print("{0} is not a integer number ")
    else:
        dec = int(dec)
        break

print("Binary convertion {0} = {1}".format(dec, dec_to_bin(dec)))

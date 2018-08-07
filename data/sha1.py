import hashlib
import itertools
import sys
import hsh
hash = hsh.hash
i = 0
def dictionary():
        wlist = input("Wordlist: ")
        try:
            f = open(wlist, 'r').readlines()
        except IOError:
            print("Wordlist not found!")
            quit()
        for guess in f:
            newhash = hashlib.sha1(guess.encode("utf-8")).hexdigest()
            if newhash == hash:
                print("\nHash Cracked:",guess)
            else:
                sys.stdout.write("\rTesting " + 
guess)
                sys.stdout.flush()
def brute():
    print("""
Charsets:
1. Alpha (Lowercase letters)
2. Alpha Numeric (Lower & Uppercase letter with 
numbers)
3. Numeric (Numbers only)
4. Full (Lower & Uppercase letters, Numbers, 
Special characters)
5. Custom
""")

    CHARSET_NUMERIC = "0123456789"
    CHARSET_ALPHA ="abcdefghijklmnopqrstuvwxyz."
    CHARSET_ALPHANUMERIC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    CHARSET_FULL = """ !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    option = input(">> ")
    if option == "1":
        charset = CHARSET_ALPHA
    elif option == "2":
        charset = CHARSET_ALPHANUMERIC
    elif option == "3":
        charset = CHARSET_NUMERIC
    elif option == "4":
        charset = CHARSET_FULL
    elif option == "5":
        charset = input("Charset> ")
    else:
        print("Not a valid option. Setting charset to Alpha Numeric")
        charset = CHARSET_ALPHANUMERIC
    minimum = int(input("Minimum length: "))
    for length in range(minimum, 9999):
            gen = itertools.product(charset, repeat=length)
            for i in gen:
                new = hashlib.sha1(''.join(i).encode("utf-8")).hexdigest()
                if new == hash:
                 frst = ''.join(i).replace(',', 
'')
                 frstt = frst.replace('(', '')
                 frsttt = frstt.replace(')', 
'')
                 print("\nHash Cracked:",frsttt)
                 quit()
                else:
                 i += 1
                 frst = ''.join(i).replace(',', 
'')
                 frstt = frst.replace('(', '')
                 frsttt = frstt.replace(')', 
'')
                 sys.stdout.write("\rTested %s " % str(i))
                 sys.stdout.flush()

print("""
1. Dictionary Attack
2. Bruteforce
""")
choose = input(">> ")
if choose == "1": dictionary()
elif choose == "2": brute()
else:
    print("Not a valid option")
    quit()





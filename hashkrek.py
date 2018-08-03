import hashlib, argparse, time, os
def arg():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('-H,', '--hash', help="Hash To Crack")
    parser.add_argument('-hT', '--hashtype', help="Hash Type: md5, sha1, sha256")
    args = parser.parse_args()
    if args.hash == None:
       print("No Hash Specified!")
       quit()
    elif args.hashtype == None:
       print("No Hash-Type Specified!")
       quit()
    else:
       f = open("data/hsh.py", "w")
       f.write('hash = "' + str(args.hash) + '"')
       pass
arg()
class md5:
      def __init__(hash):
          arg()
          hash = args.hash
          os.chdir("data")
          os.system("python md5.py")
class sha1:
      def __init__(hash):
          arg()
          hash = args.hash
          os.chdir("data")
          os.system("python sha1.py")
class sha256:
      def __init__(hash):
          arg()
          hash = args.hash
          os.chdir("data")
          os.system("python sha256.py")
if __name__ == '__main__':
   print('''
Hashkrek - By NSK B3
___________________ 
|HASHTYPE|--|SPEED|
|--------|--|-----|
|  MD5   |--|17k/s|
|--------|--|-----|
| SHA256 |--|19k/s|
|--------|--|-----|
|  SHA1  |--|15k/s|
|________|__|_____|
''')
   if args.hashtype == "md5" or "MD5":
      md5.__init__(hash)
   elif args.hashtype == "sha1" or "SHA1":
      sha1.__init__(hash)
   elif args.hashtype == "sha256" or "SHA256":
      sha256.__init__(hash)
   else:
      print("Supported Hash Types:\nMD5\nSHA1\nSHA256")
      time.sleep(3)
      os.system("python hashkrek.py")
           

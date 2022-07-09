from Compression import *

fh = open("File.txt","w")
fh.write("0"*5000000)
fh.close()

gzip_compress("File.tar.gz",["File.txt"])

_7z_compress("File.7z","File.txt"):

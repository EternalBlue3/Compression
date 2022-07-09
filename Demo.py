from Compression import *

fh = open("File.txt","w")
fh.write("0"*5000000)
fh.close()

compress_gzip("File.tar.gz",["File.txt"])

compress_7z("File.7z","File.txt")
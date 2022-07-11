from Compression import *

file_write = "0" * 10000000, "1" * 10000000, "2" * 10000000, "3" * 10000000, "4" * 10000000, "5" * 10000000, "6" * 10000000, "7" * 10000000, "8" * 10000000, "9" * 10000000
file_write = ''.join(file_write)
fh = open("File.txt","w")
fh.write(file_write)
fh.close()

compress_gzip("File.tar.gz",["File.txt"])

compress_bzip2("File.bz2",["File.txt"])

compress_lzma("File.xz",["File.txt"])

compress_7z("File.7z","File.txt")

from compression import *

fh = open("File.txt","w")
fh.write("0"*5000000)
fh.close()

gzip_compress(f"File.tar.gz",[f"File.txt"])

import tarfile
from tqdm import tqdm
import py7zr

def compress_lzma(file, members):
    # open file for gzip compressed writing
    tar = tarfile.open(file, mode="w:xz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()

def compress_bzip2(file, members):
    # open file for gzip compressed writing
    tar = tarfile.open(file, mode="w:bz2")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()

def compress_gzip(tar_file, members):
    """
    Adds files (`members`) to a tar_file and compress it
    """
    # open file for gzip compressed writing
    tar = tarfile.open(tar_file, mode="w:gz")
    # with progress bar
    # set the progress bar
    progress = tqdm(members)
    for member in progress:
        # add file/folder/link to the tar file (compress)
        tar.add(member)
        # set the progress description of the progress bar
        progress.set_description(f"Compressing {member}")
    # close the file
    tar.close()
    
def compress_7z(archive_name,file_name):
    
    with py7zr.SevenZipFile(archive_name, 'w') as archive:
        archive.write(file_name)

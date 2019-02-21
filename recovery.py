#!/usr/bin/env python
import os, errno, shutil, glob

def get_args():
    import argparse

    description = (
        "Sort files recoverd by Photorec.\n"
        "Files are sorted by extension and copied into respective folders.\n"
        "Dead files are removed less than 15 kb and or had no extension"
    )

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('source', metavar='src', type=str, help='source directory with files recovered by Photorec')
    parser.add_argument('destination', metavar='dest', type=str, help='destination directory to write sorted files to')
    parser.add_argument('-r', '--remove_junk', action='store_true', required=False, help='Dead and junk files less than 15 kb and or had no extension are deleted')
    
    return parser.parse_args()

source = None
destination = None
removeJunk = False

args = get_args()
source = args.source
destination = args.destination
removeJunk = args.remove_junk



while ((source is None) or (not os.path.exists(source))):
    source = input('Enter a valid source directory\n')
while ((destination is None) or (not os.path.exists(destination))):
    destination = input('Enter a valid destination directory\n')


#cleans PhotoRec file dump of all the thousands of files that
# are below 15kb if removeJunk was set to true with -r option parameter 

path=(source+"\\recup_dir.*\\*")
for filename in glob.glob(path):
    if os.path.getsize(filename) < 15 * 1024: #anything less than 15kb is removed 
        os.remove(filename)

#removes any empty directories after first cleaning pass and lists folders that remain at this point     
path2=(source+"\\recup_dir.*")
for xdirs in glob.glob(path2):
    if removeJunk == True:
        try:
            os.rmdir(xdirs)

        except OSError as ex:
            if ex.errno == errno.ENOTEMPTY:
                print(xdirs + "is still full and so not removed yet"),

#creates folders by extention and copies files to folders
                
for root, dirs, files in os.walk(source, topdown=False):

    for file in files:
        extension = os.path.splitext(file)[1][1:].upper()
        sourcePath = os.path.join(root, file)

        destinationDirectory = os.path.join(destination, extension)

        if not os.path.exists(destinationDirectory):
            os.mkdir(destinationDirectory)
   
        destinationFile = os.path.join(destinationDirectory, file)
        if not os.path.exists(destinationFile):
            shutil.copy2(sourcePath, destinationFile)

# If you use same destination as source 
# cleans PhotoRec file dump of all the thousands of junk files that get dumped into the source 
# directory because they don't have an extention to filter on
for entry in os.scandir(source):
    if removeJunk == True and entry.is_file():
        junkfile = (source + entry.name)
        os.remove(junkfile)
        
# If you use different destination than source 
# cleans PhotoRec file dump of all the thousands of junk files that get dumped into the destination
# directory because they don't have an extention to filter on and therefore copy into folders
for entry in os.scandir(destination):
    if removeJunk == True and entry.is_file():
        junkfile = (destination + entry.name)
        os.remove(junkfile) 

# cleans out original recup folders created by photo rec
for entry in os.scandir(source):
    if removeJunk == True and entry.is_dir() and "recup" in entry.name:
        junkdir = (source + entry.name + "\\")
        shutil.rmtree(junkdir)

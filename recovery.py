
#!/usr/bin/env python
#https://github.com/dcummuta/sort-PhotorecRecoveredFiles

import os, errno, shutil, glob, re, time


def get_args():
    import argparse

    description = (
        "Sorts files recoverd by Photorec.\n"
        "Folders are created by extension name\n"
        "Files are then copied into their respective folders.\n"
        "with particular options -r, -f, -rr file and directory cleanups\n" 
        "can be ran after the file sorting is done\n"
        "see option descriptions use -h with no destination or source when running.\n"
        "for no cleanup run source and destination only."
    )

    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('source', metavar='src', type=str, help='source directory with files recovered by Photorec')
    parser.add_argument('destination', metavar='dest', type=str, help='destination directory to write sorted files to')
    parser.add_argument('-r', '--remove_junk', action='store_true', required=False, help='Removes files without extension and empty folders')
    parser.add_argument('-f', '--filesize_limit', type=int, default=15, required=False, help='Set limit first pass of files less than or equal to x kb to be removed')
    parser.add_argument('-rr', '--remove_orig', action='store_true', required=False, help='remmoves original photorec recup folders and contents if you want to clean them up')

    return parser.parse_args()

source = None
destination = None
removeJunk = False
filesizelimit = 15
removeorig = False

args = get_args()
source = args.source
destination = args.destination
removeJunk = args.remove_junk
filesizelimit = args.filesize_limit
removeorig = args.remove_orig

while ((source is None) or (not os.path.exists(source))):
    source = input('Enter a valid source directory\n')
while ((destination is None) or (not os.path.exists(destination))):
    destination = input('Enter a valid destination directory\n')

time.sleep(2)
print(" Begining first clean up pass")

#cleans PhotoRec file dump of all the thousands of files that
# are below 15kb (this substantially improves this scripts performance and can be
# adjusted with the -f option

path=(source+"\\recup_dir.*\\*")
for filename in glob.glob(path):
    if os.path.getsize(filename) <= filesizelimit * 1024: #anything less than 15kb is removed 
        os.remove(filename)

#removes any empty directories after first cleaning pass and lists folders that remain at this point     
path2=(source+"\\recup_dir.*")
for xdirs in glob.glob(path2):
    try:
        os.rmdir(xdirs)

    except OSError as ex:
        if ex.errno == errno.ENOTEMPTY:
            print(xdirs + " Skipped non-empty folder"),

#creates folders by extention and copies files to folders
#otherwise if file already exists in destination it renames the file
#then copies the file to the file extention directory. this is in case it is not 
#the same but, just has the same name from a different photorec dump
time.sleep(1)
print(" ")
time.sleep(1)
print(" file extention directories being created")
print(" ")
print(" Renaming any files with same name")
print(" ")
print(" And")
print(" ")
time.sleep(1)
print(" Copying files")
print(" ")
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
        else:
            try:
                n = 0
                while os.path.exists(destinationFile):
                    src=(destinationDirectory+"\\"+file)
                    dst=(destinationDirectory+"\\"+str(n)+file)
                    n += 1
                    os.rename(src,dst)
            except:    
                break

        if os.path.exists(destinationFile):
            shutil.copy2(sourcePath, destinationFile)

print(" Done with file sort and copy")
print(" ")
time.sleep(1)
print(" Begining cleanup")

# This cleans PhotoRec file dump of all the thousands of junk files that get dumped 
# into the source or desitnation depending on if you use the same directory for both
# because the files don't have an extention to filter on and are also unopenable for normal use cases

print("Removing dead files in source and or destination that have no extention")
print(" ")
time.sleep(1)
for entry in os.scandir(source):
    if removeJunk == True and entry.is_file() and "." not in entry.name:
        junksfile = (source + entry.name)
        os.remove(junksfile)

for entry in os.scandir(destination):
    if removeJunk == True and entry.is_file() and "." not in entry.name:
        junkdfile = (destination + entry.name)
        os.remove(junkdfile)
print(".")
print("..")
print("...")


time.sleep(1)

# cleans out original recup folders created by photorec since if you have made it this far
# without error all files were moved correctly

for entry in os.scandir(source):
    if removeorig == True and entry.is_dir() and "recup" in entry.name:
        print(entry.name + "-rr was used in options cleaning original direcories")
        junkdir = (source + entry.name + "\\")
        shutil.rmtree(junkdir)

print(" ")
time.sleep(1)
print("Completed with no errors")

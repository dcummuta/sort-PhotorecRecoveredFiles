# Sort files recoverd by Photorec

Photorec does a great job when recovering deleted files. But the result is a huge, unsorted, unnamed amount of files. Especially for external hard drives serving as backup of all the personal data, sorting them is an endless job.


## Installation

First install the package [exifread](https://pypi.python.org/pypi/ExifRead):

```pip install exifread```

## Run the sorter

Then run the sorter:

```python recovery.py <path to files recovered by Photorec> <destination>```

This copies the recovered files to their folders that are created and named by their respective extensions in the destination directory you specify.  Things to note you must end the source and destination directories you chose in the command with a directory closing \ or / depenending on if you are using this in unix or windows. 
**Example:**
```python recovery.py C:\sourcefolder\ C:\destinationfolder\```

```python recovery.py /home/downloads/sourcefolder/ /home/downloads/destinationfolder/```

Also, you can make the source folder the same as the destination folder.  This is something that seems more feasable in the version because the script will be cleaning out all previous folders left by photorec after moving files from them when using the **-r** option described below.  

The recovered files are not modified. If a file already exists in the destination directory, it is skipped. Hence you can interrupt the process with Ctrl+C and continue afterwards.

First output lets you know which folders were left after cleaning up the initial empty folders after cleaning anything less than 15KB from the source folders.  

### Parameters

For an overview of all arguments, run with the `-h` option: ```python recovery.py -h```.
(if you are used to using a previous verison I suggest you do this as other arguments have been removed)


This version of recovery.py was specifically created to run a pre and post sort cleanup with the added `-r` 
parameter option:```python recovery.py <path to files recovered by Photorec> <destination> -r```

**this option cleans out all "junk" files that do not have extensions or are lower than 15kb **
**for me the reason I created this was because **
**I have a lot of old drives that used to have OS's on them**
**this means there are thousands of junk files that are **
**either unretreavable by photorec or are so small they are **
**tiny PNGs from web pages during browesing etc. **
**Currently this -r option only works on Windows.  **
**I will be updating this to clean on linux/unix boxes but, I just have to test it with aditional error handling.  **

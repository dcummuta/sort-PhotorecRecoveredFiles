# Sort files recoverd by Photorec

Photorec does a great job when recovering deleted files. But the result is a huge, unsorted, unnamed amount of files. Especially for external hard drives serving as backup of all the personal data, sorting them is an endless job.


## Installation

First install the package [exifread](https://pypi.python.org/pypi/ExifRead):

```pip install exifread```

## Run the sorter

Then run the sorter:

```python recovery.py <path to files recovered by Photorec> <destination>```

This copies the recovered files to their folders that are created and named by their respective extensions in the destination directory you specify.  Things to note you must end the source and destination directories you chose in the command with a directory closing \ or / depenending on if you are using this in unix or windows. 

```python recovery.py -h```

The recovered files are not modified. If a file already exists in the destination directory, it is skipped. Hence you can interrupt the process with Ctrl+C and continue afterwards.

First output lets you know which folders were left after cleaning up the initial empty folders after cleaning anything less than 15KB from the source folders.  

### Parameters

For an overview of all arguments, run with the `-h` option: ```python recovery.py -h```.
(if you are used to using a previous verison I suggest you do this as other arguments have been removed)
###

This version of recovery.py was created specifically to run a pre and post sort cleanup with the added `-r` 
parameter option:```python recovery.py <path to files recovered by Photorec> <destination> -r```

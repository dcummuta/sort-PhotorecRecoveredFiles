# Sort files recoverd by Photorec

Photorec does a great job when recovering deleted files. But the result is a huge, unsorted, unnamed amount of files. Especially for external hard drives serving as backup of all the personal data, sorting them is an endless job.

Created this branch for a Minimalist version that is not concerned with JPG sorting, file counting, or delta event times.

The primary purpose of the branch is for cleanup that is ran pre and post sorting.  This is to conserve drive space, manage the thousands of junk files that can still be created by photorec, and clean up photorec folders when it is done.  

This minimalist version will keep duplicate copies like the original recovery.py and maintain all recup folders but, if -r is used it will clean all of this as well as many junk files that have no extention and are therefore useless.  


## Run the sorter

Then run the sorter:

```python recovery.py <path to files recovered by Photorec> <destination>```

This copies the recovered files to their folders that are created and named by their respective extensions in the destination directory you specify.  Things to note you must end the source and destination directories you chose in the command with a directory closing \ or **/** depenending on if you are using this in windows or unix respectively. 

**Example:**

```python recovery.py C:\sourcefolder\ C:\destinationfolder\```

```python recovery.py /home/downloads/sourcefolder/ /home/downloads/destinationfolder/```

Also, you can make the source folder the same as the destination folder.  This is something that seems more feasable in the version because the script will be cleaning out all previous folders left by photorec after moving files from them when using the **-r** option described below.  

The recovered files are not modified. If a file already exists in the destination directory, it is skipped. Hence you can interrupt the process with Ctrl+C and continue afterwards.

First output lets you know which folders were left after cleaning up the initial empty folders after cleaning anything less than 15KB from the source folders.  

### Parameters

For an overview of all arguments, run with the `-h` option: ```python recovery.py -h```.
(if you are used to using a previous verison I suggest you do this as other arguments have been removed)


**Currently this -r option only works on Windows.**
**I will be updating this to clean on linux/unix boxes but, I just have to test it with aditional error handling.**

This version of recovery.py was specifically created to run a pre and post sort cleanup with the added `-r` 
parameter option:```python recovery.py <path to files recovered by Photorec> <destination> -r```

**this option cleans out all "junk" files that do not have extensions or are lower than 15kb**
**for me the reason I created this was because**
**I have a lot of old drives that used to have OS's on them**
**this means there are thousands of junk files that are**
**either unretreavable by photorec or are so small they are**
**tiny PNGs from web pages during browsing, BMP, dll, etc.**

#### Standalone EXE 

Can be ran from windows CMD prompt with same parameter and source/destination rules as above **without python**, scripted into a bat file, etc
you do not need python installed on the windows machine to run this 

## Potential future features/fixes
- Want to make the .py file cross platform with error handling for different directory cleanup procedures
- Reintroduce exifread script for jpg sorter from original fork and potentially expand this to give more metadata on other kinds of files (movie names etc) Currently removed as it is not used by this script or the standalone exe.
- Thinking of maybe making a tkinter gui for it
- Potentially script in batch and bat files to run photorec via CLI version automatically from tkinter gui


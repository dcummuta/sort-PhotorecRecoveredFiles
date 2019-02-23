# Sort files recoverd by Photorec

Photorec does a great job when recovering deleted files. But the result is a huge, unsorted, unnamed amount of files. Especially for external hard drives serving as backup of all the personal data, sorting them is an endless job.

Created this branch for a Minimalist version that is not concerned with JPG sorting, file counting, or delta event times.

The primary purpose of the branch is for cleanup that is ran pre and post sorting.  This is to conserve drive space, manage the thousands of junk files that can still be created by photorec, and clean up photorec folders when it is done.  

This minimalist version will keep duplicate copies like the original recovery.py and maintain all recup folders but, if certain options are used it will clean all of this as well as many junk files that have no extention and are therefore useless.  


## Run the sorter

To Run:

```python recovery.py <path to files recovered by Photorec> <destination>```

This copies the recovered files to their folders that are created and named by their respective extensions in the destination directory you specify.  Things to note you must end the source and destination directories you chose in the command with a directory closing \ or **/** depenending on if you are using this in windows or unix respectively. 

**Example:**

```python recovery.py C:\sourcefolder\ C:\destinationfolder\```

```python recovery.py /home/downloads/sourcefolder/ /home/downloads/destinationfolder/```

Also, you can make the source folder the same as the destination folder.  This is something that seems ideal feasable in this version because the script will be cleaning out all folders adding to folders and renaming files if similar file names exist.  

The recovered files are not modified unless you are running the script over the same folders again because you stopped midway in a previous run.  You can interrupt the process with Ctrl+C and continue afterwards.

### Parameters

For an overview of all arguments, run with the `-h` option: ```python recovery.py -h```.

(if you are used to using a previous verison I suggest you do this as older arguments have been removed in this version)


**Currently only tested to work on Windows.**
I will be updating this for linux/unix boxes but, I just have to test it with aditional error handling.
I believe the script will run without any options on linux but, may run into issues when you try to use the clean options.  

This version of recovery.py was specifically created to run a pre and post sort cleanup with the added 
`-r` 
parameter option:

```python recovery.py <path to files recovered by Photorec> <destination> -r```

Runs pre sort and post sort cleanups on files without extenstions or empty directories from other clean up options.


**The application by default deletes all files that are below 15kb unless you use the `-f` option**
This substantially increases performance of the script if you have many files to sort. 
For example if you wanted to remove anything equal to or less than 2KB 

```python recovery.py <path to files recovered by Photorec> <destination> -f2```

I have added an option to control if the script cleans up the original "recup" directories after it is done. 

**to activate this clean up use the `-rr` option**

```python recovery.py <path to files recovered by Photorec> <destination> -rr```

## Note that the -f and -rr options delete files from the original directories so use caution or you'll have to run your photorec again


#### Standalone EXE 

Can be ran from windows CMD prompt with same parameter and source/destination rules as above or scripted into a bat file, etc
you do not need python installed on the windows machine to run this 

Windows exe Has been tested and works on: 

- Windows 7 enterprise

- Windows 10 Pro

## Potential future features/fixes
- Want to make the .py file cross platform unix, macos
- Thinking of maybe making a tkinter gui for it
- Potentially script in batch and bat files to run photorec via CLI version automatically from tkinter gui

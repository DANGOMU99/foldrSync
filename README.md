# foldrSync

This program keeps a folder *replica* with the same contents as another folder *source*, this check is done
periodically with a timer that is user defined.

****

## Execution

The program starts by asking the user for the folder name of the **source** folder, if this folder is not existent
within the project folder, it is created.

Next, it asks the user for the folder name of the **replica** folder, similar to the source folder, is it does not
exist, it is also created.

It also asks for the name for the **logfile** to which all operations will be recorded on, should be written without
the file extension as it assumes it's going to be a .txt file.

Finally, it asks for the **time_interval** for the synchronization of the folders (i.e. how many seconds it should wait
periodically to check the contents of the folders and update accordingly)

From this point onwards, every **time_interval** seconds it will check the **source** folder contents and using the
***filecmp*** library for file comparison, will compare the files with the files present in **replica** folder and
either copy, update or delete the files to match the same contents in the **source** folder. It is also logged if
the file present is synced.

### Limitations

It was not considered that in the **source** folder would be possible to have another folder present within, 
folders are ignored from synchronization.
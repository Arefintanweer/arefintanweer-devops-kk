'''
#WORKING YOUR WAY THROUGH CLI
CentOs as linux distro in this course.
shell types : not GUI; Command-line: linux shell(bash shell)
BASIC COMMANDS:
1. echo #print to screen
2. ls #List files and Folder
3. cd #Change directory
4. pwd  #present working directory
5. mkdir #Make Directory
6. cd new_directory; mkdir www; pwd #multiple commands
DIRECTORY COMMANDS
7. mkdir -p #create full directory tree in one shot
  mkdir -p /tmp/asia/bangladesh/sylhet  
8. rm -r  #remove directory
9. cp -r  #Copy directory
FILES COMMANDS
10. touch new_file.txt #create a file without contents
11. cat > new_file.txt #Add contents to file
12. Ctrl + D # exit out of the prompt and save data 
13. cat new_file.txt #view contents of the file
14. cp # Copy file
15. mv #Move(Rename) file
16. rm #Delete the file

#VI EDITOR
vi filename #to open a file

INSERT MODE
to enter insert mode press i 

COMMAND MODE
to switch back to command mode press the escape key ESC
delete : x deletes one character, dd delete the whole line
copy paste: yy to copy, p to paste
Scroll: Ctrl+u (up), Ctrl+d (down)
save : :w
quit : :q
save and quit: :wq
find any word: /yoursearchwordname, to move the cursor press the n key

#MORE LINUX COMMANDS
1- to know the user : whoami
2- details about the user : id
3- switch one user to another: su username (then give password)
4- accessing one system from another system with ssh: 
ssh username@192.168.1.2
5-regular user with root power: sudo ls /root
6- to download the file: curl download-file-url -O or wget download-file-url -O nameofthefile
7- check os version :ls /etc/*release*
8- details about the os: cat /etc/*release*



'''
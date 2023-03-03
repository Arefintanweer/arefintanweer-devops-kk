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

#PACKAGE MANAGEMENT IN LINUX
package managers:
RPM based(Red hat package manager) :
rpm -i telnet.rpm #install package
rpm -e telnet.rpm #Uninstall package
rpm -q telnet.rpm #query package

rpm -q packagename #to check package is installed or not

rpm -qa #to see all the installed packages

sudo rpm -i version-number # install package
sudo rpm -e version-number #uninstall package

rpm package manager doesn't care about the other dependencies so we need to use high level package manager called YUM.

sudo yum install ansible #install package

yum list ansible #see available packages with version number

yum remove ansible #remove package

yum --showduplicates list ansible #all available packages

yum install ansible-2.4.2.0 #install a specific version of the tool


#SERVICES IN LINUX: HELP CONFIGURE SOFTWARES TO RUN ON THE BACKGROUND AND  MAKE SURE THEY RUN ALL THE TIME AUTOMATICALLY AFTER THE SERVER IS REBOOTED. ANY SOFTWARE RUNNING IN THE BACKGROUND EX: DOCKER THEY ARE AUTOMATICALLY COUNT AS A SERVICE IN THE SYSTEM.

service httpd start #start HTTPD service

systemctl start httpd #start HTTPD service
systemctl start my_app #start my_app service

systemctl stop httpd # stop HTTPD service

systemctl status httpd #check HTTPD service status

systemctl enable httpd #configure HTTPD to start automatically at startup

systemctl disable httpd #configure HTTPD to not start at startup


HOW TO CONFIGURE OUR APP AS systemd service?
this file is located in /etc/systemd/system. create a unit file as my_app.service.
define a section called service by [Service] and under that give directive ExecStart = give your application run command. Now your application is configured as a service.

then run:
systemctl daemon-reload #let the systemd know about new service
systemctl start my_app
systemctl status my_app
curl http://localhost:5000 [if active(running) then it's working]
systemctl stop my_app

Application is now configured and we can run and stop it as a service but how can we do it configure automatically when the the system restarts?

go to the my_app.service file
[Unit]
Description = My Python web application

[Service]
ExecStart = /usr/bin/python3 /opt/code/my_app.service
ExecStartPre= /opt/code/configure_db.sh #other dependencies that need to run before the application
ExecStartPost= /opt/code/email_status.sh #dependencies that need to run after the application
Restart= always #restart the application automatically if crash

[Install]
WantedBy = multi-user.target

in real project this file will be more complex.

'''
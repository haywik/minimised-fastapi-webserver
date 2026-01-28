# How to use this?

Create a venv, then run it as shown.


Method 1 is preffered for automatic bash scripting, then skip the Setup.

Method 2 is preffered for user interaction or begginers.



----

Pre-Setup:
(skip if u understand this stuff)

`mkdir -p /home/$USER/web-project-haywik/`
make a prokject location
`cd /home/$USER/web-project-haywik/`
Go to where you want it to be stored, i use the home directory.

`git clone https://github.com/haywik/minimised-fastapi-webserver`
This makes a folder in the curernt directory with the repo.

`cd minmised-fastapi-webserver`
Into the folder

----


`python3 -m ./venv `
Create the python virutal enviroment in the venv folder


Method 1:
(good for bash scripts)

`/home/USERNAME/web-project-haywik/venv/bin/python -m pip install /home/USERNAME/web-project-haywik/depend.txt`
  ^Set the correct USERNAME or path^                                 ^Set the correct USERNAME or path^
  
  this will throw an error if you dont chnage the USERNAME tag



Method 2:
(good for active user interactions)

`cd venv/bin`
`. activate`

now the venv is activated shown by the (venv) at the begging of the terminal line

`pip install repo/depend.txt`





-To run the Script-

Method 1: 
`/home/USERNAME/web-project-haywik/venv/bin/python -m pip install /home/USERNAME/web-project-haywik/wsgi.py`
  ^Set the correct USERNAME or path^                                 ^Set the correct USERNAME or path^


Method 2:
(good for active user interactions)

I assume we are still in the correct folder.

`python3 wsgi.py`
And it runs

do 
`python3 wsgi.py &`
to run in background
























    

# DroneOpenCV

---

Author: Pranav Jain

Email: jainpranav1997@gmail.com

Date: 4 September, 2022

---

# Description
Control drone based on image recognition using OpenCV

---



---
# Commonly used commands
## Creating virtual environment
#### On windows:
```
python -m venv .venv
```
- *Always remember to add virtual environment folder to .gitignore*
#### On Linux:
You may need to run sudo apt-get install python3-venv first
```
python3 -m venv .venv
```


## Creating requirements.txt file

```
pip3 freeze > requirements.txt  # Python3
```

## Installing Packages using requirements.txt
```
pip install -r requirements.txt
```

---
## Shebang in python File
The first line of the python file would point to the python.exe present in the virual environment. 
Here is an example of shebang pointing to python.exe present in a virtual environment called *.venv* :
```
#!.venv\Scripts\python.exe
```

## Steps to active venv from terminal

```
.venv\Scripts\activate.bat
```
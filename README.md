# python-programming-efficiently
Some challenges and exercises completed as part of [linkedin learning](https://www.linkedin.com/learning/python-programming-efficiently)

## Linux (Ubuntu 18.04)
To see if python is already installed run the following command.
    
    $ python3 -V
If you get an output such as.
     
     python3.7.0
     
You're a good to go, if not open a terminal and run the following commands.
    
    $ sudo apt-get update
    $ sudo apt-get install python3.7
    
To see if it's installed run

     $ python3 -V

Once python is installed now it's time to install pip which is a command line based package management system. It is used to install and manage libraries in Python.

To install pip on python3.7 we shall run the following command.

    $ python3.7 -m pip install pip
    
You should verify that pip has been installed correctly using this command:

    $ pip3 --version
    
It should show you a number like this:

    pip 18.0 from /usr/lib/python3.7/site-packages/pip (python 3.7)
    
It means that pip3 is successfully installed on your system. Now we can start installing packages using the command below.

    $ pip3 install <package_name>
    
To uninstall packages run this command.

    $ pip3 uninstall <package_name>
    
In order to see all local installed packages, the following pip command will help.

    $ pip list
    
To install a virtual environment we will be using virtualenvwrapper

    $ sudo pip3 install virtualenvwrapper
    
Now that virtualenvwrapper is installed, lets create our virtual environment

    $ mkvirtualenv myvirtualenv --python=/usr/bin/python3.7

If successful you should now see your virtual environment being created by appearing left of the dollar sign ($)

    (myvirtualenv) $
    
To deactivate your virtual environment, run the command.

    (myvirtualenv) $ deactivate
    
You should now see just the normal dollar sign symbol ($) on the terminal and no active virtual envirnoment. To reactivate your virtual environment run the command.

    $ workon myvirtualenv

To see all your current virtual environments currently on your system, run the following command.

    $ lsvirtualenv

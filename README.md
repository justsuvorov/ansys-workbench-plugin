# ANSYS Workbench - Batch Mode - Python Scripts

**Platform** - Tested on Windows 10

**ANSYS Version** - Tested on 2020R2 ; will most likely work on other versions that are not older than 19.2

This is a collection of python scripts I made for optimization of constuctures dealing with ANSYS Workbench Batch mode. I used scripts by Toybich Egor (1-2)(https://github.com/sikvelsigma/ANSYS-WB-Batch-Script)

 It requres no additional python packages whatsoever. Right now there are 7 modules:

1. *WBInterface.py*
2. *Logger.py*
3. *ap_parameters.py*
4. *ap_jaya.py*
5. *ap_handle.py*
6. *goalFunction.py*
7. *run_script.py*

Ansys Workbench comes with IronPython 2.7 so to run it from batch mode we need to write a python script, which will control the flow of the project (*run_script.py* as an example here) and a *.bat* file (*run.bat* as an example here).

- Module *WBInterface.py* is the main module which contains a class with all the useful workbench commands. I tried to document it as much as I could. This module is absolutely essential to have.

- Module *Logger.py* contains a class which will create a log file in the project directory and write the flow of the project to it. This module is absolutely essential to have.

- Module *ap_parameters.py* is a class for reading parameters from txt files (input keys, input values, output keys). 

- Module *ap_jaya.py* is a class for the implementaion of Jaya algorithm for structure optimization. More info about the algorithm on http://www.growingscience.com/ijiec/Vol7/IJIEC_2015_32.pdf

- Module *ap_handle.py* is a class for working with WBinterface and choosing of modules for solving different problems with Ansys. It will be used for future modules.

- Module *goalFunction.py* contains a goal (cost) function for the specific optimization problem. It uses results of simulations for the calculation of new values of parameters


## How to use 
First of all, this was all made with running it on a remote machine in mind, when you don't have an ability to install additional software or open apps, but have access to a file system. Second of all, in my work I use a specialised hierarchical software which does not support making changes to already existing files, so there was a need to be able to import modules by their modified names (like *WBInterface_100.py* for example). That's why there's this weird system with **exac()** commands implemented to input everything correctly. 
So, the simplest way to use all of this would be:

1. Drop modules *WBInterface.py* and *Logger.py* into the same folder where your ANSYS WB archive/project currently resides
2. Drop *run_script.py* and *run.bat* there also
3. Configure *.bat* file for your machine and run it; format of *.bat* file:

        "<ansysdir>\v<ver>\Framework\bin\Win64\RunWB2.exe" -B -R "run_script.py"

4. Copy and paste names of input parameters in input keys.txt
5. Copy and paste names of output parameters in output keys.txt
6. Copy and paste values of input parameters in input values.txt
7. Run run.bat file


The script will automatically try to find *.wbpz* file and open it or, failing that, it will try to find a *.wbpj* file. After the project was opened, the script will try to issue a global Update command for all DPs (Design Points) present in the project. 


By default in the project directory a *log.txt* file will be created. Output is written to an *output.txt* file csv-style and Workbench parametric report is saved to a *full_report.txt* file. Of course this is all customizable.


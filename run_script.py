from glob import glob 
import sys
import platform
import os
from ap_handle import APHandle
from ap_parameters import APParameters
import goalFunction
from ap_jaya import APJaya
""" Script by Anton Lobanov and Vladimir Suvorov
Note: Workbench uses IronPython (Python 2.7)!

Use iterationBuilder = None for updating WB project with user values of parameters
Use iterationBuilder = 1 for using Jaya algorithm for optimization problems in WB
For optimization problem you should write a code for a goal (cost) function in goalFunction.py


"""
#from numpy import loadtxt
#===========================================================================
#======= This block imports framework files ================================
#===========================================================================
def find_module(st_in):
    res = []
    stlist = st_in if isinstance(st_in, list) else [st_in]
    
    for st in stlist:
        try:
            srch = [f for f in glob('{}*.py'.format(st))]
            print('Found: {}'.format(srch))
            srch = srch[0] if srch[0] == '{}.py'.format(st) else srch[-1]
            srch = srch.replace('.py','')
        except: res.append(None)
        else: res.append(srch)
    return tuple(res) if len(stlist) > 1 else res[0]
    
print(1)
modules = ['WBInterface', 'ExcelFileReader', 'Logger', 'CSVTable']
modules_files = find_module(modules)

print('Using: {}, {}, {}, {}'.format(*modules))

if modules_files[0]: exec('from {} import WBInterface'.format(modules_files[0]))
#if modules_files[1]: exec('from {} import ExcelFileReader'.format(modules_files[1]))
if modules_files[2]: exec('from {} import Logger'.format(modules_files[2]))
#if modules_files[3]: exec('import {} as CSVTable'.format(modules_files[3]))
#===========================================================================
#===========================================================================
#===========================================================================

_logger = Logger('log.txt')
_log_ = _logger.log


def apJayaIterationBuilder(index, outParams):
    _log_('[apJayaIterationBuilder] index: ' + str(index))
    _log_('[apJayaIterationBuilder] outParams: ' + str(outParams))
    apJayaAlgorithmResult =  apJaya.algorithm(index, outParams)
    _log_('[apJayaIterationBuilder] apJayaAlgorithmResult: ' + str(apJayaAlgorithmResult))
    parameters = APParameters(
        inKeys = apParameters.inKeys(),
        inValues = apJayaAlgorithmResult,
        outKeys = apParameters.outKeys()
    )
    _log_('[apJayaIterationBuilder] completed] ')
    return parameters


if __name__ == '__main__':
    filepath = os.path.abspath(__file__)
    filedir = os.path.dirname(filepath)
    os.chdir(filedir)
    print('CWD: ' + os.getcwd())
    print('File: ' + filepath)
    cwdp = lambda x: os.path.join(filedir, x)
    #__________________________________________________________
    
    
    apParameters = APParameters()
    apJaya = APJaya(
        kids_number = 5,
        parameters = apParameters
    )

    apHandle = APHandle(
        '',
        apParameters,
        WBInterface(),
        iterationCount = 200,
        iterationBuilder = apJayaIterationBuilder
    )
    
    apHandle.run()





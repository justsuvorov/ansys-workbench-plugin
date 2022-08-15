# Script by Vladimir Suvorov

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Jaya algorithm for optimization problems
import random
import os
#from numpy import loadtxt
from goalFunction import goalFunction
from Logger import Logger


class APPSO:
    def __init__(self, 
        swarm_number,
        parameters
    ):
        self._logger = Logger('log.txt')
        self._log_ = self._logger.log
        self._resultLog = Logger('ap_jaya_results.txt')
        self._resultLog_ = self._resultLog.log
        self.__iteration = 0                #Iteration for output
        self.parameters = parameters
        self.swarm_number = swarm_number
        self.goal_function_min = []
        self.swarm = []
        self.filepath = os.path.abspath(__file__)
        self.filedir = os.path.dirname(self.filepath)
        self.results = []
        self.best = 0
        self.w = 0.9
        self.P_local_best = []
        self.P_global_best = []
        self.velocity = []
        self.goal_function = []
        self._initialization_completed = False
        self._log_('[APPSO]: ' + self.__class__.__name__)

    def __initialization (self):
        self._log_('[APPSO.__initialization]')
        self._log_(str (self.swarm_number))
        for i in range(self.swarm_number):
            self.swarm.append([])
            self.P_local_best([])

            for j in range(len(self.parameters.inKeys())):
                self.swarm[i].append(0)
                if i == 0:
                    self.swarm[i].append(
                        self.parameters.inValues()[0][j]
                    )
                    self.P_local_best[i].append(self.swarm[i])
                    
                else:
                    self.swarm[i].append(
                        self.parameters.inValues()[0][j] +
                                    random.randint(-8, 8) / 2
                    )
                    self.P_local_best[i].append(self.swarm[i])

       # self.parameters.inValues() =  self.kids
        self._log_('[APPSO.__initialization] Initialization completed')
        self._resultLog_('Initialization completed')

        return self.swarm
        

    def algorithm(self, 
        index,
        outParams
    ):

        self._log_('[APPSO.algorithm] index: ' + str(index))
        if (index == 0):
           return self. __initialization()
        else:
            return self.__algorithm(outParams)            
        
    def __restictions (self):
       self._log_('[APPSO] no restrictions')
    
    def __algorithm(self, outParams):
        c1 = 1.494
        c2 = 1.494
        self.omega = self.omega - 0.5/200
        
        self._log_('[APPSO.__algorithm]')
        self.__iteration = self.__iteration + 1
        self._resultLog_('Iteration' + str(self.__iteration) + ' completed' )
        self._resultLog_('initialization_completed: '+ str(self._initialization_completed))
        self.results = outParams
        if self._initialization_completed == False:
            for j in range(self.swarm_number):
                self.goal_function.append(goalFunction(self.results[j]))
                self.goal_function_min(self.goal_function[j])
                self.velocity.append(0)
            self.best = min(self.goal_function)
            for j in range(self.swarm_number):
                self.P_global_best.append(self.swarm[self.goal_function.index(self.best)])
                
            
            self._resultLog_('Best swarm' + str(self.goal_function.index(self.best)))
            self._initialization_completed = True


        else: 
            for j in range(self.swarm_number):
                self.goal_function[j] = goalFunction(self.results[j])
                if self.goal_function[j] < self.goal_function_min[j]:
                    self._resultLog_('New best local goal_function')
                    self.goal_function_min[j] = self.goal_function[j]
                    for k in range(len(self.parameters.inKeys())):
                        self.P_local_best[j][k] = self.swarm[j][k]
             
            for j in range(self.swarm):
                if self.goal_function[j] < self.best:
                    self._resultLog_('New best')
                    self.best = self.goal_function[j]
                    self.P_global_best = self.swarm[j]
          
        self._resultLog_('Iteration ' + str(self.__iteration) + ' completed. Goal functions are ' + str(self.goal_function))
        self._resultLog_('Best kid is ' + str(self.goal_function.index(self.best)) + ' ' + str(self.best_kid))
        
        for j in range(self.swarm_number):
            for k in range(len(self.parameters.inKeys())):
                r1 = random.random()
                r2 = random.random()
                self.velosity[j]= self.velosity[j] *self. omega + c1 * r1 * (self.P_local_best[k] - self.swarm[j][k]) + c2 * r2 * (self.P_global_best[k] - self.swarm[j][k]) 
                self.swarm[j][k]= self.swarm[j][k] + self.velosity[j]
     
        self._log_('[APPSO.__algorithm] completed')
        return self.swarm
            
            
    



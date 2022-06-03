# Script by Vladimir Suvorov

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Jaya algorithm for optimization problems
import random
import os
#from numpy import loadtxt
from goalFunction import goalFunction
from Logger import Logger


class APJaya:
    def __init__(self, 
        kids_number,
        parameters
    ):
        self._logger = Logger('log.txt')
        self._log_ = self._logger.log
        self._resultLog = Logger('ap_jaya_results.txt')
        self._resultLog_ = self._resultLog.log
        self.__iteration = 0                #Iteration for output
        self.parameters = parameters
        self.kids_number = kids_number
        self.goal_function_temp = []
        self.kids = []
        self.kids_temp = []
        self.filepath = os.path.abspath(__file__)
        self.filedir = os.path.dirname(self.filepath)
        self.results = []
        self.best = 0
        self.worst = 0
        self.best_kid = []
        self.worst_kid = []
        self.goal_function = []
        self._initialization_completed = False
        self._log_('[APJaya]: ' + self.__class__.__name__)

    def __initialization (self):
        self._log_('[APJaya.__initialization]')
        self._log_(str (self.kids_number))
        for i in range(self.kids_number):
            #self._log_('[APJaya.__initialization begin child]')
            self.kids.append([])
            self.kids_temp.append([])
            self.goal_function_temp.append(0)

            for j in range(len(self.parameters.inKeys())):
                self.kids_temp[i].append(0)
                if i == 0:
                    self.kids[i].append(
                        self.parameters.inValues()[0][j]
                    )
                else:
                    self.kids[i].append(
                        self.parameters.inValues()[0][j] +
                                    random.randint(-8, 8) / 2
                    )



          
       # self.parameters.inValues() =  self.kids
        self._log_('[APJaya.__initialization] Initialization completed')
        self._resultLog_('Initialization completed')

        return self.kids
        

    def algorithm(self, 
        index,
        outParams
    ):

        self._log_('[APJaya.algorithm] index: ' + str(index))
        if (index == 0):
           return self. __initialization()
        else:
            return self.__algorithm(outParams)            
        
    def __restictions (self):
       self._log_('[APJaya] no restrictions')
    
    def __algorithm(self, outParams):
        self._log_('[APJaya.__algorithm]')
        self.__iteration = self.__iteration + 1
        self._resultLog_('Iteration' + str(self.__iteration) + ' completed' )

        self.results = outParams
        if self._initialization_completed == False:
            for j in range(self.kids_number):
                self.goal_function.append(goalFunction(self.results[j]))
            self.best = min(self.goal_function)
            self.best_kid = self.kids[self.goal_function.index(self.best)]
            self.worst = max(self.goal_function)
            self.worst_kid = self.kids[self.goal_function.index(self.worst)]
            self._initialization_completed == True

        else: 
            for j in range(self.__kids_number):
                self.goal_function_temp[j] = goalFunction(self.results[j])
                if self.goal_function_temp[j] < self.goal_function[j]:
                    self.goal_function[j] = self.goal_function_temp[j]
                    for k in range(len(self.parameters.inKeys())):
                        self.kids[j][k] = self.kids_temp[j][k]
            worst_temp = max(self.goal_function) 
            for j in range(self.kids_number):
                if self.goal_function[j] < self.best:
                    self.best = self.goal_function[j]
                    self.best_kid = self.kids[self.goal_function.index(self.best)]
              #      self._resultLog_('New best')
                if worst_temp < self.worst:
                    self.worst = worst_temp
                    self.worst_kid = self.kids[self.goal_function.index(self.worst)]
        #            self._resultLog_('New worst')
        self._resultLog_('Iteration ' + str(self.__iteration) + ' completed. Goal functions are ' + str(self.goal_function))
        self._resultLog_('Best kid is ' + str(self.goal_function.index(self.best)) + ' ' + str(self.best_kid))
        for j in range(self.kids_number):
            for k in range(len(self.parameters.inKeys())):
                r1 = random.random()
                r2 = random.random()
                self.kids_temp[j][k] = self.kids[j][k] + r1 * (self.best_kid[k] - abs(self.kids[j][k])) - \
                             r2 * ((self.worst_kid[k] - abs(self.kids[j][k])))
                self.kids_temp[j][k] =  round(self.kids_temp[j][k]*2) / 2
        self._log_('[APJaya.__algorithm] completed')

        return self.kids_temp 
            
            
    



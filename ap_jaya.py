# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import os
#from numpy import loadtxt
from goalFunction import goalFunction
params = {
    'inKeys': ['p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p120', 'p123', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p140', 'p143', 'p145', 'p146', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165', 'p166', 'p167', 'p168', 'p169', 'p170', 'p171', 'p172', 'p173', 'p174', 'p175', 'p176', 'p177', 'p178', 'p179', 'p180', 'p181'],
    'inValues': [16.5, 18.5, 27.0, 25.0, 27.0, 21.0, 20.0, 20.0, 20.0, 31.0, 25.0, 21.5, 20.5, 20.0, 28.0, 20.0, 11.0, 14.0, 12.5, 21.5, 23.5, 20.5, 25.0, 22.5, 30.0, 23.0, 29.0, 22.5, 20.0, 17.5, 17.5,17.0, 19.5, 44.5, 19.5, 16.0, 12.0, 17.0, 20.5,12.0, 16.0, 11.5, 25.0, 16.0, 19.5, 16.0, 15.0, 14.0, 16.0, 7.0, 11.0, 33.5, 11.0, 15.5, 23.0, 18.5, 13.5, 17.0, 15.0, 14.5, 11.0, 9.5, 11.5, 10.0, 21.0, 16.0, 10.0, 9.0, 15.0, 22.5, 16.0, 15.5, 16.5, 12.5, 22.0, 12.0, 20.5, 11.0, 10.0, 10.0, 8.5, 8.5, 8.5, 9.5, 9.5, 9.5, 11.5, 13.0, 8.5],
         
    'outKeys': ['p36', 'p33', 'p35', 'p34', 'p50', 'p76', 'p56', 'p79', 'p52', 'p77', 'p54', 'p78', 'p57', 'p58', 'p80'],
}


class APJaya:
    def __init__(self, 
        kids_number,
        parameters
    ):
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
 
    def __initialization (self):
        for i in range(self.kids_number):
            self.kids.append([])
            self.kids_temp.append([])
            self.goal_function_temp.append(0)
            for j in range(len(self.parameters['inKeys'])):
                self.kids_temp[i].append(0)
                if i == 0:
                    self.kids[i].append(self.parameters['inValues'][j])
                else:
                    self.kids[i].append(self.parameters['inValues'][j] +
                                        random.randint(-round(self.parameters['inValues'][j]),round(self.parameters['inValues'][j])) / 2)
          
        self.parameters['inValues'] =  self.kids  
        print('Initialization completed')
        return self.kids
        

    def algorithm(self, 
        index,
        outParams
    ):
        if (index == 0):
           return self. __initialization()
        else:
            return self.__algorithm(outParams)            
        
    def __restictions (self):
       print('no restrictions')
    
    def __algorithm(self, outParams):
        self.__iteration = self.__iteration + 1
        #self.results = loadtxt(self.filedir+"\output.txt",delimiter=",")
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
                    for k in range(len(self.parameters['inKeys'])):
                        self.kids[j][k] = self.kids_temp[j][k]
            worst_temp = max(self.goal_function) 
            for j in range(self.kids_number):
                if self.goal_function[j] < self.best:
                    self.best = self.goal_function[j]
                    self.best_kid = self.kids[self.goal_function.index(self.best)]
                    print('New best')
                if worst_temp < self.worst:
                    self.worst = worst_temp
                    self.worst_kid = self.kids[self.goal_function.index(self.worst)]
                    print('New worst')
        print('Iteration ',self.__iteration, ' completed. Goal functions are ', self.goal_function)
        print('best kid is ', self.goal_function.index(self.best), ' ', self.best_kid)
        for j in range(self.kids_number):
            for k in range(len(self.parameters['inKeys'])):
                r1 = random.random()
                r2 = random.random()
                self.kids_temp[j][k] = self.kids[j][k] + r1 * (self.best_kid[k] - abs(self.kids[j][k])) - \
                             r2 * ((self.worst_kid[k] - abs(self.kids[j][k])))
                self.kids_temp[j][k] =  round(self.kids_temp[j][k]*2) / 2
                

   

        return self.kids_temp 
            
            
    



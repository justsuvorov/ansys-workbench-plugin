# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random
from random import randint
import subprocess
import os
from numpy import loadtxt
import ap_parameters
from goalFunction import goalFunction
params = {
    'inKeys': ['p83', 'p84', 'p85', 'p86', 'p87', 'p88', 'p89', 'p90', 'p91', 'p92', 'p93', 'p94', 'p95', 'p96', 'p97', 'p100', 'p101', 'p102', 'p103', 'p104', 'p105', 'p106', 'p107', 'p108', 'p109', 'p110', 'p111', 'p112', 'p113', 'p114', 'p115', 'p116', 'p117', 'p118', 'p120', 'p123', 'p125', 'p126', 'p127', 'p128', 'p129', 'p130', 'p131', 'p132', 'p133', 'p134', 'p135', 'p136', 'p137', 'p138', 'p140', 'p143', 'p145', 'p146', 'p147', 'p148', 'p149', 'p150', 'p151', 'p152', 'p153', 'p154', 'p155', 'p156', 'p157', 'p158', 'p159', 'p160', 'p161', 'p162', 'p163', 'p164', 'p165', 'p166', 'p167', 'p168', 'p169', 'p170', 'p171', 'p172', 'p173', 'p174', 'p175', 'p176', 'p177', 'p178', 'p179', 'p180', 'p181'],
    'inValues': [16.5, 18.5, 27.0, 25.0, 27.0, 21.0, 20.0, 20.0, 20.0, 31.0, 25.0, 21.5, 20.5, 20.0, 28.0, 20.0, 11.0, 14.0, 12.5, 21.5, 23.5, 20.5, 25.0, 22.5, 30.0, 23.0, 29.0, 22.5, 20.0, 17.5, 17.5,17.0, 19.5, 44.5, 19.5, 16.0, 12.0, 17.0, 20.5,12.0, 16.0, 11.5, 25.0, 16.0, 19.5, 16.0, 15.0, 14.0, 16.0, 7.0, 11.0, 33.5, 11.0, 15.5, 23.0, 18.5, 13.5, 17.0, 15.0, 14.5, 11.0, 9.5, 11.5, 10.0, 21.0, 16.0, 10.0, 9.0, 15.0, 22.5, 16.0, 15.5, 16.5, 12.5, 22.0, 12.0, 20.5, 11.0, 10.0, 10.0, 8.5, 8.5, 8.5, 9.5, 9.5, 9.5, 11.5, 13.0, 8.5],
         
    'outKeys': ['p36', 'p33', 'p35', 'p34', 'p50', 'p76', 'p56', 'p79', 'p52', 'p77', 'p54', 'p78', 'p57', 'p58', 'p80'],
}


class Jaya:
    def __init__(self, iterations, kids_number, parameters):
        self.__iterations = iterations
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
        
        
        
    def initialization (self):
        for i in range(self.kids_number):
            self.kids.append([])
            self.kids_temp.append([])
            self.goal_function_temp.append(0)
            for j in range(len(self.parameters['inKeys'])):
                self.kids_temp[i].append(0)
                if i == 0:
                    self.kids[i].append(self.parameters['inValues'][j])
                else:
                    self.kids[i].append(self.parameters['inValues'][j]) #+ random.random((-self.parameters['inValues'][j],self.parameters['inValues'][j]) / 2))
           # здесь нужно записать новые параметры inValues
            #subprocess.run(self.filedir+r'\run.bat', cwd = self.filedir)
            self.results = loadtxt(self.filedir+"\output.txt",delimiter=",")
            for j in range(self.kids_number):
                self.goal_function.append(goalFunction(self.results[j]))
            self.best = min(self.goal_function)
            self.best_kid = self.kids[self.goal_function.index(self.best)]
            self.worst = max(self.goal_function)
            self.worst_kid = self.kids[self.goal_function.index(self.worst)]
            print('Initialization completed. Goal functions are ', self.goal_function)
            print('best kid is ', self.goal_function.index(self.best), ' ', self.best_kid)

                
        
    def restictions (self):
       print('no restrictions')
    
    def algorithm(self):
        for i in range(self.__iterations):
            for j in range(self.__kids_number):
                for k in range(len(self.parameters['inKeys'])):
                    r1 = random.random()
                    r2 = random.random()
                    self.kids_temp[j][k] = self.kids[j][k] + r1 * (self.best_kid[k] - abs(self.kids[j][k])) - \
                             r2 * ((self.worst_kid[k] - abs(self.kids[i][k])))
                    self.kids_temp[j][k] =  round(self.kids_temp[j][k]*2) / 2
                   
                    #здесь записываем ин values
                    #self.parameters['inValues'][j][k] = 
                #restrictions!!!
            #subprocess.run(self.filedir+r'\run.bat', cwd = self.filedir)
            self.results = loadtxt(self.filedir+"\output.txt",delimiter=",")
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
            print('Iteration ', i+1,' completed. Goal functions are ', self.goal_function)
            print('best kid is ', self.goal_function.index(self.best), ' ', self.best_kid)
            
            
            
    


optimization = Jaya(10,1,params)
print(len(params['inValues']))
print(params['inKeys'][2])
optimization.initialization()    
print(optimization.results) 
        
        
"""



# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    print('Hi' )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# алгоритм Джая


goal_function = []
mass = []
for i in range (kids_number):
    mass.append(0)
    goal_function.append(0)

# имена входных параметров
parameters = [83, 84, 85, 86, 87, 88, 89, 90,
              91, 92, 93, 94, 95, 96, 97, 100,
              101, 102, 103, 104, 105, 106, 107,
              108, 109, 110, 111, 112, 113, 114, 115,
              116, 117, 118, 120, 123, 125, 126, 127,
              128, 129, 130, 131, 132, 133, 134, 135,
              136, 137, 138, 140, 143, 145, 146, 147,
              148, 149, 150, 151, 152, 153, 154, 155, 156,
              157, 158, 159, 160, 161, 162, 163, 164, 165,
              166, 167, 168, 169, 170, 171, 172, 173, 174,
              175, 176, 177, 178, 179, 180, 181]
# имена выходных параметров
output_parameters = [36, 33, 35, 34, 50, 76, 56, 79, 52, 77, 54, 78, 57, 58, 80]

# запись имен pпараметров в файл control.csv
with open(workdir + '\_control.csv', 'w', newline='') as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(parameters)
    write.writerow(output_parameters)

# начальные приближения радиусов
"""
initial_radiuses = [15, 20, 22, 21, 27, 28, 25, 22, 21, 28,
                    27, 26, 25, 25, 25, 24, 21, 20, 20, 19,
                    19, 19, 19, 19, 18, 19, 19, 19, 18, 18,
                    18, 17, 17, 17, 17, 17, 17, 17, 12, 12,
                    12, 13, 20, 16, 20, 19, 18, 16, 12, 7,
                    7, 7, 11, 20, 16, 16, 14, 11, 11, 13,
                    13, 13, 13, 13, 12, 12, 12, 10, 10, 20,
                    19, 16, 16, 10, 20, 11, 16, 11, 11, 11,
                    11, 11, 11, 11, 11, 11, 10, 8, 11]
"""
initial_radiuses = [16.5, 18.5, 27.0, 25.0, 27.0, 21.0, 20.0, 20.0, 
                   20.0, 31.0, 25.0, 21.5, 20.5, 20.0, 28.0, 20.0, 
                   11.0, 14.0, 12.5, 21.5, 23.5, 20.5, 25.0, 
                   22.5, 30.0, 23.0, 29.0, 22.5, 20.0, 17.5, 17.5,
                   17.0, 19.5, 44.5, 19.5, 16.0, 12.0, 17.0, 20.5,
                   12.0, 16.0, 11.5, 25.0, 16.0, 19.5, 16.0, 15.0, 
                   14.0, 16.0, 7.0, 11.0, 33.5, 11.0, 15.5, 23.0, 
                   18.5, 13.5, 17.0, 15.0, 14.5, 11.0, 9.5, 11.5, 10.0, 
                   21.0, 16.0, 10.0, 9.0, 15.0, 22.5, 16.0, 15.5, 16.5, 
                   12.5, 22.0, 12.0, 20.5, 11.0, 10.0, 10.0, 8.5, 8.5, 
                   8.5, 9.5, 9.5, 9.5, 11.5, 13.0, 8.5]                 
# проверка на равенство параметров и входных значений
if len(initial_radiuses) != len(parameters):
    raise Exception('Число параметров и радиусов не соответсвует друг другу')

# генерируем начальные приближения
kids = []
kids_temp = []
for i in range(kids_number):
    kids.append([])
    kids_temp.append([])
    for j in range(len(parameters)):
        kids_temp[i].append(0)
       # if i == 0:
      #      kids[i].append(initial_radiuses[j])
     #   else:
    #        kids[i].append(initial_radiuses[j] + random.randint(-5, 5) / 2)
        kids[i].append(40 + random.randint(-20, 20) / 2)
    #ровинги второй секции
    
    for j in range (110,116):
        if kids[i][parameters.index(j+1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j+1)] = \
            kids[i][parameters.index(j)]
   #ровинги второй секции
    for j in range (101,107):
        if kids[i][parameters.index(j+1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j+1)] = \
            kids[i][parameters.index(j)]
       #ровинги второй секции
    for j in range (150,156):
        if kids[i][parameters.index(j+1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j+1)] = \
            kids[i][parameters.index(j)]        
    #нижние ровинги первой секции
   # if kids[i][parameters.index(146)] > kids[i][parameters.index(167)]: kids[i][parameters.index(146)] =\
    #    kids[i][parameters.index(167)]
    for j in range(146, 148):    
        if kids[i][parameters.index(j + 1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j + 1)] = \
            kids[i][parameters.index(j)]
    for j in range(88, 91):    
        if kids[i][parameters.index(j + 1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j + 1)] = \
            kids[i][parameters.index(j)]
    #Верхние ровинги первой секции
    for j in range(93, 96):
        if kids[i][parameters.index(j + 1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j + 1)] = \
            kids[i][parameters.index(j)]
   
    # верхние ровинги третьей секции
    
    if kids[i][parameters.index(157)] > kids[i][parameters.index(126)]: kids[i][parameters.index(157)] =\
        kids[i][parameters.index(126)]
    if kids[i][parameters.index(127)] > kids[i][parameters.index(157)]: kids[i][parameters.index(127)] =\
        kids[i][parameters.index(157)]
    if kids[i][parameters.index(158)] > kids[i][parameters.index(127)]: kids[i][parameters.index(158)] =\
        kids[i][parameters.index(127)]
    if kids[i][parameters.index(128)] > kids[i][parameters.index(158)]: kids[i][parameters.index(128)] =\
        kids[i][parameters.index(158)]
    if kids[i][parameters.index(159)] > kids[i][parameters.index(128)]: kids[i][parameters.index(159)] =\
        kids[i][parameters.index(128)]
    if kids[i][parameters.index(129)] > kids[i][parameters.index(159)]: kids[i][parameters.index(129)] =\
        kids[i][parameters.index(159)]
    if kids[i][parameters.index(160)] > kids[i][parameters.index(129)]: kids[i][parameters.index(160)] =\
        kids[i][parameters.index(129)]
    if kids[i][parameters.index(130)] > kids[i][parameters.index(160)]: kids[i][parameters.index(130)] =\
        kids[i][parameters.index(160)]
    if kids[i][parameters.index(161)] > kids[i][parameters.index(130)]: kids[i][parameters.index(161)] =\
        kids[i][parameters.index(130)]  
    if kids[i][parameters.index(179)] > kids[i][parameters.index(161)]: kids[i][parameters.index(179)] =\
        kids[i][parameters.index(161)]
    
      # боковые ровинги третьей секции
    
    if kids[i][parameters.index(170)] > kids[i][parameters.index(166)]: kids[i][parameters.index(170)] =\
        kids[i][parameters.index(166)]
    for j in range(170, 178):    
        if kids[i][parameters.index(j + 1)] > kids[i][parameters.index(j)]: kids[i][parameters.index(j + 1)] = \
            kids[i][parameters.index(j)]  
    if kids[i][parameters.index(181)] > kids[i][parameters.index(178)]: kids[i][parameters.index(181)] =\
        kids[i][parameters.index(178)] 
        
   # нижние ровинги третьей секции

      
    if kids[i][parameters.index(162)] > kids[i][parameters.index(133)]: kids[i][parameters.index(162)] =\
        kids[i][parameters.index(133)]
    if kids[i][parameters.index(134)] > kids[i][parameters.index(162)]: kids[i][parameters.index(134)] =\
        kids[i][parameters.index(162)]
    if kids[i][parameters.index(163)] > kids[i][parameters.index(134)]: kids[i][parameters.index(163)] =\
        kids[i][parameters.index(134)]
    if kids[i][parameters.index(135)] > kids[i][parameters.index(163)]: kids[i][parameters.index(135)] =\
        kids[i][parameters.index(163)]
    if kids[i][parameters.index(164)] > kids[i][parameters.index(135)]: kids[i][parameters.index(164)] =\
        kids[i][parameters.index(135)]
    if kids[i][parameters.index(136)] > kids[i][parameters.index(164)]: kids[i][parameters.index(136)] =\
        kids[i][parameters.index(164)]
    if kids[i][parameters.index(165)] > kids[i][parameters.index(136)]: kids[i][parameters.index(165)] =\
        kids[i][parameters.index(136)]
    if kids[i][parameters.index(137)] > kids[i][parameters.index(165)]: kids[i][parameters.index(137)] =\
        kids[i][parameters.index(165)]  
    if kids[i][parameters.index(149)] > kids[i][parameters.index(137)]: kids[i][parameters.index(149)] =\
        kids[i][parameters.index(137)]     
    if kids[i][parameters.index(180)] > kids[i][parameters.index(149)]: kids[i][parameters.index(180)] =\
        kids[i][parameters.index(149)] 
  







        
# записываем начальные приближения в файл input.csv
with open(workdir + '\_input.csv', 'w', newline='') as f:
    write = csv.writer(f, delimiter=',')
    write.writerows(kids)
   
# запуск решателя
subprocess.run(workdir + r'\run.bat', cwd = workdir)

minStress = -268
maxDisplacement = 200
#чтение параметров из output
results = loadtxt(workdir+"\output.txt",delimiter=",")
best_mass = 3000
#Значения целевой функции
for i in range(kids_number):
    goal_function[i] = round(results[i][0])
    mass[i] = round(results[i][0])
    if mass[i] < best_mass: best_mass = mass[i]
    if results[i][2] > maxDisplacement:  goal_function[i] += round(
        ((maxDisplacement - results[i][2]) / 10 * results[i][0]))
    # print(results[i][2]) #Displacement
    if (results[i][1] / 1000000) < minStress: goal_function[i] += round(((minStress - results[i][1]/1000000) / 100 * results[i][0]))
    #print(results[i][1]/1000000) #stress1
    for j in range(4, 11, 2):
        if results[i][j] < minStress: goal_function[i] += round(((minStress - results[i][j])/100 * results[i][0]))
    for j in range(3, 12, 2):
        if results[i][j] < 1.5: goal_function[i] += round(((1.5 - results[i][j]) * results[i][0]))
    if results[i][12] > maxDisplacement:  goal_function[i] += round(
        ((maxDisplacement - results[i][12]) / 10 * results[i][0]))
    if results[i][13] < minStress: goal_function[i] += round(((minStress - results[i][13]) / 100 * results[i][0]))
    if results[i][14] < 1.5: goal_function[i] += round(((1.5 - results[i][14]) * results[i][0]))

#Определение лучших и худших
best = min(goal_function)
best_kid = kids[goal_function.index(best)]
worst = max(goal_function)
worst_kid = kids[goal_function.index(worst)]
best_mass = mass[goal_function.index(best)]

print('Initial stage completed. Goal functions are ', goal_function)
print('Mass is ', best_mass)
print('best kid is ', goal_function.index(best), ' ', best_kid)



goal_function_temp = []


for i in range(kids_number):
    goal_function_temp.append(0)
   

# Оптимизация

for j in range(iterations):
    for i in range(kids_number):
        for k in range(len(parameters)):
            r1 = random.random()
            r2 = random.random()
            kids_temp[i][k] = kids[i][k] + r1 * (best_kid[k] - abs(kids[i][k])) - \
                              r2 * ((worst_kid[k] - abs(kids[i][k])))
            kids_temp[i][k] =  round(kids_temp[i][k]*2) / 2
          
        for jj in range (110,116):
                if kids[i][parameters.index(jj+1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj+1)] = \
                        kids[i][parameters.index(jj)]
                #ровинги второй секции
        for jj in range (101,107):
                if kids[i][parameters.index(jj-1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj-1)] = \
                        kids[i][parameters.index(jj)]
           #ровинги второй секции
        for jj in range (150,156):
               if kids[i][parameters.index(jj+1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj+1)] = \
                        kids[i][parameters.index(jj)]        
                        #нижние ровинги первой секции
        if kids[i][parameters.index(146)] > kids[i][parameters.index(167)]: kids[i][parameters.index(146)] =\
                    kids[i][parameters.index(167)]
        for jj in range(146, 148):    
                if kids[i][parameters.index(jj + 1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj + 1)] = \
                        kids[i][parameters.index(jj)]
        for jj in range(88, 91):    
                if kids[i][parameters.index(jj + 1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj + 1)] = \
                        kids[i][parameters.index(jj)]
                        #Верхние ровинги первой секции
        for jj in range(94, 96):
                if kids[i][parameters.index(jj + 1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj + 1)] = \
                        kids[i][parameters.index(jj)]
                   # верхние ровинги третьей секции
        if kids[i][parameters.index(157)] > kids[i][parameters.index(126)]: kids[i][parameters.index(157)] =\
                    kids[i][parameters.index(126)]
        if kids[i][parameters.index(127)] > kids[i][parameters.index(157)]: kids[i][parameters.index(127)] =\
                    kids[i][parameters.index(157)]
        if kids[i][parameters.index(158)] > kids[i][parameters.index(127)]: kids[i][parameters.index(158)] =\
                    kids[i][parameters.index(127)]
        if kids[i][parameters.index(128)] > kids[i][parameters.index(158)]: kids[i][parameters.index(128)] =\
                    kids[i][parameters.index(158)]
        if kids[i][parameters.index(159)] > kids[i][parameters.index(128)]: kids[i][parameters.index(159)] =\
                    kids[i][parameters.index(128)]
        if kids[i][parameters.index(129)] > kids[i][parameters.index(159)]: kids[i][parameters.index(129)] =\
                    kids[i][parameters.index(159)]
        if kids[i][parameters.index(160)] > kids[i][parameters.index(129)]: kids[i][parameters.index(160)] =\
                    kids[i][parameters.index(129)]
        if kids[i][parameters.index(130)] > kids[i][parameters.index(160)]: kids[i][parameters.index(130)] =\
                    kids[i][parameters.index(160)]
        if kids[i][parameters.index(161)] > kids[i][parameters.index(130)]: kids[i][parameters.index(161)] =\
                    kids[i][parameters.index(130)]  
        if kids[i][parameters.index(179)] > kids[i][parameters.index(161)]: kids[i][parameters.index(179)] =\
                    kids[i][parameters.index(161)]
        
          # боковые ровинги третьей секции
        
        if kids[i][parameters.index(170)] > kids[i][parameters.index(166)]: kids[i][parameters.index(170)] =\
                    kids[i][parameters.index(166)]
        for jj in range(170, 178):    
                    if kids[i][parameters.index(jj + 1)] > kids[i][parameters.index(jj)]: kids[i][parameters.index(jj + 1)] = \
                        kids[i][parameters.index(jj)]  
        if kids[i][parameters.index(181)] > kids[i][parameters.index(178)]: kids[i][parameters.index(181)] =\
                    kids[i][parameters.index(178)] 
            
       # нижние ровинги третьей секции
    
                  
        if kids[i][parameters.index(162)] > kids[i][parameters.index(133)]: kids[i][parameters.index(162)] =\
                    kids[i][parameters.index(133)]
        if kids[i][parameters.index(134)] > kids[i][parameters.index(162)]: kids[i][parameters.index(134)] =\
                    kids[i][parameters.index(162)]
        if kids[i][parameters.index(163)] > kids[i][parameters.index(134)]: kids[i][parameters.index(163)] =\
                    kids[i][parameters.index(134)]
        if kids[i][parameters.index(135)] > kids[i][parameters.index(163)]: kids[i][parameters.index(135)] =\
                    kids[i][parameters.index(163)]
        if kids[i][parameters.index(164)] > kids[i][parameters.index(135)]: kids[i][parameters.index(164)] =\
                    kids[i][parameters.index(135)]
        if kids[i][parameters.index(136)] > kids[i][parameters.index(164)]: kids[i][parameters.index(136)] =\
                    kids[i][parameters.index(164)]
        if kids[i][parameters.index(165)] > kids[i][parameters.index(136)]: kids[i][parameters.index(165)] =\
                    kids[i][parameters.index(136)]
        if kids[i][parameters.index(137)] > kids[i][parameters.index(165)]: kids[i][parameters.index(137)] =\
                    kids[i][parameters.index(165)]  
        if kids[i][parameters.index(149)] > kids[i][parameters.index(137)]: kids[i][parameters.index(149)] =\
                    kids[i][parameters.index(137)]     
        if kids[i][parameters.index(180)] > kids[i][parameters.index(149)]: kids[i][parameters.index(180)] =\
                    kids[i][parameters.index(149)] 
        
        
  

    
            
            
           
        with open(workdir + '\_input.csv', 'w', newline='') as f:
            write = csv.writer(f, delimiter=',')
            write.writerows(kids_temp)

     # запуск решателя
    subprocess.run(workdir + r'\run.bat', cwd = workdir)
    print("Solved")

    #чтение параметров из output

    results = loadtxt(workdir+"\output.txt",delimiter=",")
    print("Reading results")
        #РАсчет целевых функций
    for i in range(kids_number):
        goal_function_temp[i] = round(results[i][0])
        mass[i] = round(results[i][0])
        
        if results[i][2] > maxDisplacement:  goal_function_temp[i] += round(
        ((maxDisplacement - results[i][2]) / 10 * results[i][0]))
    # print(results[i][2]) #Displacement
        if (results[i][1] / 1000000) < minStress: goal_function_temp[i] += round(
            ((minStress - results[i][1] / 1000000) / 100 * results[i][0]))
        # print(results[i][1]/1000000) #stress1
        for k in range(4, 11, 2):
            if results[i][k] < minStress: goal_function_temp[i] += round(((minStress - results[i][k]) / 100 * results[i][0]))
        for k in range(3, 12, 2):
            if results[i][k] < 1.5: goal_function_temp[i] += round(((1.5 - results[i][k]) * results[i][0]))
        if results[i][12] > maxDisplacement:  goal_function_temp[i] += round(
            ((maxDisplacement - results[j][12]) / 10 * results[i][0]))
        if results[i][13] < minStress: goal_function_temp[i] += round(((minStress - results[i][13]) / 100 * results[i][0]))
        if results[i][14] < 1.5: goal_function_temp[i] += round(((1.5 - results[i][14]) * results[i][0]))
        if goal_function_temp[i] < goal_function[i]:
            goal_function[i] = goal_function_temp[i]
            for k in range(len(parameters)):
                kids[i][k] = kids_temp[i][k]


    worst_temp = max(goal_function)
    for i in range(kids_number):
        if goal_function[i] < best:
            best = goal_function[i]
            best_kid = kids[i]
            best_mass = mass[i]
            print('New best')
        if worst_temp < worst:
            worst = worst_temp
            worst_kid = kids[goal_function.index(worst)]
            print('New worst')

    print('Iteration ', j+1,' completed. Goal functions are ', goal_function)
    print('Mass is ', best_mass)
    print('best kid is ', goal_function.index(best), ' ', best_kid)

# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




import subprocess
import csv




def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == "__main__":
    print('Hi' )
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# алгоритм Джая
workdir = r'E:\ANSYS\Optimization Python'

# имена входных параметров
parameters = [83, 84, 85, 86, 87, 88, 89, 90,
              91, 92, 93, 94, 95, 96, 97, 100,
              101, 102, 103, 104, 105, 106, 107,
              108, 109, 110, 111, 112, 113, 114, 115,
              116, 117, 118, 120, 123, 125, 126, 127,
              128, 129, 130, 131, 132, 133, 134, 135,
              136, 137, 138, 140, 143, 145, 146, 147,
              148, 149, 150, 151, 152, 153, 154, 155, 156,
              157, 158, 159, 160, 161, 162, 163, 164, 165,
              166, 167, 168, 169, 170, 171, 172, 173, 174,
              175, 176, 177, 178, 179, 180, 181]
# имена выходных параметров
output_parameters = [36, 33, 35, 34, 50, 76, 56, 79, 52, 77, 54, 78, 57, 58, 80]

# запись имен pпараметров в файл control.csv
with open(workdir + '\_control.csv', 'w', newline='') as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(parameters)
    write.writerow(output_parameters)

# начальные приближения радиусов
initial_radiuses =[16.5, 18.5, 27.0, 25.0, 27.0, 19.5, 24.5, 20.0, 24.0, 31.0, 16.5, 20.5, 21.5, 25.0, 28.0, 20.0, 11.0, 14.0, 12.5, 21.5, 23.5, 20.5, 25.0, 22.5, 30.0, 23.0, 29.0, 22.5, 20.0, 17.5, 17.5, 17.0, 19.5, 44.5, 19.5, 16.0, 12.0, 17.0, 20.5, 12.0, 16.0, 11.5, 25.0, 16.0, 19.5, 16.0, 15.0, 14.0, 16.0, 7.0, 11.0, 33.5, 11.0, 15.5, 23.0, 18.5, 13.5, 17.0, 15.0, 14.5, 11.0, 9.5, 11.5, 10.0, 21.0, 16.0, 10.0, 9.0, 15.0, 22.5, 16.0, 15.5, 16.5, 12.5, 22.0, 12.0, 20.5, 11.0, 10.0, 10.0, 8.5, 8.5, 8.5, 9.5, 9.5, 9.5, 11.5, 13.0, 8.5]
                  
# проверка на равенство параметров и входных значений
if len(initial_radiuses) != len(parameters):
    raise Exception('Число параметров и радиусов не соответсвует друг другу')

# генерируем начальные приближения


        
# записываем начальные приближения в файл input.csv
with open(workdir + '\_input.csv', 'w', newline='') as f:
    write = csv.writer(f, delimiter=',')
    write.writerow(initial_radiuses)
   
# запуск решателя
print('Solving...')
subprocess.run(workdir + r'\run.bat', cwd = workdir)
print('Solved')
"""

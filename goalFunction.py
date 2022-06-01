# -*- coding: utf-8 -*-
"""
Created on Fri May 27 16:06:59 2022

@author: Suvorov
"""

def goalFunction(results):
    minStress = -268
    maxDisplacement = 200
    goal_function = round(results[0])
    if results[2] > maxDisplacement:  goal_function += round(
        ((maxDisplacement - results[2]) / 10 * results[0]))
    # print(results[i][2]) #Displacement
    if (results[1] / 1000000) < minStress: goal_function += round(((minStress - results[1]/1000000) / 100 * results[0]))
    #print(results[i][1]/1000000) #stress1
    for j in range(4, 11, 2):
        if results[j] < minStress: goal_function += round(((minStress - results[j])/100 * results[0]))
    for j in range(3, 12, 2):
        if results[j] < 1.5: goal_function += round(((1.5 - results[j]) * results[0]))
    if results[12] > maxDisplacement:  goal_function += round(
        ((maxDisplacement - results[12]) / 10 * results[0]))
    if results[13] < minStress: goal_function += round(((minStress - results[13]) / 100 * results[0]))
    if results[14] < 1.5: goal_function += round(((1.5 - results[14]) * results[0]))
    return goal_function
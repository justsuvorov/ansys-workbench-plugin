import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from goalFunction import goalFunction

datadir = r'E:\ANSYS\Dissertation'

#загрузка данных из csv
inputData = np.loadtxt(datadir + '\Optimization Pythoninput parameters.csv', delimiter=",")
outputData = np.loadtxt(datadir + '\Optimization Pythonresults.csv', delimiter=",")

#формирование DataFrames
results = pd.DataFrame((outputData), columns= ['mass','stress1','Displacement','k1','stress2','k2',
                                               'stress3', 'stress4', 'stress5','k3',
                                            'stress6', 'stress7',  'stress8',  'k4' ,
                                            'stress10', 'stress11', 'stress12','k5','Displacement2',
                                               'stress13', 'stress14', 'stress15', 'k6'])


results['stress1'] = results['stress1']/1000000
parameters = pd.DataFrame(inputData)
#array fo goal function calculation
results_array = results.to_numpy()
goal_function = []

for i in range(len(results_array)):
    goal_function.append(goalFunction(results_array[i]))

results['Goal function'] = goal_function

#concat
data = pd.concat([parameters, results], axis = 1)
data1 = data.to_numpy()

U, S, V = np.linalg.svd(data1, full_matrices = False)
S = np.diag(S)

plt.figure(1)
plt.semilogy(np.diag(S))
plt.title('Singular Values')

plt.figure(2)
plt.plot(np.cumsum(np.diag(S))/np.sum(np.diag(S)))
plt.title('Singular Values: Cumulative Sum')
plt.show()

from sklearn.decomposition import PCA

transformer = PCA(n_components=20)
X_ = transformer.fit(data1)
print(transformer.explained_variance_ratio_)

from factor_analyzer.factor_analyzer import calculate_kmo
kmo_all, kmo_model = calculate_kmo(data1)
print(kmo_model)


from sklearn.decomposition import FactorAnalysis
transformer = FactorAnalysis(n_components = 12, random_state=0, rotation="varimax")
X_transformed = transformer.fit(data1)

from factor_analyzer.factor_analyzer import FactorAnalyzer
fa = FactorAnalyzer(rotation="varimax", n_factors= 12)
fa.fit(data1)
#print(fa.loadings_)
#print(results.iloc[0])
#pd.DataFrame(fa.loadings_).to_csv('E:\ANSYS\Dissertation.csv', sep =";")
#print(fa.get_communalities())
with open(datadir + 'factor.csv', 'w') as f:
    write = csv.writer(f, delimiter=";")
    write.writerows(X_transformed)

import seaborn as sns
plt.figure(figsize=(20,10))

c = sns.heatmap(data1.corr(), linewidths=.01 )
plt.show()

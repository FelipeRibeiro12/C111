import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

statusMission = len(ds[1:,7]) #quantidade de linhas da coluna 7, exceto o nome da coluna (linha 0)

statusMissionSuccess = np.sum(ds[1:,7] == 'Success') #quantidade de linhas da coluna 7, exceto o nome da coluna (linha 0), que tem o valor 'Success'

print((statusMissionSuccess/statusMission)*100,'%') #porcentagem de missoes bem sucedidas
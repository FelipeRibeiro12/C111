import os
import numpy as np

file = os.path.abspath(r'Y:\Inatel\P8\C111\space.csv')

ds = np.loadtxt(file, delimiter=';',
                dtype='str', encoding='utf-8') #carregar dataset como texto(string)

spacexCosts = ds[1:, 6][ds[1:, 1] == 'SpaceX'].astype(float) #transforma a coluna de custos onde o nome da empresa e spacex em numero

meMissionIndex = np.argmax(spacexCosts) #indice da missao mais cara

meMission = ds[1:, 4][ds[1:, 1] == 'SpaceX'][meMissionIndex] #missao mais cara

meCost = spacexCosts[meMissionIndex] #custo da missao mais cara

print(meMission, ' ', meCost)
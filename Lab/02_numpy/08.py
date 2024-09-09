import numpy as np

np.random.seed(10)
mtz = np.random.randint(1, 50, 16).reshape(4, 4)

m_linhas = np.mean(mtz, axis=1) 
print(m_linhas)

m_colunas = np.mean(mtz, axis=0)
print(m_colunas)


max_m_linhas = np.max(m_linhas)
print(max_m_linhas)

max_m_colunas = np.max(m_colunas)
print(max_m_colunas)
aluno1 = {'nome': 'aluno1',
          'media': 60,
}

#comparando a média e salvando a situacao do aluno
def situacaoAluno(aluno):
    if aluno['media'] >= 60:
        aluno['situacao'] = 'AP'
        
    elif aluno['media'] >= 30:
        aluno['situacao'] = 'NP3'
        
    elif aluno['media'] < 30:
        aluno['situacao'] = 'RP'
        
    return aluno

aluno1 = {'nome': 'aluno1', 'media': 60}
aluno1 = situacaoAluno(aluno1)

print(aluno1)
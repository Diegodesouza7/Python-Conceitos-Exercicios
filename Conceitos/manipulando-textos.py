# Fatiamento

"""frase = 'Curso em video Python'
print(frase[0:21]) # Indice inicia no 0 
print(frase[0:21:2])
print(frase[9:])
print(frase[9::3])"""

#Analise

"""frase = 'Curso em video Python'
print(len(frase)) # Faz a contagem das letras da frase
print(frase.count('o')) # Faz a contagem de quantas vezes uma letra aparece
print(frase.count('o', 0, 13)) # Faz a contagem do caracter com por range
print(frase.find('deo')) # faz a busca de strings e mostra sua posição
print('Curso' in frase) # Faz a busca de uma palavra retornando true ou false


#Transformação

print(frase.replace('Python' , 'Android')) # Substitui uma palavra pela outra
print(frase.upper()) # Deixa toda a frase em letras maiusculas
print(frase.lower()) #Deixa toda a frase em letras minusculas
print(frase.capitalize()) # Coloca toda a string em minusculo e a primeira letra maiuscula
print(frase.title()) # Coloca toda inicial de uma palavra em letra maiuscula

fr = str(str('   Aprenda Python  '))
print(fr.strip()) # Remove os espaços não utilizados na frase
print(fr.rstrip()) # Remove somente o espaço da direita da string 
print(fr.lstrip())# Remove somente o espaço da esquerda da string
"""

# Divisão

frase = str('Curso em Video Python')
print(frase.split()) # Faz a divisão da string por palavras
#Junção
print('-'.join(frase)) # Faz a junção das strings utilizando '-'




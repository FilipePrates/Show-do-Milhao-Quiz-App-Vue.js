#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import random


# In[ ]:


perg = pd.read_csv(r'C:\Users\Filipe Prates\Documents\Projects\Jovem Genios\perguntascsv.csv')
resp = pd.read_csv(r'C:\Users\Filipe Prates\Documents\Projects\Jovem Genios\respostascsv.csv')


# In[ ]:


pd.options.display.max_colwidth = 100



# In[ ]:


def printPergunta():
    for i in range(0,5):
        print(perg.iloc[indexPerg+i,:].values)
    return


# In[ ]:


def resposta():
    return resp.iloc[perguntaEscolhida][-1][-1]


# In[ ]:


#Mockup rápido de platéia
def votosPlateia():
    vote1 = 0
    vote2 = 0
    vote3 = 0
    vote4 = 0

    randPlat1 = random.random()
    votosPlat = 0
    valorMinAcertoPlat = randPlat1*0.55 + 0.35
    while(votosPlat < 100):
        randPlat2 = random.random()
        if randPlat2 < valorMinAcertoPlat:
            vote1 += 1
        else:
            randPlat3 = random.randint(2,4)
            if randPlat3 == 2: vote2 += 1
            if randPlat3 == 3: vote3 += 1
            if randPlat3 == 4: vote4 += 1
        votosPlat += 1
    return [vote1,vote2,vote3,vote4]


# In[ ]:


#Flags
perguntasFeitas = []
enable = 1
preco = [0,1000,2000,5000,10000,25000,50000,100000,150000,350000,750000,1000000]
precoI = 1
flagPlat = 1
flag50 = 1
flagUniver = 1


#Intro
print("Será que hoje alguém vai ganhar R$1.000.000? \n")
print("A qualquer momento você pode escrever UNIVERSITÁRIO (U), PLATÉIA (P), ou 50/50 (50) para usar as ajudas, lembre-se que só tem uma de cada por tentativa! Boa Sorte! \n")
print("Está pronto para jogar o jogo? Y/N \n")
a = input()
if a not in ['Sim','Y','Yes','S', 'y', 'sim', 'yes']:
    enable = 0
    
#Main Loop  
while(enable):    
    #Win-check
    if precoI == len(preco):
        print('Parabéns! UM MILHÃO DE REAIS! Você acertou todas as perguntas!')
        enable = 0
        break
    
    
    print("Valendo " + str(preco[precoI]) + " reais \n")
        
    #Escolha de Pergunta
    checkPerguntaRepetida = 1
    while(checkPerguntaRepetida):
        perguntaEscolhida = random.randint(0,62)
        if perguntaEscolhida not in perguntasFeitas:
            perguntasFeitas.append(perguntaEscolhida)
            checkPerguntaRepetida = 0
            
    indexPerg = perguntaEscolhida*5
    printPergunta()
    
    #Loop Pergunta
    aux = 1
    while(aux):
        print('Qual a resposta? 1/2/3/4 \n')
        r = input()
        
        #Check Ajudas
        
        #Universitário    
        if r.lower() in ['universitario','universitário','universitarios','universitários','u']:
            if flagUniver == 0:
                print("Parece que você já usou essa ajuda!")
            else:
                #print('#### tapa buraco enquanto arruma call de skype pro meu numero')
                univer = random.random()
                if univer < 0.05:
                    respErradas = ['Humm essa é dificil, acho que é a ', 'Putz, me pegou desprevenido, chutaria a ', 'Nossa, mínima ideia, iria com a ', 'Não sei, chuto a', 'Sei la, vai na ']
                    print(respErradas[int(univer*100)%5])
                    print("alternativa " +str(3)) if resposta() != 3 else print("alternativa " +str(2))
                if 0.05 <= univer < 0.30:
                    respMedias = ['Acho que já vi essa! Vai na', 'Quase certeza que ja aprendi essa, acho que é ', 'Confia, eu posso tar errado mas iria na ']
                    print(respMedias[int(univer*10)%3])
                    if univer > 0.20:
                        print("alternativa " +resposta())
                    else:
                        print(str(3)) if resposta() != 3 else print(str(1))
                if univer > 0.30:
                    respCertas = ['Essa é da minha área! Sei que é a ', 'Pode comemorar, essa é com certeza a ', 'Ja sei! É a ']
                    print(respCertas[int((1-univer)*10%3)])
                    print("alternativa " +resposta())
            flagUniver = 0;
            r = input()
            
        #Platéia
        elif r.lower() in ['plateia','platéia','p']:
            if flagPlat == 0:
                print("Parece que você já usou essa ajuda!")
            else:   
                plat = votosPlateia()
                print("VOTOS PLATÉIA: \n")
                print("Respostas          Votos \n")
                #Jeito burro mas funciona, se tiver tempo arrumo
                if resposta() == '1':
                    print("1     " + "#"*plat[0])
                    print("2     " + "#"*plat[1])
                    print("3     " + "#"*plat[2])
                    print("4     " + "#"*plat[3])
                if resposta() == '2':
                    print("1     " + "#"*plat[1])
                    print("2     " + "#"*plat[0])
                    print("3     " + "#"*plat[2])
                    print("4     " + "#"*plat[3])
                if resposta() == '3':
                    print("1     " + "#"*plat[2])
                    print("2     " + "#"*plat[1])
                    print("3     " + "#"*plat[0])
                    print("4     " + "#"*plat[3])
                if resposta() == '4':
                    print("1     " + "#"*plat[3])
                    print("2     " + "#"*plat[1])
                    print("3     " + "#"*plat[2])
                    print("4     " + "#"*plat[0])   
            flagPlat = 0;
            r = input()
            
        #50/50, apaga 2 alternativas
        elif r in ['50/50','50','5050']:
            if flag50 == 0:
                print("Parece que você já usou essa ajuda!")
            else:
                numApagados = 0
                for i in range(1,5):
                    if str(i) == resposta() or numApagados >= 2:
                        print(perg.iloc[indexPerg+i,:].values)
                    else:
                        print("############")
                        numApagados += 1
            flag50 = 0;
            r = input()

            
        print('Você tem certeza disso? Y/N \n')
        a = input()
        if a in ['Sim','Y','Yes','S', 'y', 'sim', 'yes']:
            
            #Acerto
            if r == resposta():
                print('Parabéns você acertou a resposta! :) \n')
                
                precoI += 1
                
            #Erro
            else:
                print('Infelizmente, escolheu a resposta errada :( \n')
                print('Seu premio final foi de ' + str(preco[precoI-1]) + ' reais \n')
                precoI = 1
                
                print("Está pronto para jogar denovo? Y/N \n")
                b = input()
                if b not in ['Sim','Y','Yes','S', 'y', 'sim', 'yes']:
                    enable = 0
                    
                #Reset dos flags
                else:
                    flagPlat = 1
                    flagUniver = 1
                    flag50 = 1
                    perguntasFeitas = []
            aux = 0    
                


# In[ ]:


perguntaEscolhida


# In[ ]:


indexPerg


# In[ ]:


resposta()


# In[ ]:





# In[ ]:


votosPlateia()


# In[ ]:





# In[ ]:





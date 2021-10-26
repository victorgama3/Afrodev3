# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_excel(r"C:\Users\victor.gama\Documents\Afrodev\Atletas.xlsx")
df1 = pd.read_excel(r"C:\Users\victor.gama\Documents\Afrodev\Times.xlsx")
df2 = pd.read_excel(r"C:\Users\victor.gama\Documents\Afrodev\Medalhas.xlsx")
df3 = pd.read_excel(r"C:\Users\victor.gama\Documents\Afrodev\Tecnicos.xlsx")
df4 = pd.read_excel(r"C:\Users\victor.gama\Documents\Afrodev\EntriesGender.xlsx")
arq_ini = open(r'C:\Users\victor.gama\Documents\Afrodev\inicial.txt')
inicio = arq_ini.read()
print(inicio)


while True:
    opcao = input("Digite o numero da sua pergunta? Dê 1 a 18!!\n").lower().strip()
    def totalAtleta():
            print(f"Quantos Atletas foram a TOKYO disputar as Olimpiadas?")
            qtd_atl = len(df)
            return qtd_atl
    def totalHomem():
            print(f"Qual foi o Total de participantes homens?")
            atl_men = df4["Male"].sum()
            return atl_men
            
    def totalMulher():
            print(f"Qual foi o Total de participantes mulheres?")
            atl_women = df4["Female"].sum()
            return atl_women

    def totalEsporte():
            print(f"Qual foi o Total de participantes por esporte?\n")
            part = df4['Male'] + df4['Female']
            total = df4["Total"] = part
            return df4

    def totalMedalha():
            print(f'Total de medalhas por países\n')
            medal = df2['Gold'] + df2['Silver'] + df2['Bronze']
            soma_medalhas = df2["Total de Medalhas"] = medal
            return df2

    def rank():
            print(f"Rank por medalhas \n\n")
            rank = df2.head(10).reset_index(drop=True)
            return (rank)

    def ouro(): 
            print(f"Paises com mais medalhas de OURO \n")
            gold = (df2.sort_values(by=['Gold'], ascending=False).head(10))
            return gold

    def prata():
            print(f"Paises com mais medalhas de PRATA \n")
            silver = (df2.sort_values(by=['Silver'], ascending=False).head(10))
            return silver

    def bronze():    
            print(f"Paises com mais medalhas de BRONZE \n")
            bronze = (df2.sort_values(by=['Bronze'], ascending=False).head(10))
            return bronze

    def menorOuro():
            print(f"Paises com MENOS medalhas de OURO \n")
            mGold = (df2.sort_values(by=['Gold'], ascending=True).head(10))
            return mGold

    def menorPrata():
            print(f"Paises com MENOS medalhas de PRATA \n")
            mSilver = (df2.sort_values(by=['Silver'], ascending=True).head(10))
            return mSilver

    def menorBronze():
            print(f"Paises com MENOS medalhas de BRONZE \n")
            mBronze = (df2.sort_values(by=['Bronze'], ascending=True).head(10))
            return mBronze

    def listaEsporte():
            print(f"Lista de Esportes que fizeram parte da olimpiadas \n")
            lsEsporte = (df4["Discipline"])
            return lsEsporte


    def listaHomem():
            print(f"Lista de Esportes que tem MAIS HOMENS \n")
            lh = df4.loc[[0,1,2,3,4,5,6,7,8,9,10],["Discipline", "Male"]].sort_values(by=['Male'], ascending=False).reset_index(drop=True)
            return(lh)

    def listaMulher():
            print(f"Lista de Esportes que tem MAIS MULHERES \n")
            lm = df4.loc[[0,1,2,3,4,5,6,7,8,9,10],["Discipline", "Female"]].sort_values(by=['Female'], ascending=False).reset_index(drop=True)
            return lm

    def qtdTreinador():
            print(f'Quantidade de Treinadores por PAÍS \n')
            treinadores = df3.value_counts(subset="NOC")
            return treinadores

    def qtdPais():
            print(f"Pais com a maior Quantidade de Treinadores\n")
            qtd_tre = df3.value_counts(subset="NOC").idxmax()
            return(qtd_tre)

    def qtdEsporte():
            print(f'Quantidade de Treinadores por ESPORTES \n')
            trein_esportes = df3.value_counts(subset="Discipline")
            return(trein_esportes)


    if opcao == "1":
            print(totalAtleta())
    elif opcao == "2":
            print(totalHomem())
    elif opcao == "3":
            print(totalMulher())
    elif opcao == "4":
            print(totalEsporte())
    elif opcao == "5":
            print(totalMedalha())
    elif opcao == "6":
            print(rank())
    elif opcao == "7":
            print(ouro())
    elif opcao == "8":
            print(prata())
    elif opcao == "9":
            print(bronze())
    elif opcao == "10":
            print(menorOuro())
    elif opcao == "11":
            print(menorPrata())
    elif opcao == "12":
            print(menorBronze())
    elif opcao == "13":
            print(listaEsporte())
    elif opcao == "14":
            print(listaHomem())
    elif opcao == "15":
            print(listaMulher())
    elif opcao == "16":
            print(qtdTreinador())
    elif opcao == "17":
            print(qtdPais())
    elif opcao == "18":
            print(qtdEsporte())


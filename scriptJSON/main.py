import os 
import json
#variables pour le rempissage des fichiers CSV
i = 0
list_lieu = []
list_dep = []
list_com = []
list_arr = []
list_vq = []
fichier = open("benin_zones_bj_lean.json","r+")
list_lieu = json.load(fichier)
print(list_lieu)
#Géneration des listes pour les dep, com, arr et vq
while i < len(list_lieu):
    list_dep.append([list_lieu[i]["CDP"],list_lieu[i]["DP"]])
    list_com.append([list_lieu[i]["CCM"],list_lieu[i]["CM"]])
    list_arr.append([list_lieu[i]["CAR"],list_lieu[i]["AR"]])
    list_vq.append([list_lieu[i]["CVQ"],list_lieu[i]["VQ"]])
    print(i)
    i += 1
#ON GERE LES DEPARTEMENTS
#Suppression des doublons de la liste
i = 0
while i < len(list_dep):
    cpt = 0
    cpt = list_dep.count(list_dep[i])
    print(cpt)
    while list_dep.count(list_dep[i]) > 1:
        del list_dep[i]
        
    i += 1

#conversion de la liste en dictionnaire et transformation de la liste en dictionnaire
i = 0
dic_dep = {list_dep[i][0]:list_dep[i][1] for i in range(0,len(list_dep))}
#dic_dep = json.dumps(dic_dep)
print(dic_dep)

#Creation du fichier des departements
os.system("type nul > dep.json")

#Remplissage du fichier correspondant aux dep
j = 0
os.chdir("D:\\Projets\\scriptJSON")
f_dep = open("dep.json","w")
print(f_dep)
json.dump(dic_dep,f_dep)


#ON GERE LES COMMUNES
#Suppression des doublons de la liste
j = 0
while j < len(list_com):
    cpt = 0
    cpt = list_com.count(list_com[j])
    print(cpt)
    while list_com.count(list_com[j]) > 1:
        del list_com[j]
        
    j += 1

#conversion de la liste en dictionnaire et transformation de la liste en dictionnaire
i = 0
dic_com = {list_com[j][0]:list_com[j][1] for j in range(0,len(list_com))}
#dic_dep = json.dumps(dic_dep)
print(dic_com)

#Creation du fichier des communes
os.system("type nul > com.json")

#Remplissage du fichier correspondant aux communess
j = 0
os.chdir("D:\\Projets\\scriptJSON")
f_com= open("com.json","w")
print(f_com)
json.dump(dic_com,f_com,indent=2)

#ON GERE LES ARRONDISSEMENTS
#Remplissage de la liste des arrondissements
#Suppression des doublons de la liste
l = 0
while l < len(list_arr):
    cpt = 0
    cpt = list_arr.count(list_arr[l])
    print(cpt)
    while list_arr.count(list_arr[l]) > 1:
        del list_arr[l]
        
    l += 1

#conversion de la liste en dictionnaire et transformation de la liste en dictionnaire
l = 0
dic_arr = {list_arr[l][0]:list_arr[l][1] for l in range(0,len(list_arr))}
#dic_dep = json.dumps(dic_dep)
print(dic_arr)

#Creation du fichier des arrondissements
os.system("type nul > arr.json")

#Remplissage du fichier correspondant aux arr
os.chdir("D:\\Projets\\scriptJSON")
f_arr = open("arr.json","w")
print(f_arr)
json.dump(dic_arr,f_arr,indent=2)


#ON GERE LES VILLAGES/QUARTIERS
#Remplissage de la liste des villages ou quartiers
#Suppression des doublons de la liste
m = 0
while m < len(list_vq):
    cpt = 0
    cpt = list_vq.count(list_vq[m])
    print(cpt)
    while list_vq.count(list_vq[m]) > 1:
        del list_vq[m]
        
    m += 1

#conversion de la liste en dictionnaire et transformation de la liste en dictionnaire
m = 0
dic_vq = {list_vq[m][0]:list_vq[m][1] for m in range(0,len(list_vq))}
#dic_dep = json.dumps(dic_dep)
print(dic_vq)

#Creation du fichier des departements
os.system("type nul > vq.json")

#Remplissage du fichier correspondant aux dep
os.chdir("D:\\Projets\\scriptJSON")
f_vq = open("vq.json","w")
print(f_vq)
json.dump(dic_vq,f_vq,indent=2)

#os.system("rename *.txt *.json")
os.system("pause")
def Annee(d,r,m):
    u1=d
    un=u1+r
    n=1
    while(un<m):
        u1=un
        un=u1+r
        n=n+1
        
    return n

def Renouv (fichier):
    depart=open(fichier,"r")
    resultat=open("Resultat.txt","a+")
    for ligne in depart:
        mot=ligne.split()
        x=Annee(int(mot[1]),int(mot[2]),int(mot[3]))
        resultat.write("Immat: {} | Nombre d'années:{}\n".format(str(mot[0]),x))
    depart.close()
    resultat.close()
def main():
    #d=int(input("Donnez d:"))
    #r=int(input("Donnez r:"))
    #m=int(input("Donnez m:"))
    #n=Annee(d,r,m)
    #print("le nombre d'années est:{}".format(n))
    file="Depart.dat"
    Renouv(file)
if __name__=="__main__":
    main()
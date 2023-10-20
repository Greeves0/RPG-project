from random import randint,choice
class caracter_stats:
    def __init__(self,name,HP,exp,level):
        self.name=nom
        self.HP=HP
        self.HPmax=HP
        self.exp=exp
        self.level=niveau
        self.expscale=1.4
    def ajouterVie(self,vie):
        #ajoute de la vie dans self.vie sans dépasser self.maxVie
        while self.HP<self.HPmax:
            self.HP+=HP
        return self.HP
    def retirerVie(self,vie):
        while self.HP>0:
            self.HP-=HP
        return self.HP
    def monterExperience(self):
        self.exp+=2
        if self.exp>=expcap:
            self.level+=1
            self.expcap=self.expcap*self.expscale
        #Augmente d’un niveau tous les 10 xp
        #Exemple 30xp = niveau 3
    def estVivant(self):
        if self.HP>0:
            return True
    def estMort(self):
        #retourne vrai si le personnage est mort

nom=str(input("insert your caracter name here"))



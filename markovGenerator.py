# -*- coding:utf-8 -*-
from random import randrange

class MarkovGenerator:
    def __init__(self, baseString = ""):
        self.dictionnary = {}
        self.firstWords = []


        if(baseString is not ""):
            self.add_sentence(baseString)


    """Add a string to the dictionnary"""
    def add_sentence(self, baseString):
        splitted = baseString.split()

        # Add the reference of the first word
        if splitted[0] not in self.firstWords:
            self.firstWords.append(splitted[0])

        # Add words to the dictionnary
        splitSize = len(splitted)
        currentWord = ""
        nextWord = ""

        for i in range(0, splitSize):
            currentWord = splitted[i]

            if i+1 >= splitSize:
                nextWord = ""
            else:
                nextWord = splitted[i+1]

            self.add_word(currentWord, nextWord if nextWord != "" and nextWord[-1] != "." else "")

        # Last word of the string is followed by an EOL
        self.add_word(currentWord, "")


    """ Add "nextword" in the array of the given key. If the key doesn't already exist, it will be created. """
    def add_word(self, key, nextWord):
        try:
            self.dictionnary[key].append(nextWord)
        except:
            self.dictionnary[key] = [nextWord]

    """ Generate a sentence using a random first word from the dictionnary """
    def generate_sentence(self, maxChar = 0):
        result = ""

        # Get the first word randomly
        #randomKey = self.get_indexed_key(randrange(len(self.dictionnary)))
        randomKey = self.firstWords[randrange(len(self.firstWords))]
        currentWord = randomKey
        nextWord = ""
        result += currentWord + " "

        while True:
            nextWord = self.dictionnary[currentWord][randrange(len(self.dictionnary[currentWord]))]

            if nextWord == "" or (maxChar != 0 and len(result.strip()) + len(nextWord) > maxChar):
                return result.strip()

            result += nextWord + " "
            currentWord = nextWord

    def get_indexed_key(self, index):
        i = 0

        for key in self.dictionnary.keys():
            if i == index:
                #print(key)
                return key

            #print(i, "(", type(i), ") != ", index, "(", type(index), ")")
            i += 1

        print("NO KEY RETURNED")


if __name__ == '__main__':
    #dummyString = "This is a dummy string. It contains some dummy values for testing purposes. It will be short, annoying, but still usefull."
    dummyString = """Une heureuse prédestination m'a fait naître à Braunau-am-Inn, bourgade située précisément à la frontière
de ces deux Etats allemands dont la nouvelle fusion nous apparaît comme la tâche essentielle de notre
vie, à poursuivre par tous les moyens.
L'Autriche allemande doit revenir à la grande patrie allemande et ceci, non pas en vertu de quelconques
raisons économiques. Non, non : même si cette fusion, économiquement parlant, est indifférente ou
même nuisible, elle doit avoir lieu quand même. Le même sang appartient à un même empire. Le peuple
allemand n'aura aucun droit à une activité politique coloniale tant qu'il n'aura pu réunir ses propres fils en
un même Etat. Lorsque le territoire du Reich contiendra tous les Allemands, s'il s'avère inapte à les
nourrir, de la nécessité de ce peuple naîtra son droit moral d'acquérir des terres étrangères. La charrue
fera alors place à l'épée, et les larmes de la guerre prépareront les moissons du monde futur.
C'est ainsi que la situation de ma ville natale m'apparaît comme le symbole d'un grand devoir. Elle a
d'autres titres à fixer le souvenir. Ce nid perdu fut, il y a plus d'un siècle, le théâtre d'une poignante
tragédie qui demeurera immortelle dans les annales de la nation allemande. C'est là en effet que, lors du
plus complet effondrement qu'ait connu notre patrie, un libraire de Nüremberg, Johannes Palm,
nationaliste endurci et ennemi des Français, mourut pour cette Allemagne qu'il aimait si ardemment
jusque dans son malheur. Il avait obstinément refusé de livrer ses complices, d'ailleurs les principaux
responsables. Comme Leo Schlageter l'avait fait. Comme lui aussi, il fut dénoncé à la France par un
représentant du Gouvernement. Un directeur de police d'Augsbourg s'acquit cette triste gloire, et donna
ainsi l'exemple aux autorités néo-allemandes du Reich de Severing.
C'est cette petite ville de l'Inn, auréolée de ce martyre allemand, bavaroise de sang mais politiquement
autrichienne que mes parents habitaient vers 1890. Mon père était un consciencieux fonctionnaire ; ma
mère vaquait aux soins de son intérieur et entourait ses enfants de soins et d'amour. Cette époque a peu
marqué dans mon souvenir, car, quelques années plus tard, mon père alla occuper un nouveau poste un
peu plus bas sur le cours de l'Inn, à Passau, donc en Allemagne même.
Mais le sort d'un employé des douanes autrichien comportait alors bien des déplacements. Peu de temps
après mon père revenait à Linz, et y prenait sa retraite. Pour le cher vieil homme, cela ne devait pas être
le repos. Fils d'un pauvre petit journalier agricole, il lui avait déjà fallu naguère quitter la maison. A peine
âgé de treize ans, il boucla sa sacoche et quitta le canton de forêt qui était son pays natal. Malgré le
conseil de villageois expérimentés, il était parti à Vienne pour y apprendre un métier. Ceci se passait vers
1850. C'était une décision bien amère que celle de partir, de se mettre ainsi en route vers l'inconnu avec
trois écus en poche. Quatre ans après, passé compagnon, il n'était cependant pas satisfait. Au contraire.
La misère persistante de cette époque fortifia sa résolution de quitter son métier pour devenir quelque
chose de « plus haut ». Alors que jadis, pauvre jeune homme, la situation du prêtre de son village lui
paraissait le summum de la condition humaine, maintenant que la grande ville avait élargi ses idées, il
mettait au-dessus de tout la dignité de fonctionnaire. Avec toute l'âpreté de ceux que la misère et
l'affliction ont mûris avant l'âge, ce jeune homme de dix-sept ans poursuivit obstinément la réalisation de
ses nouveaux projets - et il devint fonctionnaire. Il atteignit son but vers vingt-trois ans, je crois, réalisant
ainsi sa promesse de jeune homme de ne retourner dans son cher village qu'après être devenu
quelqu'un.
Maintenant, le but était atteint ; mais personne au village ne se souvenait plus du petit garçon de jadis et
le village lui était devenu à lui-même étranger."""
    testing = MarkovGenerator(dummyString)
    for i in range(0, 50):
        value = testing.generate_sentence(150)
        print(i, ":", value)
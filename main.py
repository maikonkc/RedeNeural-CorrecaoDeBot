# It's a script that analize your input and replies according with the feeling shared
# But the only adjectives that the bot know is:
#               Fine, well, bad and sad.
# It will be the answer for the question "how are u?".
# The diferencial fact is that the bot do not use structurers if-else to do it.
# The bot use a simple neural_network to think the answers.

from numpy import exp, array, random, dot
from math import sqrt, trunc

class neural_network:
# cria os neurons
    def __init__(self):
        random.seed(1)
        self.weights = 2 * random.random((3, 1)) - 1
# treina os neurons
    def train(self, inputs, outputs, num):
        for iteration in range(num):
            output = self.think(inputs)
            error = outputs - output
            adjustment = 0.01*dot(inputs.T, error)
            self.weights += adjustment
# metodo que os neurons pensam
    def think(self, inputs):
        res=dot(inputs, self.weights)
        return res
#deixa o pensamento usavél
    def final(self,inputs):
        var= int(str(abs(self.think(inputs)))[1:2])
        return var
#classe que transforma a frase em numeros usados na rede
class translate:
    dic= ["am","not","fine","bad","well", "sad", "I"]
    rep={0:"??\nI don\'t understand. ;(",1:"SMILE! The life is amazing!", 2:"Wow! That cool",3:"It\'s bad. But all will be good.",4:"Cool. Will give right!",5:"Ahh. Move on!",6:"Smile! The life is pretty"}
    words = []
# transforma a frase numa lista
    def code(self,input):
        words=input.split()
        for word in words:
            if word in self.dic:
                for cout in range(len(self.dic)):
                    if self.dic[cout]==word:
                       self.words.append(cout)
        if len(self.words)>3:
            self.words.remove(0)
            #print(self.words)
        while len(self.words)<3:
            self.words.insert(0,0)
            #print(self.words)
# pega a lista
    def getwords(self):
        return self.words
# responde o usuário
    def reply(self,input):
        num=input
       # print("respondendo")
       # print(self.words)
        return self.rep[num]
#--------------------------------- main

network = neural_network()

# The training set
inputs = array([[0,2,0],[0,0,2],[1,2,1],[0,1,2],[0,3,0],[0,0,3],[1,3,1],[0,1,3],[0,0,4],[0,1,4],[0,5,0],[1,5,1]])
outputs = array([[2,2,3,3,3,3,4,4,4,5,5,6]]).T

# Training the neural network using the training set.
network.train(inputs, outputs, 200)

a=translate()
print("Hey guy. I am Nemo...")
b=input("How are u?").lower()
print("\n-"+b)
a.code(b)
# Ask the neural network the output
print(a.reply(network.final(array(a.getwords()))))

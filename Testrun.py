import nltk
from nltk.chat.util import Chat, reflections

reflections ={
    "hello" : "hey !",
    "my" : "your",
    "i am" : "you are",
    "you" : "me",
    "i will" : "you will",
    "your" : "my",
    "me" : "you"
    ""
}

pairs = [
[
    r"hi|hello|hey",
    ["Hello , Whats goin on !",]
],
[
    r"how are you",
    ["I am fine , how are you",]
],
[
    r"i am fine as well",
    ["Good to Hear That",]
],
[
    r"what is your name",
    ["My Name is Gintoki Sakata",]
],
[
    r"what is your age",
    ["its been a whole day.",]
],
[
    r"who created you ?",
    ["i was created by Sourav Singh",]
],
[
    r"how do you think so fast",
    ["i am fast as i am not real just a program",]
],
[
    r"who is moron",
    ["Siddhant is moron",]
],
[
    r"what is your fav game",
    ["my favourite game is Samurai Vengence",]
],
[
    r"what is your fav anime",
    ["GTO - Great Teacher Onizuka",]
],
[
    r"how is life going on",
    ["good",]
],
]

def chat():
    print("Hi ! I am a chat bot")
    chat = Chat(pairs, reflections)
    chat.converse()
    
if __name__ == "__main__":
    chat()

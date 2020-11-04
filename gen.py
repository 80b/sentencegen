import random
print("""

• Random Sentence Gen   
        Loading....             
          By Raz                  
          
[1] Quit the app
[2] Gen sentences
""")
yes = int(input('Which option?: '))
amount = int(input("How many sentences do you want to gen?: "))
nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
for i in range(amount+1):
	print("%s %s %s %s"%(random.choice(nouns), random.choice(verbs), random.choice(adv), random.choice(adj)))	

print('Exiting..')

import random
print("""

• Random Sentence Gen   
        Loading....             
          By Raz                  
          
[1] Quit the app
[2] Gen sentences
""")
yes = int(input('Which option?: '))
nouns = ("puppy", "car", "rabbit", "girl", "monkey")
verbs = ("runs", "hits", "jumps", "drives", "barfs") 
adv = ("crazily.", "dutifully.", "foolishly.", "merrily.", "occasionally.")
adj = ("adorable", "clueless", "dirty", "odd", "stupid")
while yes != 1:
	if yes == 2:
		print("%s %s %s %s"%(random.choice(nouns), random.choice(verbs), random.choice(adv), random.choice(adj)))	

print('Exiting..')

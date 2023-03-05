# REMAKE THIS IN JS
# This is just establishing the script idea
# ADD: TKINTER

# enter 4 names
# pull initials, store in a list of tuples

# find every arrangement of those letters
# using loops? inefficient, but works for now

# let user select which dictionary to use
# search the dictionary file using these rules
# letters must occur in the order they're shown
# W <-> U, K -> C
# maybe work backwards? 
# >> find any word with all of those letters, then arrange the letter. 

# letters = input("4 letters pls ty: ")

from itertools import permutations

dict = []
for line in open('./words_alpha.txt', 'r').readlines():
    dict.append(line.strip())

validWords = []
for word in dict:
    if (word[0] == 'j') & ('n' in word) & ('p' in word) & ('r' in word):
            validWords.append(word)

perms = [''.join(p) for p in permutations("jnpr")]
perms = set(perms)
print(validWords)

# find words that begin with each of the 4 letters and divide based on that
# in interface > bold any of the letters as they appear, user can figure that out
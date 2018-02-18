import itertools
import json

def anagram(word):

    list = ["".join(perm) for perm in itertools.permutations(word)]
    return list

def search(list):
        words=json.load(open("/tmp/freq_dict.json"))
        result = ""
        rank = 10000

        for word in list:
            if word in words:
                value = words[word]
                if value == 0: value = 9999
                if 0 < value < rank:
                    result = word
                    rank = value
        return result

puzzle1=['nagld','ramoj','camble','wraley']
puzzle2=['bnedl','idova','seheyc','aracem']
puzzle3=['shast','doore','ditnic','catili']
puzzle4=['knidy','legia','cronee','tuvedo']
puzzle5=['gyrint','drivet','snamea','ceedit','sowdah','elchek']

def display(puzzle):
        print("The solutions for the puzzle are :")
        for word in puzzle:
            list = anagram(word)
            output = search(list)
            print(output)

def main():
        puzzle1=['nagld','ramoj','camble','wraley']
        puzzle2=['bnedl','idova','seheyc','aracem']
        puzzle3=['shast','doore','ditnic','catili']
        puzzle4=['knidy','legia','cronee','tuvedo']
        puzzle5=['gyrint','drivet','snamea','ceedit','sowdah','elchek']
        display(puzzle1)
        display(puzzle2)
        display(puzzle3)
        display(puzzle4)
        display(puzzle5)

if __name__== "__main__":
        main()

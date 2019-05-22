#import the json library to use the data.json file
import json

#import the get_close_matches method that is in the difflib library.
#This uses SequenceMatcher to compare two words and then looks in another
#list or dictionary to find similar words. We set the tolerance level and the
#maximum number of items it can return
from difflib import get_close_matches

#In the variable called data, open the json file by doing this:
data = json.load(open("data.json"))

#Create a function that will return the definition of the word when calling the function
def translate(word):
    word = word.lower()

    #If the entered word is in data, return the definition
    if word in data:
        return data[word]

    #In line 15, we made the whole word lowercase. This causes a problem when the user
    #enters a word such as "Texas", which has a capital T in our data file.
    #The title() method makes the first letter of the word capital and the rest of
    #the letters as lowercase.
    elif word.title() in data:
        return data[word.title()]

    #There was a problem where the program could not return acronyms such as USA
    #or NATO. This was fixed by saying if the user enters a word thats uppercase,
    #find the word in data.
    elif word.upper() in data:
        return data[word.upper()]

    #Checking if the length of the list of similar words is greater than 0
    elif len(get_close_matches(word, data.keys())) > 0:
        #Returning if they mean the first word in the list that gets returned in
        #the get_close_matches method. This also asks the user to enter yes if
        #they actually meant to put the corrected word or no if they did not.
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        #If the user enters yes, print the definition of the word
        if yn == "Y":
            #get_close_matches(word, data.keys())[0]
            #This line will do the same thing as line 18 but return the first
            #word in the new list
            return data[get_close_matches(word, data.keys())[0]]

        #If the user enters no, tell them that it does not exist
        elif yn == "N":
            return "The word doesn't exist. Please double check it."

        #If the user enters something other than Y or N, tell them it is unrecognizable.
        else:
            return "We did not understand your entry."
    else:
        return "The word doesn't exist. Please double check it."



#Tell the user to input a word
word = input("Enter word: ")

output = translate(word)

#Sometimes the output can be a list or it can be a string.
#To prevent the output from messing up, I said that if the output is a list,
#print each item in the list. This way, if a word has multiple definitions, they
#will be printed line by line.
if type(output) == list:
    for item in output:
        print(item)

#if it is not a list, then it will be a string. Print the output if it is a string:
else:
    print(output)

"""Generate Markov text from text files."""
import sys
from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    text = file.read()
   
    return text #'Contents of your file as one long string'


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    #Output = chains (dict) = {(word1), (word2) => tuple : ['list' => list of random words]
#              -->> repeat  -->>
#               }
 
    words = text_string.split()
    chains = {}
    

    for i in range(len(words) -2):
        value_list = []
        chains[(words[i], words[i + 1])]  =  value_list
      
        if (words[i+2]) not in chains:
            value_list.append(words[i+2])
    return (chains)
       
    # if (words[word+2]) is not chains:
    #     chains [(words[word+2])]=[]
    #     chains [(words[word+2])].append(value_list)
    #     key= (word[i+1])
    #     value= word[1+2]

    # word= text_string

    # # # for i in range(0, len(word)):
    # word= text_string
    # words.append(none)
    # for i in range(len(word) -2):
    #     key= (word[i+1])
    #     value= word[1+2]

    #     if key not in chains:
    #         chains[key]= []
    #         chains[key].append(value) 

def make_text(chains):
    """Return text from chains."""
    
    
    # your code goes here
    #List will link random key + value and join at the end
    words = []

    #Convert keys into list and select random keys from list
#     new_list_keys = list(chains.keys())
#     random_keys = choice(new_list_keys)
   
#    #Convert values into list and select random value from list
#     new_values = list(chains.values())
#     random_values = choice(new_values) 

    for k, v in chains.items():
            key_list = list(k)
            value_list = list(v)

    random_key = choice(key_list)
    words.append(random_key)
            
    random_value = choice(value_list) 
    words.append(random_value)
    #print(words)        


    # while words is not None:
    #     random_keys= (random_keys[1], words)
    #    # print (random_keys)

    #words.append(random_keys)
    #words.append(random_values) 
    #print('list: {words}')

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)

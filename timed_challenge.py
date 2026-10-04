#Question 5: Unique Word Count
#I want to count how many distinct words are in this collection.
#Input: "one fish two fish red fish blue fish"
#Output = 5


def unique_word_count(text):
    #A set is better because it automatically stores each word just once.
    #Adding words to this set is O(1) on average, which means the overall runtime is O(n).
    if not isinstance(text, str):
        return None

    words = text.split()
    unique_words = set(words)

    return len(unique_words)


#Test cases
print(unique_word_count("one fish two fish red fish blue fish"))
#Expected: 5

print(unique_word_count("apple apple banana banana"))
#Expected: 2

print(unique_word_count("hello"))
#Expected: 1

print(unique_word_count(""))
#Expected: 0

print(unique_word_count("apple banana apple orange banana"))
#Expected: 3

print(unique_word_count(12345))
#Expected: None

#Reflection

#I chose to use a set for this problem because I needed to count
#the number of unique words. A set is the better choice because 
#it automatically removes any duplicate values. 
#I used the split() method to break up the sentence into
#the individual words, and then I added those words to a set.
#After, I used len() to find the number of unique words in the set.
#I used these operations to add values to a set and to check
#the size of the set, which are both O(1) on average.
#Since every word needs to be procedssed, the overall runtime is O(n).
#The 30 minute timer affected my decision because I wanted to find
#a solution that was simple and efficient. 
#Since I was already familiar with sets, and it fit the problem well
#because it is designed to store unique values, it allowed me to 
#work on getting a quick solution and testing it instead of 
#trying to create a complicated and thorough algorithm
#One trade-off I made was that I used python's built-in 
#set data structure instead of implementing my own.
#This made my solution simpler and easier to understand,
#but it doesn't correctly show how a set works internally.
#During the time limit I thought that having a correct and 
#efficient solution was more important than implementing
#my own data structure.
#I also tested normal inputs, duplicate words, single words,
#empty strings, and a wrong input type to make sure the function
#was able to handle a variety of cases and return the expected output.
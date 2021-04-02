''' Q1.	Write a function that eliminates all the punctuation symbols, html tags, etc. in the given text.
    It should return plain text containing alpha numeric characters.
    Text="NumPy,<1> pandas ?,matplotlib; |,seaborn# SciPy* etc.. are few &Python packages) that are) frequently (/used |@for text% preprocessing$.” '''
                

# define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~|1'''

text= ''' "NumPy,<1> pandas ?,matplotlib; |,seaborn# SciPy* etc.. are few &Python packages) that are) frequently (/used |@for text% preprocessing$.” '''

# To take input from the user
# my_str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in text:
   if char not in punctuations:
       no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)



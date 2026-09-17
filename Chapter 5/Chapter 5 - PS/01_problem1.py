# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

words = {
    "Hamah": "All",
    "Salam": "Hello",
    "Chetor": "How",
    "Chera": "Why",
    "Hamisha": "Always"
}
word = input("Enter your Persian words you want to translate to English: ")
persian_to_english = words[word]
print(f"Mean of {word} is: ", persian_to_english)
print(words.values())




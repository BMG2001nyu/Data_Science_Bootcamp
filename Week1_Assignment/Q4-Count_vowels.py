def count_vowels(word):
    vowels = "aeiouAEIOU"
    return sum(1 for char in word if char in vowels)

print(count_vowels("This_is_DataScience_Bootcamp")) 
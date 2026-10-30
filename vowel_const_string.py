#write a function that takes a string and returns the count of vowels and consonants separatly

def funCountVowelConst(userInput):
    #define vovwels
    vovwels = "aeiouAEIOU"
    countVowel = 0
    contConst = 0

    #Lajwanti123
    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vovwels):
                countVowel = countVowel+1
            else :
                contConst = contConst+1
    return countVowel, contConst

#Function call
vowels,consonents =  funCountVowelConst("Lajwanti Lohana")  
print(vowels,consonents)              
'''
Pig Latin is the same words in the same order except that you take the first
letter of each word and put it on the end, then you add 'ay' to the end of that.

Task:
Take a sentence or word in English and convert to Pig Latin!

Input Format:
Only small letters

Output Format:
A string of the same sentence in Pig Latin

Sample Input:
'i know how to use git'

Sample Output:
'iay nowkay owhay otay seuay itgay'

'''

# accept user input or use the provided sample
entry = input('Enter a word or sentence: ') or 'enter a word or sentence'

def english_to_pig_latin(eng):
    output = []
    for i in eng.split():
        output.append(i[1:] + i[0] + 'ay')
    return 'The Pig Latin equivalent is: ' + ' '.join(output)

print(english_to_pig_latin(entry))
'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  

    count = 0 
    if word == "":
        return count
    elif ((word[0:2]) == 'th'):
        word = word[2:]
        count += 1
    else:
        word = word[1:]
    return count + count_th(word)


print(count_th('therapist'))
print(count_th('plethora'))
print(count_th('thoth'))
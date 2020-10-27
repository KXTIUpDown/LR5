import math
alphabet ="abcdefghijklmnopqrstuvwxyz"

w = ["basic", "compilation", "programs"]
result = ''
if alphabet[alphabet.index(w[0][-1])+1] != "z":
    result += alphabet[alphabet.index(w[0][-1])+1]
else:
    result += "a"
if alphabet[alphabet.index(w[1][-1])+1] != "z":
    result += alphabet[alphabet.index(w[1][-1])+1]
else:
    result += "z"

if len(w[2])/2 != int(len(w[2])/2):
    if alphabet[alphabet.index(w[2][1])+1] == "z":
        result += "a"
    else:
        result += alphabet[alphabet.index(w[2][1])+1]
else:
    if alphabet[alphabet.index(w[2][int(len(w[2])/2-1)])-1] != "a":
            result += alphabet[alphabet.index(w[2][int(len(w[2])/2-1)])-1]
    else:
        result += "z"

index = len(w[0]) + len(w[1])
if index > 26:
    index %= 26
result += alphabet[index - 1]
print(result)

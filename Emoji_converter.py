ip = input(">")
words=ip.split()
mapping ={
    ":)":"😊",
    ":(":"😒"
}
output=""
for word in words:
    output+=mapping.get(word,word)+" "
print(output)
# A four-column/four-row table ‒ a two dimensional array (4x4)

table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]


for i in range(4):
    for j in range(4):
        print(table[i][j],end="\t\t")
    print()


print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

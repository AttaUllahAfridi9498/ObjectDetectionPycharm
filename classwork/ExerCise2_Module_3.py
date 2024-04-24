cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],

        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],

        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

for i in range(3):
    for j in range(3):
        for t in range(3):
            print(cube[i][j][t],end="\t\t")
    print()


print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
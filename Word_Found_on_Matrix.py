matrix = [
    ['A', 'B', 'C', 'D'],
    ['E', 'F', 'G', 'H'],
    ['I', 'J', 'K', 'L'],
    ['M', 'N', 'O', 'P']
]

word = input("Enter word to search: ").upper()

rows = 4
cols = 4

found = False

for i in range(rows):
    for j in range(cols):

        if matrix[i][j] == word[0]:
            print("Starting letter found at:", i, j)
            found = True

if found:
    print("Word letters are present")
else:
    print("Word not found")
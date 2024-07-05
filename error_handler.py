file = open('youtube.py', 'w')

try:
    file.write('Learning python')
finally:
    file.close()

with open('youtube.txt', 'w') as file:
    file.write('Learning python')

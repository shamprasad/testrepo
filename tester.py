import random
import string
count = 0
while count <= 1310720:
        randName = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase) for _ in range(16))
        print randName
        count += 1

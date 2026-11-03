dagen = 0
robots = 10



while robots < 30:
    dagen = dagen + 1
    robots = robots + 4
if dagen % 3 == 0:
    robots = robots - 2

print(dagen)
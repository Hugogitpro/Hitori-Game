a = int(input("valeur de a :"))
b = int(input("valeur de b :"))


def PGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a
PGCD(a,b)

def iskeyValid(key):
    return True if PGCD(a,26)==1 else False

print iskeyValid(11)

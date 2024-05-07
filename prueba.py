# Prueba de nuevo archivo.py

def nuevaRama():
    print("Esta es una nueva rama")

nuevaRama()

def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return n * (n-1)
factorial(5)

# probando el replit, modificacion desde Vs code en remoto con git.
def suma(a,b):
   return a + b

def test_suma():
    assert suma(5,5) == 10

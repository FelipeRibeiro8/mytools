PI_INT = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
E_INT =  "7182818284590452353602874713526624977572470936999595749669676277240766303535475945713821785251664274"

def pi_real(num):
    casapi = int(PI_INT)
    casas = 10**(100-num)
    numero = casapi/casas
    int_numero = int(numero)
    pi = "3" + "," + str(int_numero)
    print(pi)

def e_real(num):
    casae = int(E_INT)
    casas = 10**(100-num)
    numero = casae/casas
    int_numero = int(numero)
    e = "2" + "," + str(int_numero)
    print(e)


#Novoselec, 20 nalog, najtežje: 11, 12, 30

#1.naloga
def multiples_of_3_or_5(n):
    vsota = 0
    
    for stevilo in range(n):
        if stevilo % 3 == 0 or stevilo % 5 == 0:
            vsota += stevilo
    return vsota

print(multiples_of_3_or_5(1000))
    
#2.naloga
def even_fibonacci_numbers(meja):
    a = 1
    b = 2
    vsota_sodih = 2  

    while True:
        c = a + b
        if c > meja:
            break
        if c % 2 == 0:
            vsota_sodih += c
        a = b
        b = c
    return vsota_sodih

print(even_fibonacci_numbers(4000000))

#3.naloga
def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largest_prime_factor(600851475143))

#4.naloga
def ali_je_palindrom(stevilo):
    return str(stevilo) == str(stevilo)[::-1]

def largest_palindrome_products():
    najvecji = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            produkt = i * j
            if ali_je_palindrom(produkt) and produkt > najvecji:
                najvecji = produkt
    return najvecji

print(largest_palindrome_products())

#5.naloga

import math

def najmanjsi_veckratnik(a, b):
    return a * b // math.gcd(a, b)

def smallest_multiple(n):
    rezultat = 1
    for i in range(2, n + 1):
        rezultat = najmanjsi_veckratnik(rezultat, i)
    return rezultat

print(smallest_multiple(20))

#6.naloga
def sum_square_difference(stevilo):
    vsota1 = 0
    j = 0
    for i in range(stevilo + 1):
        vsota1 += i ** 2
        j += i
    vsota2 = j ** 2
    return vsota2 - vsota1

print(sum_square_difference(100))

#7.naloga    
def je_prastevilo(stevilo):
    if stevilo <= 1:
        return False
    if stevilo == 2:
        return True
    if stevilo % 2 == 0:
        return False
    for i in range(3, int(stevilo**0.5) + 1, 2):
        if stevilo % i == 0:
            return False
    return True

def poisci_stevilo(n):
    a = 0
    stevilo = 2
    while a < n:
        if je_prastevilo(stevilo):
            a += 1
        stevilo += 1
    return stevilo - 1

print(poisci_stevilo(10001))

#8.naloga
stevilo_str = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)

def largest_product_in_a_series(stevilo):
    najvecji_produkt = 0
    for i in range(len(stevilo_str) - stevilo + 1):
        produkt= 1
        for j in range(i, i + stevilo):
            produkt *= int(stevilo_str[j])
        najvecji_produkt = max(najvecji_produkt, produkt)
    return najvecji_produkt

print(largest_product_in_a_series(13))

#9.naloga 
def special_pythagoream_triple(vsota):
    for a in range(1, vsota):
        for b in range(a + 1, vsota - a):
            c = vsota - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
print(special_pythagoream_triple(1000))
    
#10.naloga
def je_prastevilo(stevilo):
    if stevilo <= 1:
        return False
    if stevilo == 2:
        return True
    if stevilo % 2 == 0:
        return False
    for i in range(3, int(stevilo**0.5) + 1, 2):
        if stevilo % i == 0:
            return False
    return True

def vsota(meja):
    vsota = 0
    for i in range(meja + 1):
        if je_prastevilo(i):
            vsota += i
    return vsota

print(vsota(2000000))

#11.naloga
grid_str = """
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
"""

grid = [[int(stevilo) for stevilo in line.strip().split()] for line in grid_str.strip().split('\n')]

def get_product(vrstica, stolpec, smer):
    product = 1
    if smer == "desno":
        for i in range(4):
            product *= grid[vrstica][stolpec + i]
    elif smer == "dol":
        for i in range(4):
            product *= grid[vrstica + i][stolpec]
    elif smer == "diagonalno1":
        for i in range(4):
            product *= grid[vrstica + i][stolpec + i]
    elif smer == "diagonalno2":
        for i in range(4):
            product *= grid[vrstica + i][stolpec - i]
    return product

def largest_product_in_a_grid():
    najvecji_produkt = 0

    for vrstica in range(len(grid)):
        for stolpec in range(len(grid[0])):
            if stolpec + 3 < len(grid[0]):
                najvecji_produkt = max(najvecji_produkt, get_product(vrstica, stolpec, "desno"))
            if vrstica + 3 < len(grid):
                najvecji_produkt = max(najvecji_produkt, get_product(vrstica, stolpec, "dol"))
            if vrstica + 3 < len(grid) and stolpec + 3 < len(grid[0]):
                najvecji_produkt = max(najvecji_produkt, get_product(vrstica, stolpec, "diagonalno1"))
            if vrstica + 3 < len(grid) and stolpec - 3 >= 0:
                najvecji_produkt = max(najvecji_produkt, get_product(vrstica, stolpec, "diagonalno2"))

    return najvecji_produkt

print(largest_product_in_a_grid())


#12.naloga
def triangle_number(n):
    return n * (n + 1) // 2

def prestej_prastevila(stevilo):
    slovar = {} #slovar prastevil in st. pojavitev
    i = 2
    while i * i <= stevilo:
        while stevilo % i == 0:
            stevilo //= i
            slovar[i] = slovar.get(i, 0) + 1
        i += 1
    if stevilo > 1:
        slovar[stevilo] = slovar.get(stevilo, 0) + 1
    return slovar

def st_deliteljev(stevilo):
    prime_factors = prestej_prastevila(stevilo)
    stevilo = 1
    for i in prime_factors.values():
        stevilo *= i + 1
    return stevilo

def highly_divisable_triangle_number(najmanjse_st_deliteljev):
    n = 1
    while True:
        triangle_num = triangle_number(n)
        stevilo_deliteljev = st_deliteljev(triangle_num)
        if stevilo_deliteljev > najmanjse_st_deliteljev:
            return triangle_num
        n += 1

print(highly_divisable_triangle_number(500))

#14.naloga
def collatz_dolzina(n):
    dolzina = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        dolzina += 1
    return dolzina

def longest_collatz_sequence(meja):
    najdaljsi = 0
    zacetek = 0

    for i in range(1, meja):
        dolzina = collatz_dolzina(i)
        if dolzina > najdaljsi:
            najdaljsi = dolzina
            zacetek = i

    return zacetek

print(longest_collatz_sequence(1000000))

#15.naloga
def fakulteta(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

def binomski_koef(n, k):
    return fakulteta(n) // (fakulteta(k) * fakulteta(n - k))

def lattice_paths(dimenzije):
    return binomski_koef(2 * dimenzije, dimenzije)

print(lattice_paths(20))



#16.naloga
stevilo = 2 ** 1000
stevilo_str = str(stevilo)
vsota =sum(int(stevilka) for stevilka in stevilo_str)
print(vsota)


#19.naloga
def je_prestopno_leto(leto):
    if leto % 4 == 0:
        if leto % 100 == 0:
            if leto % 400 == 0:
                return True
            return False
        return True
    return False

def prestej_nedelje():
    dan_v_tednu = 2  #torek
    st_nedelj = 0
    
    for leto in range(1901, 2001):
        for mesec in range(1, 13):
            if dan_v_tednu == 6: #6=nedelja
                st_nedelj += 1

            if mesec in [4, 6, 9, 11]:
                dnevi_v_mesecu = 30
            elif mesec == 2:
                dnevi_v_mesecu = 29 if je_prestopno_leto(leto) else 28
            else:
                dnevi_v_mesecu = 31

            dan_v_tednu = (dan_v_tednu + dnevi_v_mesecu) % 7

    return st_nedelj

print(prestej_nedelje())

#20.naloga
def fakulteta(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

def vsota_decimalk(stevilo):
    return sum(int(decimalka) for decimalka in str(stevilo))

print(vsota_decimalk(fakulteta(100)))


#25.naloga
def fibonacci(st_decimalk):
    a, b = 1, 1
    i = 2  
    while len(str(b)) < st_decimalk:
        a, b = b, a + b
        i += 1
    return i

print(fibonacci(1000))
            
#30.naloga
def vsota_petih_potenc(stevilo):
    return sum(int(decimalka)**5 for decimalka in str(stevilo))

def digit_fifth_power():
    meja = 354294
    #najvecje mozno stevilo, (9^5) * 6 = 354294
    stevila = []

    for i in range(2, meja + 1):
        if i == vsota_petih_potenc(i):
            stevila.append(i)

    return sum(stevila)

print(digit_fifth_power())

#34.naloga

def fakulteta(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fakulteta(n - 1)

def vsota_decimalk(n):
    return sum(fakulteta(int(digit)) for digit in str(n))

def digit_factorials(meja):
    vsota = 0
    for stevilo in range(10, meja):
        if stevilo == vsota_decimalk(stevilo):
            vsota += stevilo
    return vsota

print(digit_factorials(2540160)) #najvecja mozna meja za 7-mestno stevilo, 7 * 9! = 2540160


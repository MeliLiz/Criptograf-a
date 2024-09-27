# Permutación Inicial (IP)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

# Permutación Final (FP)
FP = [40, 8, 48, 16, 56, 24, 64, 32,
      39, 7, 47, 15, 55, 23, 63, 31,
      38, 6, 46, 14, 54, 22, 62, 30,
      37, 5, 45, 13, 53, 21, 61, 29,
      36, 4, 44, 12, 52, 20, 60, 28,
      35, 3, 43, 11, 51, 19, 59, 27,
      34, 2, 42, 10, 50, 18, 58, 26,
      33, 1, 41, 9, 49, 17, 57, 25]

# Expansión E
E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

# Permutación P
P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

# Tabla de permutación PC-1
PC1 = [57, 49, 41, 33, 25, 17, 9,
       1, 58, 50, 42, 34, 26, 18,
       10, 2, 59, 51, 43, 35, 27,
       19, 11, 3, 60, 52, 44, 36,
       63, 55, 47, 39, 31, 23, 15,
       7, 62, 54, 46, 38, 30, 22,
       14, 6, 61, 53, 45, 37, 29,
       21, 13, 5, 28, 20, 12, 4]

# Tabla de permutación PC-2
PC2 = [14, 17, 11, 24, 1, 5,
       3, 28, 15, 6, 21, 10,
       23, 19, 12, 4, 26, 8,
       16, 7, 27, 20, 13, 2,
       41, 52, 31, 37, 47, 55,
       30, 40, 51, 45, 33, 48,
       44, 49, 39, 56, 34, 53,
       46, 42, 50, 36, 29, 32]

# Número de rotaciones para cada ronda
ROTATIONS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Las 8 S-boxes
S_BOXES = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
     [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
     [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
     [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
     [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
     [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
     [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
     [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
     [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
     [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
     [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
     [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
     [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],
    
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
     [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
     [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


def permutate(block, table):
    """ Permutar un bloque de bits según la tabla dada. """
    return [block[i - 1] for i in table]

def xor(a, b):
    """ Operación XOR bit a bit. """
    return [i ^ j for i, j in zip(a, b)]

def sbox_substitution(block):
    """ Aplicar las S-boxes sobre un bloque de 48 bits. """
    output = []
    for i in range(8):
        chunk = block[i * 6:(i + 1) * 6]
        row = (chunk[0] << 1) | chunk[5]
        col = (chunk[1] << 3) | (chunk[2] << 2) | (chunk[3] << 1) | chunk[4]
        val = S_BOXES[i][row][col]
        output += [int(b) for b in f'{val:04b}']
    return output

def f_function(r_half, key):
    """ Función Feistel F. """
    expanded_half = permutate(r_half, E)  # Expande 32 bits a 48
    xor_result = xor(expanded_half, key)  # XOR con la subclave
    substituted = sbox_substitution(xor_result)  # Sustitución con S-boxes
    return permutate(substituted, P)  # Permutación P final

def feistel_round(l_half, r_half, key):
    """ Una ronda de Feistel. """
    new_r = xor(l_half, f_function(r_half, key))  # XOR entre L y F
    return r_half, new_r  # Intercambio de L y R

def generate_subkeys(key):
    """ Generar las 16 subclaves a partir de la clave inicial. """
    key = permutate(key, PC1)  # Aplicar la permutación PC1
    c, d = key[:28], key[28:]  # Dividir en dos mitades de 28 bits

    subkeys = []
    for i in range(16):
        # Rotaciones circulares
        c = c[ROTATIONS[i]:] + c[:ROTATIONS[i]]
        d = d[ROTATIONS[i]:] + d[:ROTATIONS[i]]
        # Permutación PC2 para obtener la subclave
        subkeys.append(permutate(c + d, PC2))
    return subkeys

def pad(text):
    """ Padding para que el texto sea múltiplo de 64 bits. """
    pad_len = 8 - (len(text) % 8)
    return text + chr(pad_len) * pad_len

def unpad(text):
    """ Eliminar el padding después del descifrado. """
    pad_len = ord(text[-1])
    return text[:-pad_len]

def text_to_bits(text):
    """ Convertir texto a bits. """
    bits = []
    for char in text:
        bits += [int(bit) for bit in f'{ord(char):08b}']
    return bits

def bits_to_text(bits):
    """ Convertir bits a texto. """
    chars = []
    for b in range(0, len(bits), 8):
        byte = bits[b:b + 8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def des_encrypt(text, key):
    """ Cifrar un bloque de texto usando DES. """
    # Convertir el texto y la clave en bits
    text = text_to_bits(pad(text))
    key = text_to_bits(key)
    #print("Texto en bits:", (text))

    # Generar subclaves
    subkeys = generate_subkeys(key)

    # Cifrado en bloques de 64 bits
    encrypted_bits = []
    for i in range(0, len(text), 64):
        block = text[i:i + 64]
        encrypted_bits += des_encrypt_block(block, subkeys)

    return encrypted_bits

def des_encrypt_block(block, keys):
    """ Proceso completo de cifrado DES en 16 rondas para un bloque de 64 bits. """
    permuted_block = permutate(block, IP)
    l_half, r_half = permuted_block[:32], permuted_block[32:]

    for i in range(16):
        l_half, r_half = feistel_round(l_half, r_half, keys[i])

    final_block = permutate(r_half + l_half, FP)
    return final_block


# Para que no queden caracteres extraños
def bits_to_hex(bits):
    """ Convertir bits a una representación hexadecimal. """
    hex_str = ''
    for i in range(0, len(bits), 4):
        nibble = bits[i:i+4]
        hex_str += f'{int("".join(map(str, nibble)), 2):x}'
    return hex_str

def hex_to_bits(hex_str):
    """ Convertir una cadena hexadecimal a bits. """
    bits = []
    for char in hex_str:
        bits += [int(bit) for bit in f'{int(char, 16):04b}']
    return bits

weak_keys_hex = [
    '0101010101010101',
    'fefefefefefefefe',
    '1f1f1f1f1f1f1f1',
    'e0e0e0e0e0e0e0e0'
]

semi_weak_keys_hex = [
    '01fe01fe01fe01fe', 'fe01fe01fe01fe01',
    '1fe01fe01fe01fe0', 'e01fe01fe01fe01f',
    '01e001e001e001e0', 'e001e001e001e001',
    '1ffe1ffe1ffe1ffe', 'fe1ffe1ffe1ffe1f',
    '011f011f011f011f', '1f011f011f011f01',
    'e0fee0fee0fee0fe', 'fee0fee0fee0fee0'
]

possible_weak_keys = [
    '1f1f01010e0e0101', 'e00101e0f10101f1',
    '011f1f01010e0e01', 'fe1f01e0fe0e01f1',
    '1f01011f0e01010e', 'fe011fe0fe010ef1',
    '01011f1f01010e0e', 'e01f1fe0f10e0ef1',
    'fe0101fefe0101fe',
    'e0e00101f1f10101', 'e01f01fef10e01fe',
    'fefe0101fefe0101', 'e0011ffef1010efe',
    'fee01f01fef10e01', 'fe1f1ffefe0e0efe',
    'e0fe1f01f1fe0e01',    
    'fee0011ffef1010e', '1ffe01e00efe01f1',
    'e0fe011ff1fe010e', '01fe1fe001fe0ef1',
    'e0e01f1ff1f10e0e', '1fe001fe0ef101fe',
    'fefe1f1ffefe0e0e', '01e01ffe01f10efe',
    'fe1fe001fe0ef101', '0101e0e00101f1f1',
    'e01ffe01f10efe01', '1f1fe0e00e0ef1f1',
    'fe01e01ffe01f10e', '1f01fee00e0ef1f1',
    'e001fe1ff101fe0e', '011ffee0010efef1',
    '1f01e0fe0e01f1fe',
    '01e0e00101e1e101', '011fe0fe010ef1fe',
    '1ffee0010efef001', '0101fefe0101fefe',
    '1ffee0010ef1fe01', '1f1ffefe0e0efefe',
    '01fefe0101fefe01',    
    '1fe0e0f10ef1f10e', 'fefee0e0fefef1f1',
    '01fee01f01fef10e', 'e0fefee0f1fefef1',
    '01e0fe1f01f1fe0e', 'fee0e0fefef1f1fe',
    '1ffefe1f0efefe0e', 'e0e0fefef1f1fefe']



# Texto a cifrar
plaintext = "00011100110101"
# Clave de 8 caracteres (64 bits) para DES
key = "1f1f1f1f1f1f1f1"

# Cifrar el texto
ciphertext_bits = des_encrypt(plaintext, key)

# Convertir los bits cifrados a hexadecimal para mostrar un resultado legible
ciphertext_hex = bits_to_hex(ciphertext_bits)

# Mostrar el texto cifrado en formato hexadecimal
#print("Texto cifrado (hexadecimal):", ciphertext_hex)


print("\n 1. Claves débiles")
for weak_key in weak_keys_hex:
    ciphertext_bits = des_encrypt(plaintext, weak_key)
    print("\nKey:", weak_key)
    print("Texto cifrado:", bits_to_hex(ciphertext_bits))
    """count = -1
    for bit in ciphertext_bits:
        count += 1
        if count == 8:
            print(" ", end="")
            count = 0
        print(bit, end="")"""

"""print("\n 2. Claves semi-débiles")
for semi_weak_key in semi_weak_keys_hex:
    ciphertext_bits = des_encrypt(plaintext, semi_weak_key)
    print("Key:", semi_weak_key)
    print("Texto cifrado:", bits_to_hex(ciphertext_bits))

print("\n 3. Posibles claves débiles")
for possible_weak_key in possible_weak_keys:
    ciphertext_bits = des_encrypt(plaintext, possible_weak_key)
    print("Key:", possible_weak_key)
    print("Texto cifrado:", bits_to_hex(ciphertext_bits))"""



def get_valid_input(prompt, length, valid_range):
    while True:
        try:
            values = list(map(int, input(prompt).split()))
            if len(values) != length:
                print(f"Must enter exactly {length} numbers")
                continue
            if any(
                value < valid_range[0] or value > valid_range[1] for value in values
            ):
                print(f"Values must be between {valid_range[0]} and {valid_range[1]}")
                continue
            return values
        except ValueError:
            print("Invalid input. Please enter numbers only")


def get_key():
    while True:
        key = input("Enter 10-bit key (eg. 1010101010): ")
        if len(key) != 10 or not set(key).issubset({"0", "1"}):
            print("Invalid key! Key must be a 10-bit binary string(0's and 1's)")
            continue
        return [int(bit) for bit in key]


def shift(bits, n):
    return bits[n:] + bits[:n]


def generate_keys(key, p10, p8):
    p10_key = [key[i - 1] for i in p10]

    left = p10_key[:5]
    right = p10_key[5:]
    # Generate Key1 (1st shift)
    left1 = shift(left, 1)
    right1 = shift(right, 1)

    key1 = [(left1 + right1)[i - 1] for i in p8]

    # Generate Key2 (2nd shift)
    left2 = shift(left1, 2)
    right2 = shift(right1, 2)

    key2 = [(left2 + right2)[i - 1] for i in p8]

    return key1, key2


def encryption_decryption(block, key1, key2, encryption=True):
    IP = [2, 6, 3, 1, 4, 8, 5, 7]
    permuted = [block[i - 1] for i in IP]

    def round(right, key):
        # Expansion
        EP = [4, 1, 2, 3, 2, 3, 4, 1]
        expanded = [right[i - 1] for i in EP]
        # XOR with key
        xor = [e ^ k for e, k in zip(expanded, key)]
        # S-boxe
        s0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
        s1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]
        s0_val = s0[2 * xor[0] + xor[3]][2 * xor[1] + xor[2]]
        s1_val = s1[2 * xor[4] + xor[7]][2 * xor[5] + xor[6]]
        combined = [(s0_val >> 1) & 1, s0_val & 1, (s1_val >> 1) & 1, s1_val & 1]
        # Permutation
        p4 = [2, 4, 3, 1]
        return [combined[i - 1] for i in p4]

    # First round
    left, right = permuted[:4], permuted[4:]
    p4 = round(right, key1)
    new_right = [1 ^ p for l, p in zip(left, p4)]
    result = right + new_right

    # Swap and second round
    left, right = result[:4], result[4:]
    p4 = round(right, key2)
    new_right = [1 ^ p for l, p in zip(left, p4)]
    result = right + new_right

    # Inverse IP
    IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]
    return [result[i - 1] for i in IP_inv]


key = get_key()
p10 = get_valid_input("Enter P10 permutation (10 numbers 1-10): ", 10, (1, 10))
p8 = get_valid_input("Enter P8 permutation (8 numbers 1-10): ", 8, (1, 10))

key1, key2 = generate_keys(key, p10, p8)

plaintext = list(map(int, input("Enter 8-bit plaintext (eg. 10101010): ")))
ciphertext = encryption_decryption(plaintext, key1, key2)
print("Ciphertext:", "".join(map(str, ciphertext)))

decrypted = encryption_decryption(ciphertext, key1, key2, False)
print("Decrypted:", "".join(map(str, decrypted)))

def create_keyed_ascii_polybius_grid(key=""):
    all_chars = [chr(i) for i in range(32, 127)]  # Printable ASCII
    seen = set()
    ordered_chars = []

    for char in key:
        if char in all_chars and char not in seen:
            ordered_chars.append(char)
            seen.add(char)

    for char in all_chars:
        if char not in seen:
            ordered_chars.append(char)

    grid = {}
    reverse_grid = {}
    index = 0
    for row in range(10):
        for col in range(10):
            if index < len(ordered_chars):
                code = f"{row}{col}"
                grid[ordered_chars[index]] = code
                reverse_grid[code] = ordered_chars[index]
                index += 1

    return grid, reverse_grid

def encrypt_ascii_polybius(text, key=""):
    grid, _ = create_keyed_ascii_polybius_grid(key)
    return " ".join(grid.get(char, "??") for char in text)

def decrypt_ascii_polybius(code, key=""):
    _, reverse_grid = create_keyed_ascii_polybius_grid(key)
    return "".join(reverse_grid.get(part, "?") for part in code.split())

# 🔽 NEW: Read from file
def read_text_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return ""
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

# 🔼 NEW: Write to file
def write_text_to_file(filename, content):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Output written to '{filename}'")
    except Exception as e:
        print(f"Error writing to file: {e}")

# 🧪 Example Usage
if __name__ == "__main__":
    key = "TOPSECRET"
    input_file = "C:\\Users\\User\\csd\\cybr-250\\raw.txt"
    output_file = "C:\\Users\\User\\csd\\cybr-250\\encrypted.txt"

    # Encrypt from file
    plaintext = read_text_from_file(input_file)
    encrypted = encrypt_ascii_polybius(plaintext, key)
    write_text_to_file(output_file, encrypted)

    # To decrypt:
    # encrypted = read_text_from_file("encrypted.txt")
    # decrypted = decrypt_ascii_polybius(encrypted, key)
    # write_text_to_file("decrypted.txt", decrypted)

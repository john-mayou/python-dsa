DOC = """Write a Python program that inputs a document and then outputs a bar-chart
plot of the frequencies of each alphabet character that appears in that document."""

def main():
    char_map = {}
    for char in DOC:
        if char in char_map:
            char_map[char] += 1
        else:
            char_map[char] = 1
    for char, count in sorted(char_map.items(), key=lambda x: -x[1]):
        print(f"{char}: {'*' * count}")

if __name__ == "__main__": main()
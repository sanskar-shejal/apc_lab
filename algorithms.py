def run_length_encoding(s: str) -> str:
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result


def main():
    input_str = "aaabbccccd"
    compressed = run_length_encoding(input_str)
    print(f"Original Input  : '{input_str}'")
    print(f"RLE Compressed  : '{compressed}'")

    input_str2 = "WWWWWWAAAAAABBBBBCCCCCC"
    print(f"Original Input 2: '{input_str2}'")
    print(f"RLE Compressed 2: '{run_length_encoding(input_str2)}'")


if __name__ == "__main__":
    main()

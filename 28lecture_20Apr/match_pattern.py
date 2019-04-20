import re

def main():
    text = "This is text -- with punctuation"
    pattern = 'T\w+'
    with_case = re.compile(pattern)
    without_case = re.compile(pattern, re.IGNORECASE)

    print("Text : ", text)
    print("Pattern : ", pattern)
    print("Case-sensitive : ", with_case.findall(text))
    print("Case-insensitive : ", without_case.findall(text))

if __name__ == "__main__":
    main()
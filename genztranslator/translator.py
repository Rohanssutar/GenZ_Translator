import re
from slangs import slang_dict

def translate(text: str) -> str:
    for slang in sorted(slang_dict, key=len, reverse=True):
        text = re.sub(r'\b' + re.escape(slang) + r'\b', slang_dict[slang], text, flags=re.IGNORECASE)
    return text

def main():
    sentence = input("Enter a sentence: ")
    print("Meaning:", translate(sentence))

if __name__ == "__main__":
    main()
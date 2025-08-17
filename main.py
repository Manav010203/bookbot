import sys
from stats import num_of_words
from stats import lower_case
from stats import report
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_file=sys.argv[1]
    # path_file = #"books/frankenstein.txt"
    content = get_book_text(path_file)
    num_words  = num_of_words(content)
    # print(f"{num_words} words found in the document")
    res = lower_case(content)
    # print(res)
    
    report(num_words,path_file,res)

if __name__ == "__main__":
    main()

def num_of_words(text):
    return len(text.split())
def lower_case(text):
    ans = {}
    for ch in text.lower():
        if ch in ans:
            ans[ch]+=1
        else:
            ans[ch]=1
    return ans
def sort_on(items):
    return items[""]
def report(num_words , path_file,item):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char,count in sorted(item.items(),key=lambda x:x[1],reverse=True):
        if char.isalpha():
            print(f"{char}:{count}")
    print("============= END ===============")


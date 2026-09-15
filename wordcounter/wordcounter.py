# always write dummy structure of the set first 
# wordcounts = {
#     "the": 3,
#     "fox": 2,
#     "quick": 1
# }

def count_word(word):
    wordcounts = {} # store the word and its repetetiveness
    wordlow = word.lower()
    wordlist = wordlow.split() # stores all word give by user in one list
    for word in wordlist:
        if word in wordcounts:
            wordcounts[word] += 1
        else:
            wordcounts[word] = 1
    return wordcounts



while True:
    print("=== Word Counter ===\n")
    word = input("Enter your text (or 'quit' to exit)\n")
    if word.lower() == "quit":
        print("GoodBye!")
        break
    if not word.strip():
        print("Please enter some text.\n")
        continue

    wordcounts = count_word(word)

    print("=== Word Counter Results ===\n")
    print(f"{'Word':<15} {'Count':<5}")
    print("-"*40)

    for word, count in sorted(wordcounts.items(), key=lambda item: item[1], reverse=True):
        print(f"{word:<15} {count:<5}")

    print(f"Total unique word: {len(wordcounts)} ")
    print(f"Total word count: {sum(wordcounts.values())} ") # kita tgok hasil tambah value semua yang kira kira tadi  "the": 3, part 3 tu yang kita tambah 
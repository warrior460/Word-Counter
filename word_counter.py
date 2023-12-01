def count_words(filename, search_words):
    # Read the file contents
    with open(filename, 'r') as f:
        file_contents = f.read()

    # Convert the file contents to lowercase for case-insensitive search
    file_contents = file_contents.lower()

    # Split the file contents into words
    words = file_contents.split()

    # Count the occurrences of each search word
    word_counts = {}
    for word in search_words:
        word_counts[word] = 0
        for file_word in words:
            if file_word == word:
                word_counts[word] += 1

    return word_counts

# Get the filename and list of search words from the user
filename = 'file.txt'

search_words = ['java', 'python', 'php', 'Hello', 'oop' ]

# Count the occurrences of the search words in the file
word_counts = count_words(filename, search_words)

# Display the word counts
for word, count in word_counts.items():
    print(f"{word}: {count}")

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents

def count_characters(s: str):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    result = [{"character": char, "count": count} for char, count in char_count.items()]
    ordered = sorted(result, key=lambda x: x["count"], reverse=True)
    return ordered

book = main()
words = len(book.split())
chtrs = count_characters(book.lower())

report = ''

for ch in chtrs:
    if ch['character'].isalpha():
        report += f"The '{ch['character']}' character was found {ch['count']} times\n"

print(f'''
--- Begin report of books/frankenstein.txt ---
{words} words found in the document
{report}
--- End report ---'''
      )
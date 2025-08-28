def reverse_words(sentence):
    result = sentence.split()
    left, right = 0, len(result) - 1

    while left <= right:
        result[left], result[right] = result[right], result[left]
        left += 1
        right -= 1

    return " ".join(result)

def reverse_words1(sentence):

    rev = ""
    words = sentence.strip().split()
    for word in words[::-1]:
        rev += " "+word
    return rev.strip()

print(reverse_words("Sun rises in the east"))
print(reverse_words1("Sun sets in the west"))
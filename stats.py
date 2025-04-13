def count_book_word(text):
    return len(text.split())
def count_time_char(text):
    result = {}
    words = text.split()
    for word in words:
        lower_word = word.lower()
        for char in lower_word:
            if char not in result:
                result[char] = 0
            result[char] +=1
    return result
def sort_on(dict):
    return dict["count"]
def sort_time_char(dict):
    list_dict = []
    for entry in dict:
        if entry.isalpha():
            list_dict.append({"letter": entry, "count": dict[entry]})
 
    list_dict.sort(reverse=True, key=sort_on)
    return list_dict
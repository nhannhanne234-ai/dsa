def group_by_first_letter(words):
    groups = {}
    for word in words:
        key = word[0]
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    return groups

words = ["meow", "gaugau", "kingbob", "anh", "papoi", "thatlongyeuem", "nhoemlam", "choanhcohoinha", "lop", "nguoidung"]

result = group_by_first_letter(words)
for key, value in result.items():
    print(f"{key}: {value}")
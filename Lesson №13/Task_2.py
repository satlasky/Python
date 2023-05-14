def format_names(names):
    formatted_names = []
    for name in names:
        name = ''.join([i.lower() for i in name if i.isalpha() or i == ' ']).capitalize()
        formatted_names.append(name)
    return formatted_names

s = ['анТОн', 'НАТАЛЬЯ', 'никита', 'МаРиЯ', '!СЕРГЕЙ!', 'Владимир747', 'Павел+100500']
formatted_s = format_names(s)
print(formatted_s)
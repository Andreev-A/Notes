def input_note_text(title):
    add_note_text = '*'
    while add_note_text != '':
        add_note_text = input('Добавить (или "enter" для выхода): ')
        if add_note_text != '':
            text_notes[title] += '___' + add_note_text


with open('D:\\notes.txt', 'r', encoding='cp1251') as inf:
    text_notes_in_memory = inf.read().strip().split('\n')
    text_notes, ident = {}, {}
    for string in text_notes_in_memory:
        string = (string.strip().split('***'))
        ident[string[0]] = string[1]
        text_notes[string[1]] = string[2]
        print(string[0], '-', string[1])
    my_request = input('Введите номер нужной записи или "enter" для новой записи: ')
    if my_request in ident.keys():
        print('ОТВЕТ: ', *text_notes[ident[my_request]].split('___'), sep='\n- ')
    elif my_request == '':
        note_title = input('Название заметки: ').lower()
        if note_title != '':
            if note_title in text_notes.keys():
                print('ЕСТЬ ТАКАЯ: ', *text_notes[note_title].split('___'), sep='\n- ')
            else:
                note_text = input('Заметка: ')
                text_notes[note_title] = note_text
            input_note_text(note_title)
with open('D:\\notes.txt', 'w') as ouf:
    count = 0
    for note_title, note_text in text_notes.items():
        count += 1
        print(str(count) + '***' + note_title + '***' + note_text, file=ouf)

# with open(path, 'rb') as f:
#   contents = f.read()
# with open('D:\\notes.txt', 'r', encoding='utf-8') as inf:
#     data = inf.read().strip().split('\n')
# with open(filename, encoding=encoding) as file:
# encoding='cp1251'

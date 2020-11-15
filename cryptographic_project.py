from random import choice, randint

txt = input("Введите текст: ").lower()
chars = {}
bad_syms = (' ', ',', '.', ':', ';', '?', '!')

for i in txt:
	if i not in chars.keys() and i not in bad_syms:
		chars[i] = 1
	elif i not in bad_syms:
		chars[i] += 1
	else:
		if i != ' ':
			txt.replace(i, '')

txt = txt.split(' ')
mx = max(chars.values())
add_txt = ''

while bool(chars):
	r_char = choice(tuple(chars.keys()))
	if chars[r_char] < mx:
		add_txt += r_char
		chars[r_char] += 1
	else:
		chars.pop(r_char)

splt = randint(1, 6)
while splt < len(add_txt):
	txt.insert(randint(1, len(txt)), add_txt[0:splt])
	add_txt = add_txt.replace(add_txt[0:splt], '')
	splt = randint(1, 6)

txt.insert(randint(1, len(txt)), add_txt[0:splt])

print(' '.join(txt))

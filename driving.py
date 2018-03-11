country = input('國籍')
age = input('年齡')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('許可')
	else:
		print('不許可')
country = input('國籍: ')
age = input('年齡: ')
age = int(age)
if country == '台灣':
	if age >= 18:
		print('許可')
	else:
		print('不許可')
elif country =='美國':
	if age >= 16:
		print('許可')
	else:
		print('不許可')
else:
	print('只能輸入台灣或美國')
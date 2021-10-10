a,b,c,d,e,f,g,k,l = (0,)* 9
def function(a,b,c,d,e,f,g,k,l):
	print ('Введите длину комнаты (в метрах): ')
	try:
		a = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите ширину комнаты (в метрах): ')
	try:
		b = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите высоту комнаты (в метрах):')
	try:
		c = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите ширину оконного проёма (в метрах): ')
	try:
		d = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите высоту оконного проёма (в метрах): ')
	try:
		e = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите ширину дверного проёма (в метрах): ')
	try:
		f = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите высоту дверного проёма (в метрах): ')
	try:
		g = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите ширину рулона обоев (в метрах): ')
	try:
		k = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	print ('Введите длину рулона обоев (в метрах): ')
	try:
		l = float(input ())
	except ValueError:
		print("Неверный формат.")
		exit()
	n = (((2*a*b) + (2*b*c) + (2*a*c) - (2*d*e) - (f*g))//(k*l))+1
	print("Вам понадобится", n,"рулонов")
function(a,b,c,d,e,f,g,k,l)
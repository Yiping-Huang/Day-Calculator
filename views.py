from django.shortcuts import render, redirect
from .day_calculator import day_calculation

def daycalculate(request):
	""" Calculate the days between two dates. """
	A_check = 0
	B_check = 0
	C_check = 0
	D_check = 0
	E_check = 0
	Aresult = 0
	Bresult = 0
	Cresult = 0
	Dresult = 0
	Eresult = 0

	if request.POST.get('Ayear_1') and request.POST.get('Amonth_1') and request.POST.get('Aday_1') and request.POST.get('Ayear_2') and request.POST.get('Amonth_2') and request.POST.get('Aday_2'):
		Ayear_1 = int(request.POST.get('Ayear_1'))
		Amonth_1 = int(request.POST.get('Amonth_1'))
		Aday_1 = int(request.POST.get('Aday_1'))
		Ayear_2 = int(request.POST.get('Ayear_2'))
		Amonth_2 = int(request.POST.get('Amonth_2'))
		Aday_2 = int(request.POST.get('Aday_2'))
		A_check = 1
		Aresult = day_calculation(Ayear_1, Amonth_1, Aday_1, Ayear_2, Amonth_2, Aday_2)
		
	if request.POST.get('Byear_1') and request.POST.get('Bmonth_1') and request.POST.get('Bday_1') and request.POST.get('Byear_2') and request.POST.get('Bmonth_2') and request.POST.get('Bday_2'):
		Byear_1 = int(request.POST.get('Byear_1'))
		Bmonth_1 = int(request.POST.get('Bmonth_1'))
		Bday_1 = int(request.POST.get('Bday_1'))
		Byear_2 = int(request.POST.get('Byear_2'))
		Bmonth_2 = int(request.POST.get('Bmonth_2'))
		Bday_2 = int(request.POST.get('Bday_2'))
		B_check = 1
		Bresult = day_calculation(Byear_1, Bmonth_1, Bday_1, Byear_2, Bmonth_2, Bday_2)

	if request.POST.get('Cyear_1') and request.POST.get('Cmonth_1') and request.POST.get('Cday_1') and request.POST.get('Cyear_2') and request.POST.get('Cmonth_2') and request.POST.get('Cday_2'):
		Cyear_1 = int(request.POST.get('Cyear_1'))
		Cmonth_1 = int(request.POST.get('Cmonth_1'))
		Cday_1 = int(request.POST.get('Cday_1'))
		Cyear_2 = int(request.POST.get('Cyear_2'))
		Cmonth_2 = int(request.POST.get('Cmonth_2'))
		Cday_2 = int(request.POST.get('Cday_2'))
		C_check = 1
		Cresult = day_calculation(Cyear_1, Cmonth_1, Cday_1, Cyear_2, Cmonth_2, Cday_2)
	
	if request.POST.get('Dyear_1') and request.POST.get('Dmonth_1') and request.POST.get('Dday_1') and request.POST.get('Dyear_2') and request.POST.get('Dmonth_2') and request.POST.get('Dday_2'):
		Dyear_1 = int(request.POST.get('Dyear_1'))
		Dmonth_1 = int(request.POST.get('Dmonth_1'))
		Dday_1 = int(request.POST.get('Dday_1'))
		Dyear_2 = int(request.POST.get('Dyear_2'))
		Dmonth_2 = int(request.POST.get('Dmonth_2'))
		Dday_2 = int(request.POST.get('Dday_2'))
		D_check = 1
		Dresult = day_calculation(Dyear_1, Dmonth_1, Dday_1, Dyear_2, Dmonth_2, Dday_2)
	
	if request.POST.get('Eyear_1') and request.POST.get('Emonth_1') and request.POST.get('Eday_1') and request.POST.get('Eyear_2') and request.POST.get('Emonth_2') and request.POST.get('Eday_2'):
		Eyear_1 = int(request.POST.get('Eyear_1'))
		Emonth_1 = int(request.POST.get('Emonth_1'))
		Eday_1 = int(request.POST.get('Eday_1'))
		Eyear_2 = int(request.POST.get('Eyear_2'))
		Emonth_2 = int(request.POST.get('Emonth_2'))
		Eday_2 = int(request.POST.get('Eday_2'))
		E_check = 1
		Eresult = day_calculation(Eyear_1, Emonth_1, Eday_1, Eyear_2, Emonth_2, Eday_2)

	if A_check + B_check + C_check + D_check + E_check == 0:
		result = "您尚未输入完整数据！You have not submitted complete data yet!"
	
	if A_check + B_check + C_check + D_check + E_check >= 1:
		if Aresult == 'unfit' or Bresult == 'unfit' or Cresult == 'unfit' or Dresult == 'unfit' or Eresult == 'unfit':
			result = "您输入了不合适的数据！You have submitted improper data!"
		else:
			result = "共计 " + str(Aresult + Bresult + Cresult + Dresult + Eresult) + " 天。There are " + str(Aresult + Bresult + Cresult + Dresult + Eresult) + " days in total."

	context = {'result': result}
	return render(request, 'ect_cal/daycalculate.html', context)

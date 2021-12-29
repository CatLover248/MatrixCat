from datetime import datetime

def getDT():
	dateandtimern_v1 = datetime.now()
	dateandtimern_v2 = dateandtimern_v1.strftime("%d/%m/%Y %H:%M:%S")
	return str(dateandtimern_v2)
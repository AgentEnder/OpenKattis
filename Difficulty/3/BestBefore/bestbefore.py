#Best Before, OpenKattis, https://open.kattis.com/problems/bestbefore
#Sln by Craigory Coppola

days_in_months = {
	1:31,
	2:28,
	3:31,
	4:30,
	5:31,
	6:30,
	7:31,
	8:31,
	9:30,
	10:31,
	11:30,
	12:31
}

leap_years = [2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060, 2064, 2068, 2072, 2076, 2080, 2084, 2088, 2092, 2096]

def is_leap_year(year):
	return (year in leap_years)

def days_before_year(year):
	lcount = 0
	for lyear in leap_years:
		if lyear > year:
			break
		lcount +=1
	return (year-lcount)*365+(lcount)*366
	

def getDateInt(y,m,d):
	days = days_before_year(y-1)
	days+=sum([get_days_in_month(x,y) for x in range(1,m)])+d
	return days

def get_days_in_month(m, y):
	if m == 2 and y in leap_years:
		return 29
	else:
		return days_in_months[m]

original = input()
input_map = {idx:int(value) for idx,value in enumerate(original.split("/"))}
		
years = input_map
days = {idx:value for idx, value in years.items() if value <= 31 and value is not 0}
months = {idx:value for idx, value in years.items() if value <= 12 and value is not 0}

curr_min = None
curr_min_out = ""

for year_idx, year in years.items():
	if year < 2000:
		year+=2000
	for month_idx, month in months.items():
		if month_idx == year_idx:
			continue
		for day_idx, day in days.items():
			if day_idx == month_idx or day_idx == year_idx or day > get_days_in_month(month, year) :
				continue
			date_int = getDateInt(year,month,day)
			if curr_min == None or curr_min > date_int:
				curr_min = date_int
				curr_min_out = "{0}-{1:02d}-{2:02d}".format(year,month,day)
if curr_min == None:
	print(original + " is illegal")
print(curr_min_out)
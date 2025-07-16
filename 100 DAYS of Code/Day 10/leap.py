# leap

def isYearLeap(year):
	"""Take a first and last name and format it to
	return the title case version of the name.

	Args:
		year (int): Year for leep check
	Returns:
		bool: Leep yes or no
	"""
	if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
		return True
	else:
		return False

year = int(input("Enter the year: "))
isLeap = isYearLeap(year)

if isLeap == True:
	print(f"Year {year} IS leap year.")
else:
	print(f"Year {year} IS NOT leap year.")
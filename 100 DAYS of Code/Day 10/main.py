#Day 10, functions with output

def format_name(fName, lName):
	if fName == "" or lName == "":
		return "You didn't provide valid inputs."
	formated_f_name = fName.title()
	formated_l_name = lName.title()

	return f"{formated_f_name} {formated_l_name}"

name = format_name('', 'LUKAS')
print(f"title name: {name}")
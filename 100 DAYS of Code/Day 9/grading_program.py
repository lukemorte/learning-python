# Grading program

student_scores = {
	'Harry': 88,
	'Ron': 78,
	'Hermione': 95,
	'Draco': 75,
	'Neville': 60
}

student_grades = {}

for student in student_scores:
	score = student_scores[student]

	if score >= 91:
		student_grades[student] = 'Outstanding'
	elif score >= 81:
		student_grades[student] = "Exceeds Expectations"
	elif score >= 71:
		student_grades[student] = "Acceptable"
	else:
		student_grades[student] = "Fail"

print("SCORE:")
print("------------------")
for student in student_scores:
	print(f"{student}: {student_scores[student]}")

print("")
print("GRADES:")
print("------------------")
for student in student_grades:
	print(f"{student}: {student_grades[student]}")
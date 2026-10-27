midterm = float(input("Enter the midterm score: "))
final = float(input("Enter the final score: "))

average = 0.4 * midterm + 0.6 * final

print("Average:", format(average, ".2f"))

if average >= 80:
    print("Excellent!")
elif average >= 60:
    print("Passed")
else:
    print("Failed")
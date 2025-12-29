def analyze_marks(marks):
    total = sum(marks)
    average = total / len(marks)

    highest = max(marks)
    lowest = min(marks)

    return total, average, highest, lowest


student_marks = [78, 85, 92, 66, 74]

total, avg, high, low = analyze_marks(student_marks)

print("Total marks:", total)
print("Average marks:", avg)
print("Highest marks:", high)
print("Lowest marks:", low)

test_score = int(input("Enter your test score: "))
if test_score >= 80 and test_score <= 100:
    performance = "Excellent"
elif test_score >= 50 and test_score < 80:
    performance = "Good"
elif test_score >= 0 and test_score < 50:
    performance = "Needs Improvement"
else:
    performance = "Invalid score entered."

print ("", performance)



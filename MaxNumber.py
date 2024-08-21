Student_Score = [123,456,789,321,987,543,923]
max_number = max(Student_Score)
print(max_number)

max_score = 0
for score in Student_Score:
    if score > max_score:
        max_score = score
print(max_score)
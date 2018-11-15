key = ['D',  'B',  'D',  'C',  'C',  'D',  'A',  'E',  'A',  'D'] 

student_answers =  [ 
	 ['A'  ,'B',  'A',  'C',  'C',  'D',  'E',  'E',  'A',  'D'],
	 ['D', 'B',  'A',  'B',  'C',  'A',  'E',  'E',  'A',  'D'], 
	 ['E', 'D',  'D',  'A',  'C',  'B',  'E',  'E',  'A',  'D'],
	 ['C', 'B',  'A',  'E',  'D',  'C',  'E',  'E',  'A',  'D'], 
	 ['A', 'B',  'D',  'C',  'C',  'D',  'E',  'E',  'A',  'D'], 
	 ['B', 'B',  'E',  'C',  'C',  'D',  'E',  'E',  'A',  'D'], 
	 ['B', 'B',  'A',  'C',  'C',  'D',  'E',  'E',  'A',  'D'], 
	 ['E', 'B',  'E',  'C',  'C',  'D',  'E',  'E',  'A',  'D'] 
  ] 

score = [0,0,0,0,0,0,0,0]

for i in range(8):
	for j in range(10):
		if(student_answers[i][j]==key[j]):
			score[i] += 1

print(score)


# print(score,"\n\n")

# i = 0
# for ans in student_answers:
# 	score=0
# 	for q in range(10):
# 		if key[q]==ans[q]:
# 			score=score+1
# 	i += 1
# 	print("Student ", i, " scored: ", score)


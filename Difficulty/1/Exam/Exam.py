#Exam, OpenKattis, https://open.kattis.com/problems/exam
#Sln by MSU ICPC TEAM FA 2018
num_correct = int(input())
my_answers = input()
his_answers = input()
num_questions = len(my_answers)
same = len([my_answers[i] == his_answers[i] for i in range(num_questions) if (my_answers[i] == his_answers[i]) == True])
diff = num_questions-same
if same <= num_correct:
    print(num_questions-(num_correct-same))
else:
    print(num_correct+num_questions-same)
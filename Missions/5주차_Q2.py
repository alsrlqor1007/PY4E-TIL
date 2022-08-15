def grader(students_answer, answer_sheet):
    problem_counts = len(answer_sheet)

    student_list = list()
    for el in students_answer:
        answers = el.split(',')[1]
        score = 0
        problem_num = 0

        while problem_num < problem_counts:
            if int(answers[problem_num]) == answer_sheet[problem_num]:
                score += 10
            problem_num += 1

        student_list.append((el.split(',')[0], score))

    student_tuple_inorder = sorted(
        student_list, key=lambda student_info: -student_info[1])

    for name, score in student_tuple_inorder:
        rank = student_tuple_inorder.index((name, score)) + 1
        print(f'학생: {name} 점수: {score}점 {rank}등')


# 학생 답
s = ["김갑,3242524215",
     "이을,3242524223",
     "박병,2242554131",
     "최정,4245242315",
     "정무,3242524315"]

# 정답지
a = [3, 2, 4, 2, 5, 2, 4, 3, 1, 2]

grader(s, a)

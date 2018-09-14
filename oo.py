class Student:
    """A class for students with name and address"""

    def __init__(self, f_name, l_name, address):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address


class Question:
    """A class for questions with correct answers"""

    def __init__(self,question,correct_a):
        self.question = question
        self.correct_a = correct_a

    def ask_and_evaluate(self):
        answer = input('{}: ' .format(self.question))
        return answer == self.correct_a
                


class Exam:
    """A class for exams with questions"""

    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        correct_count = 0
        for self.question in self.questions:
            if self.question.ask_and_evaluate():
                correct_count +=1

        return (correct_count/len(self.questions))* 100


class StudentExam:
    """A class that store student, exam and score"""

    def __init__(self, student, exam):
        self.exam = exam
        self.student = student

    def take_test(self):
        self.score = self.exam.administer()
        print("Student's score is {}".format(self.score))


def example():
    exam = Exam('Midterm')
    set_q = Question('What is the method for adding an element to a set?','.add()')
    exam.add_question(set_q)
    pwd_q = Question('What does pwd stand for?','print working directory')
    exam.add_question(pwd_q)
    list_q = Question('Python lists are mutable, iterable, and what?','ordered')
    exam.add_question(list_q)
    student1 = Student("Jasmine", "Debugger", "0101 Computer Street")
    studentExam1 = StudentExam(student1, exam)
    studentExam1.take_test()

example()
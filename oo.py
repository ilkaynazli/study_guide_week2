class Student():
    """A class for students with name and address"""

    def __init__(self, f_name, l_name, address):
        self.f_name = f_name
        self.l_name = l_name
        self.address = address


class Question():
    """A class for questions with correct answers"""

    def __init__(self,question,correct_a):
        self.question = question
        self.correct_a = correct_a

    def ask_and_evaluate(self):
        answer = input('{}: ' .format(self.question))
        return answer == self.correct_a
                


class Exam():
    """A class for exams with questions"""

    def __init__(self, name, questions=[]):
        self.name = name
        self.questions = questions

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        correct_count = 0
        for self.question in self.questions:
            if self.question.ask_and_evaluate():
                correct_count +=1

        return (correct_count/len(self.questions))* 100



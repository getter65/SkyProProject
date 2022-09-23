class Question:
    def __init__(self, text_question, difficult, answer):
        self.text_question = text_question
        self.difficult = difficult
        self.answer = answer
        self.is_asked = False
        self.player_answer = None
        self.points = self.get_points()

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """
        return int(self.difficult) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответов иначе False.
        """
        return self.player_answer == self.answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """
        return f"Вопрос: {self.text_question}\nСложность: {self.difficult}/5"

    def build_feedback(self):
        """Возвращает :
        Ответ верный, получено __ баллов

        Возвращает :
        Ответ неверный, верный ответ __
        """
        if self.is_correct():
            return f"Ответ верный, получено {self.points} баллов\n"

        return f"Ответ неверный, верный ответ {self.answer}\n"

from json import load
from question import Question
from random import shuffle


def load_data(filepath):
    with open(filepath, encoding='utf-8') as file:
        data = load(file)

    return data


def retrieve_list_questions(question_data: list):
    list_questions = []

    for question in question_data:
        list_questions.append(Question(question['q'], question['d'], question['a']))

    shuffle(list_questions)

    return list_questions


def get_player_answer():
    while True:
        player_answer = input("Пользователь: ")
        if player_answer.isdigit():
            return player_answer
        elif player_answer == 'stop':
            return player_answer
        else:
            print("Введи число")
            continue



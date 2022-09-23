from utils import load_data, retrieve_list_questions, get_player_answer


def main():
    question_data = load_data('question.json')
    question_objects = retrieve_list_questions(question_data)
    points_player = 0
    valid_answer = 0
    question_count = 0

    print("Игра начинается")

    for q_obj in question_objects:
        print(q_obj.build_question())
        player_answer = get_player_answer()
        question_count += 1

        if player_answer == "stop":
            print("Желаю удачи")
            break

        q_obj.player_answer = player_answer
        print(q_obj.build_feedback())

        if q_obj.is_correct():
            points_player += q_obj.get_points()
            valid_answer += 1

    print(f"Отвечено на {valid_answer} из {question_count}\nПолучено: {points_player} баллов.")


if __name__ == "__main__":
    main()

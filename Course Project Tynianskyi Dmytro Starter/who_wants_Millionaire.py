import random

# База запитань
questions_db = [
    {
        'question': 'Який континент найбільший за площею?',
        'options': ['Африка', 'Азія', 'Антарктида', 'Європа'],
        'answer': 'Азія'
    },
    {
        'question': 'Яка планета найближча до Сонця?',
        'options': ['Венера', 'Земля', 'Меркурій', 'Марс'],
        'answer': 'Меркурій'
    },
    {
        'question': 'Скільки кольорів у веселці?',
        'options': ['5', '6', '7', '8'],
        'answer': '7'
    }
    # Можна додати більше питань
]

# Сума виграшів за кожне питання
prizes = [100, 200, 300, 500, 1000, 2000, 4000, 8000,
          16000, 32000, 64000, 125000, 250000, 500000, 1000000]

# Функція 50/50


def fifty_fifty(question):
    options = question['options'].copy()
    options.remove(question['answer'])
    incorrect_option = random.choice(options)
    return [question['answer'], incorrect_option]

# Функція "Дзвінок другу" (випадковий вибір відповіді)


def phone_a_friend(question):
    return random.choice(question['options'])

# Функція "Допомога залу" (імітований відсоток голосів)


def ask_the_audience(question):
    correct_percentage = random.randint(50, 80)
    other_percentage = 100 - correct_percentage
    return {
        question['answer']: correct_percentage,
        random.choice([opt for opt in question['options'] if opt != question['answer']]): other_percentage
    }

# Функція для валідації відповіді


def check_answer(question, user_answer):
    return user_answer == question['answer']

# Основна гра


def millionaire_game():
    used_hints = {
        '50/50': False,
        'phone_a_friend': False,
        'ask_the_audience': False
    }

    current_question_index = 0
    total_prize = 0

    while current_question_index < len(questions_db):
        question = questions_db[current_question_index]
        print(f"\nПитання на {prizes[current_question_index]} гривень:")
        print(question['question'])
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")

        print("\nВиберіть дію:")
        print("1. Відповісти")
        print("2. Використати підказку (50/50, Дзвінок другу, Допомога залу)")
        print("3. Забрати виграш і завершити гру")

        choice = input("Ваш вибір: ")

        if choice == '1':
            user_answer = input("Ваша відповідь (введіть номер варіанту): ")
            selected_option = question['options'][int(user_answer) - 1]

            if check_answer(question, selected_option):
                print("Правильна відповідь!")
                total_prize = prizes[current_question_index]
                current_question_index += 1
            else:
                print("Неправильна відповідь! Гра завершена.")
                break

        elif choice == '2':
            print("\nВиберіть підказку:")
            print("1. 50/50")
            print("2. Дзвінок другу")
            print("3. Допомога залу")
            hint_choice = input("Ваш вибір: ")

            if hint_choice == '1' and not used_hints['50/50']:
                used_hints['50/50'] = True
                options = fifty_fifty(question)
                print("Залишилось два варіанти:", options)
            elif hint_choice == '2' and not used_hints['phone_a_friend']:
                used_hints['phone_a_friend'] = True
                print("Друг радить вибрати:", phone_a_friend(question))
            elif hint_choice == '3' and not used_hints['ask_the_audience']:
                used_hints['ask_the_audience'] = True
                audience_help = ask_the_audience(question)
                print("Допомога залу (відсотки):", audience_help)
            else:
                print("Підказка вже використана або вибрано неправильний варіант.")

        elif choice == '3':
            print(f"Ви вирішили завершити гру. Ваш виграш: {
                  total_prize} гривень.")
            break
        else:
            print("Неправильний вибір, спробуйте ще раз.")

    if current_question_index == len(questions_db):
        print(f"Вітаємо! Ви виграли максимальний приз: {prizes[-1]} гривень!")


# Запуск гри
if __name__ == "__main__":
    millionaire_game()



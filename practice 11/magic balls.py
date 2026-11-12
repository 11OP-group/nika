import random
answers = [
    "Бесспорно",
    "Предрешено",
    "Никаких сомнений",
    "Определенно да",
    "Можешь быть уверен в этом",
    "Мне кажется - да",
    "Сомнительно, но окей",
    "Хорошие перспективы",
    "Знаки говорят - да",
    "Да",
    "Пока неясно, попробуй снова",
    "Спроси позже",
    "Лучше не рассказывать",
    "Сейчас нельзя предсказать",
    "Сконцентрируйся и спроси опять",
    "Даже не думай",
    "Мой ответ - нет",
    "По моим данным - нет",
    "Перспективы не очень хорошие",
    "Весьма сомнительно"
]

print("Привет, Мир! Я магический шар, и я знаю ответ на любой твой вопрос!")

name = str(input("Как к Вам обращаться: "))

print(f"Ну здравствуй, {name}.")

flag = True
while True:
    question = str(input("Твой вопрос: "))
    random_answer = random.choice(answers)
    print(answer)

    continue_question = str(input("Хотите спросить еще что-нибудь? да/нет: "))
    continue_question.lower()
    while True:
        if continue_question == "да":
            break
        if continue_question == "нет":
            flag = False
            break
        else:
            print("Не понял Вас")
            continue
    if flag == False: break


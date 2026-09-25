from knowledge_base import knowledge_base

def get_answer(user_message):
    user_message = user_message.lower()
    for item in knowledge_base:
        for keyword in item["keywords"]:
            if keyword in user_message:
                return item["answer"]
    return "Извините, я не понял вопрос. Попробуйте переформулировать или позвоните нам по телефону."

print("Бот готов к работе! Напишите 'выход', чтобы закончить.")
while True:
    user_input = input("Вы: ")
    if user_input.lower() in ["выход", "exit", "quit"]:
        print("Бот: До свидания!")
        break
    print("Бот:", get_answer(user_input))
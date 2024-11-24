authors = {"Янка Купала": "Павлинка", 
           "Александр Грибоедов": "Горе от ума",
           "Масаси Кисимото": "Наруто", 
           "Артур Конан Дойль": "Возвращение шерлока холмса"}
quiz_points = 0
for author, work in authors.items():
    answer = input(f'Автор {work}: ')
    if answer.lower() == author.lower():
        quiz_points += 1

if quiz_points == 4:
    print('Вы набрали: ', quiz_points, 'очков')
elif quiz_points ==  3:
    print('Вы набрали: ', quiz_points, 'очков. Неплохо, но можно лучше')
elif quiz_points < 3:
    print('Вы набрали: ', quiz_points, 'очков. Плохо... Это классика, это знать надо!!!')
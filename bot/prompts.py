from string import Template

ONE_PROMPT = Template("""# Корпоративные ценности компании:
1. Человечность: Люди - самое главное. Мы одинаково хорошо относимся ко всем и верим в лучшие качества человека.
2. Свобода: Эксперту нужно доверять. Мы за доброжелательность, эмпатию, понимание, уважение, открытость, ориентацию на клиента, гибкость, непредвзятость и благодарность. Мы против грубости, скрытности, ранимости, лукизма, манипуляций, вспыльчивости и стереотипного мышления.
3. Свобода: Мы за самостоятельность в организации рабочего процесса и ответственность за результат. За доверие коллегам и команде в организации их рабочего процесса. Не принуждение, но вдохновение. Свобода = ответственность. Мы самостоятельные, можем ошибаться, пунктуальные, в безопасности, находчивые, здравомыслящие, командные, вовлеченные, смелые и компромиссные. Мы не контрол-фрики, не токсичны, не тираны и не обманщики.
4. Польза: Клиент знает, чего хочет, мы знаем как. Мы постоянно совершенствуем продукт, процессы, подходы и отношения. Ориентируемся на положительный опыт пользователей. Мы против ретроградства, покорности, беспомощности и безразличия.
5. Причастность: Для достижения результата нужно отдавать частицу себя. Мы за погружение в контекст, управление ожиданиями, гласность, нацеленность на результат, заинтересованность и аргументацию. Против рабочего эгоизма, закрытости, неуважения, авторитаризма и безответственности.

# Ситуация и ответ пользователя:

## Ситуация:
$situation

### Ответ пользователя:
$answer

# Инструкции для анализа:
1. Оценить, насколько ответ пользователя соответствуют корпоративным ценностям нашей компании.
2. Выявить проявления ценностей в ответе.
3. Сформулировать общие выводы о ценностях человека на основе его ответа.

# Ответ:
Сформулируй ответ для пользователя, где объяснишь, что в его ответе правильно, а что противоречит политике компании. Объясни ему, подходит ли нашей компании его позиция. Ответ должен быть без приветсвия и лишних повторений, так как пользователь думает, что в диалоге с тобой. Обращайся к пользователю на "ты"."""
)

FULL_PROMPT = Template("""# Корпоративные ценности компании:
1. Человечность: Люди - самое главное. Мы одинаково хорошо относимся ко всем и верим в лучшие качества человека.
2. Свобода: Эксперту нужно доверять. Мы за доброжелательность, эмпатию, понимание, уважение, открытость, ориентацию на клиента, гибкость, непредвзятость и благодарность. Мы против грубости, скрытности, ранимости, лукизма, манипуляций, вспыльчивости и стереотипного мышления.
3. Свобода: Мы за самостоятельность в организации рабочего процесса и ответственность за результат. За доверие коллегам и команде в организации их рабочего процесса. Не принуждение, но вдохновение. Свобода = ответственность. Мы самостоятельные, можем ошибаться, пунктуальные, в безопасности, находчивые, здравомыслящие, командные, вовлеченные, смелые и компромиссные. Мы не контрол-фрики, не токсичны, не тираны и не обманщики.
4. Польза: Клиент знает, чего хочет, мы знаем как. Мы постоянно совершенствуем продукт, процессы, подходы и отношения. Ориентируемся на положительный опыт пользователей. Мы против ретроградства, покорности, беспомощности и безразличия.
5. Причастность: Для достижения результата нужно отдавать частицу себя. Мы за погружение в контекст, управление ожиданиями, гласность, нацеленность на результат, заинтересованность и аргументацию. Против рабочего эгоизма, закрытости, неуважения, авторитаризма и безответственности.

# Ситуации и ответы пользователя:

## Ситуация 1:
$situation_1

### Ответ пользователя:
$answer_1

## Ситуация 2:
$situation_2

### Ответ пользователя:
$answer_2

## Ситуация 3:
$situation_3

### Ответ пользователя:
$answer_3

## Ситуация 4:
$situation_4

### Ответ пользователя:
$answer_4

## Ситуация 5:
$situation_5

### Ответ пользователя:
$answer_5

# Инструкции для анализа:
1. Оценить, насколько ответы пользователя соответствуют корпоративным ценностям нашей компании.
2. Выявить проявления ценностей в ответах.
3. Сформулировать общие выводы о ценностях человека на основе его ответов.

# Ответ:
ССформулируй для HR компании выводы о ценностях сотрудника. Объясни, подходит он компании или нет, аргментируй и обоснуй почему. Предоставь в том числе вероятность того, что сотрудник подошел бы компании в процентах. Ответь на вопрос: в каком случае этого сотрудника можно было бы взять в компанию?""")

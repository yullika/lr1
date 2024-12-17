# from flask import Flask, render_template, redirect, url_for, request, flash
# import telebot
# import threading
# import SQLTable as S
#
# app = Flask(__name__)
# app.secret_key = '345890ryh72'  # Замените на свой секретный ключ
#
# # Настройки базы данных
# db_config = {
#     'user': 'j1007852',
#     'password': 'el|N#2}-F8',
#     'host': 'srv201-h-st.jino.ru',
#     'database': 'j1007852_13423'
# }
#
# # Инициализация таблиц
# health_facts_table_name = 'health_facts'
# commands_table_name = 'commands'
# sql_table_health_facts = S.SQLTable(db_config, health_facts_table_name)
# sql_table_commands = S.SQLTable(db_config, commands_table_name)  #
#
# # Инициализация бота
# bot = telebot.TeleBot("7215978807:AAHv7CQEs31qHLOKEQ4PYEaFlZebSdUz7oU")
#
# @app.route('/')
# def index():
#     return render_template('index.html')
#
# @app.route('/add_fact', methods=['GET', 'POST'])
# def add_fact():
#     if request.method == 'POST':
#         fact = request.form.get('fact')
#         if fact:
#             sql_table_health_facts.insert_fact(fact)  # Метод для вставки факта в базу данных
#             flash('Факт успешно добавлен!', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('Введите факт!', 'danger')
#     return render_template('add_fact.html')
#
# @app.route('/view_facts')
# def view_facts():
#     facts = sql_table_health_facts.get_all_facts()  # Метод для получения всех фактов из базы данных
#     return render_template('view_facts.html', facts=facts)
#
# @app.route('/add_command', methods=['GET', 'POST'])
# def add_command():
#     if request.method == 'POST':
#         command = request.form.get('command')
#         if command:
#             # Здесь вы можете добавить логику для сохранения команды в базу данных
#             # Например, если у вас есть таблица для команд:
#             # sql_table_commands.insert_command(command)
#             flash('Команда успешно добавлена!', 'success')
#             return redirect(url_for('index'))
#         else:
#             flash('Введите команду!', 'danger')
#     return render_template('add_command.html')
#
# @app.route('/view_commands')
# def view_commands():
#     # Здесь вы можете добавить логику для получения команд из базы данных
#     # commands = sql_table_commands.get_all_commands()
#     return render_template('view_commands.html', commands=commands)
#
# # Запуск бота в отдельном потоке
# def run_bot():
#     bot.polling(none_stop=True)
#
# if __name__ == '__main__':
#     threading.Thread(target=run_bot).start()
#     app.run(host='0.0.0.0', port=5000)
from flask import Flask, render_template, redirect, url_for, request, flash
import telebot
import threading
import SQLTable as S

app = Flask(__name__)
app.secret_key = '345890ryh72'  # Замените на свой секретный ключ

# Настройки базы данных
db_config = {
    'user': 'j1007852',
    'password': 'el|N#2}-F8',
    'host': 'srv201-h-st.jino.ru',
    'database': 'j1007852_13423'
}

# Инициализация таблиц
health_facts_table_name = 'health_facts'
commands_table_name = 'commands'  # Предполагается, что у вас есть таблица для команд
sql_table_health_facts = S.SQLTable(db_config, health_facts_table_name)
sql_table_commands = S.SQLTable(db_config, commands_table_name)  # Инициализация таблицы команд

# Инициализация бота
bot = telebot.TeleBot("7215978807:AAHv7CQEs31qHLOKEQ4PYEaFlZebSdUz7oU")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_fact', methods=['GET', 'POST'])
def add_fact():
    if request.method == 'POST':
        fact = request.form.get('fact')
        if fact:
            sql_table_health_facts.insert_fact(fact)  # Метод для вставки факта в базу данных
            flash('Факт успешно добавлен!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Введите факт!', 'danger')
    return render_template('add_fact.html')

@app.route('/view_facts')
def view_facts():
    facts = sql_table_health_facts.get_all_facts()  # Получение всех фактов из базы данных
    return render_template('view_facts.html', facts=facts)

@app.route('/add_command', methods=['GET', 'POST'])
def add_command():
    if request.method == 'POST':
        command = request.form.get('command')
        if command:
            sql_table_commands.insert_command(command)  # Метод для вставки команды в базу данных
            flash('Команда успешно добавлена!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Введите команду!', 'danger')
    return render_template('add_command.html')

@app.route('/view_commands')
def view_commands():
    commands = sql_table_commands.get_all_commands()  # Получение всех команд из базы данных
    return render_template('view_commands.html', commands=commands)

# Запуск бота в отдельном потоке
def run_bot():
    bot.polling(none_stop=True)

if __name__ == '__main__':
    try:
        threading.Thread(target=run_bot).start()
        app.run(host='0.0.0.0', port=5000)
    finally:
        sql_table_health_facts.close()  # Закрываем соединение с базой данных
        sql_table_commands.close()  # Закрываем соединение с базой данных для команд

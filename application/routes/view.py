from application import app, db_get
from flask import render_template, request, redirect, url_for

@app.route('/view/<date>', methods=['POST', 'GET'])
def view(date):
    db = db_get()
    food_curr = db.execute('SELECT id, name FROM food')
    food_result = food_curr.fetchall()
    curr = db.execute('SELECT id, entry_date from log_date WHERE entry_date = ?', [date])
    result = curr.fetchone()
    totals = {'protein': 0, 'carbohydrates': 0, 'fat': 0, 'calories': 0}
    calories_sum_curr = db.execute('SELECT food_date.*, food.name, food.protein, food.carbohydrates, food.fat, food.calories,\
        log_date.entry_date FROM food_date INNER JOIN food on food_date.food_id = food.id\
        INNER JOIN log_date on food_date.log_date_id = log_date.id WHERE entry_date = ?', [date])
    calories_sum_result = calories_sum_curr.fetchall()
    for foo in calories_sum_result:
        totals['protein']+=foo['protein']
        totals['carbohydrates']+=foo['carbohydrates']
        totals['fat']+=foo['fat']
        totals['calories']+=foo['calories']
    if request.method == 'POST':
        db.execute('INSERT INTO food_date (food_id, log_date_id) values (?, ?)', [request.form['select-food'], result['id']])
        db.commit()
        return redirect(url_for('view', date = date))
    return render_template('view.html', title = 'View date', result = result, food_result = food_result, totals = totals, calories_sum_result = calories_sum_result, checked = True)


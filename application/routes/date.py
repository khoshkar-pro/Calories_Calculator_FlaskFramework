from application import app, db_get
from flask import render_template, request, redirect, url_for

@app.route('/date', methods = ['POST', 'GET'])
def date():
    db = db_get()
    if request.method == 'POST':
        form_date = request.form['datetime']
        db.execute('INSERT INTO log_date (entry_date) values (?)', [form_date])
        db.commit()
        return redirect(url_for('view', date=form_date))
    curr = db.execute('SELECT id, entry_date FROM log_date')
    result = curr.fetchall()
    join_curr = db.execute('SELECT food_date.*, food.name,food.protein, food.carbohydrates, food.fat,\
        food.calories, log_date.entry_date FROM food_date INNER JOIN food on food_date.food_id=food.id INNER JOIN log_date on\
        food_date.log_date_id=log_date.id ORDER by entry_date DESC')
    result_join = join_curr.fetchall()
    return render_template('date.html', title = 'Date', result_join = result_join, result = result)
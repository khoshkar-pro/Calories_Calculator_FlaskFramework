from application import app, db_get
from flask import render_template, request

@app.route('/food', methods=['POST', 'GET'])
def food():
    db = db_get()
    if request.method == 'POST':
        name = request.form['food-name']
        protein = int(request.form['protein'])
        carbohydrates = int(request.form['carbohydrates'])
        fat = int(request.form['fat'])
        calories = (protein * 4) + (carbohydrates * 4) + (fat * 9)
        db.execute('INSERT INTO food (name, protein, carbohydrates, fat, calories)\
         values (?,?,?,?,?)', [name, protein, carbohydrates, fat, calories])
        db.commit()
    curr = db.execute('SELECT name, protein, carbohydrates, fat, calories FROM food')
    result = curr.fetchall()
    return render_template('add_food.html', title = 'Add food', result = result)
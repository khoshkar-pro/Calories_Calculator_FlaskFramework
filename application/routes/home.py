from application import app, db_get
from flask import render_template, request

@app.route('/', methods=['POST','GET'])
@app.route('/home', methods=['POST','GET'])
def home():
    db = db_get()
    if request.method == 'POST':
        return None
    curr = db.execute(
        'SELECT sum(food.protein) as protein, sum(food.carbohydrates) as carbohydrates, sum(food.fat) as fat\
        , sum(food.calories) as calories, log_date.entry_date as entry_date FROM food_date\
         INNER JOIN food on food_date.food_id = food.id INNER JOIN log_date on food_date.log_date_id = log_date.id\
          GROUP by log_date.entry_date ORDER by log_date.entry_date DESC')
    result = curr.fetchall()
    return render_template('home.html', title = 'Home', result=result)
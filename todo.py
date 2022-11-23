from flask import Flask, render_template, request
app= Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', methods=['POST'])
def addTodo():
     todoItem = request.form['todoItem']
     print(todoItem)
     return (todoItem )
if __name__=="__main__":
    app.run(debug=True)
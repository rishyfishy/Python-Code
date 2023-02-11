from flask import Flask, redirect, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import time

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Todo(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    content=db.Column(db.String(200),nullable=False)
    #completed=db.Column(db.Integer,default=0)
    date_created=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self) -> str:
        return '<Task %r>'% self.id
    
    
    
    

# decorator within flask class to tell 
# python which url should trigger the decorated function
@app.route('/',methods=['POST','GET'])
def hello():
    
    if request.method=='POST':
        task_content=request.form['content']
        newTask=Todo(content=task_content)
        
        db.session.add(newTask)
        db.session.commit()
        return redirect('/')
        
    else:
        taskList = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=taskList)

if __name__=='__main__':
    app.run(debug=True)

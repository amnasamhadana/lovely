import dataset
from flask import Flask, render_template
app = Flask(__name__)

db= dataset.connect("sqlite:///:database.db")
table= db["table"]
@app.route('/')
def hello():
	return render_template(("lovely.html"), Mark = 20 , list1= [1,2,3])
table.insert(dict(Name="Amna", Age=16, Country= "Palestine"))
userList= list(db["table"].all())
table.update(dict(Name='Amna', Age=23), ['Name'])

print len (db["table"])
print userList
if __name__ == "__main__":
	app.run(port= 9009, debug= True)
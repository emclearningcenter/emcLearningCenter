from flask import Flask, render_template

@app.route('/') 

def hello(name=None): 
	return render_template('layout.html', name=name) 

if __name__ == '__main__': 
	app.run() 
		

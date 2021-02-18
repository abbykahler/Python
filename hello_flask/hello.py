
    
    # 1
# from flask import flask
# app = Flask(__name__)
# @app.route('/')
# def index():
#     return "hello world"
# if __name__=="__main__":   
#     app.run(debug=True) 

# 2

# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/dojo')          

# def dojo():
#     return "Dojo!"
# if __name__ = '__main__';
#     app.run(debug=True)

#  3
#  from flask import Flask  
# app = Flask(__name__)    
# @app.route('/say/flask')          

# def hello():
#     return "Hi flask!"

# if __name__=="__main__":   
#     app.run(debug=True) 

# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/say/michael')          

# def hello():
#     return "Hi Michael!"

# if __name__=="__main__":   
#     app.run(debug=True) 


# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/say/john')          

# def hello():
#     return "Hi John!"

# if __name__=="__main__":   
#     app.run(debug=True) 

4
# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/repeat/35/hello')          

# def hello():
#     return "Hello! " * 35

# if __name__=="__main__":   
#     app.run(debug=True) 

# from flask import Flask  
# app = Flask(__name__)    
# @app.route('/repeat/80/bye')          

# def hello():
#     return "bye! " * 80

# if __name__=="__main__":   
#     app.run(debug=True) 

from flask import Flask  
app = Flask(__name__)    
@app.route('/repeat/99/dogs')          

def hello():
    return "dogs " * 99

if __name__=="__main__":   
    app.run(debug=True) 
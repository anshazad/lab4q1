import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    # print(jsonStr)
    jsonObj = json.loads(jsonStr)
    response = ""
    s = jsonObj['temp1']
    k = int(jsonObj['temp2'])
    l = list(map(int, s.split(",")))
    l.sort()
    if len(l) == 0:
        return "No Element in List"
    temp = [l[0]]
    for i in range(1, len(l)):
        if temp[-1] == l[i]:
            temp.append(l[i])
            if i == len(l)-1:
                if len(temp) >= k:
                    response += str(temp[-1])
        else:
            if len(temp) >= k:
                response += str(temp[-1]) + ","
            temp = [l[i]]
    if response[-1] == ",":
        return response[0:len(response)-1]

    return response
        
            
     
        
        	
    

    
    response+="<b>" + str(list3) + "</b><br>"
   
   
        
    	    
    return response
    
     
if __name__ == "__main__":
    app.run(debug=True)
    
    

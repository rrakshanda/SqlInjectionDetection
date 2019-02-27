from flask import Flask,request,render_template
import random as rd

import pypyodbc

app = Flask(__name__)


@app.route("/")
def index():

    return render_template('index.html')


@app.route('/processLogin', methods=['GET'])
def processLogin():
    userid= request.args.get('userid')
    password= request.args.get('pwd')
    print("Your usename:",userid)
    print("Your Password:",password)
    # Example Grammar rules
    rules = {
        "booleanAttack":[
            [userid.partition(' ')[0],"booleanTrueExpr"],
        ],

        "opOr": [
            ["or",],
        ],
        "booleanTrueExpr": [
            ["opOr","unaryTrue"],
            ["opOr","binaryTrue"],
            ["unaryTrue"],
            ["binaryTrue"]

        ],
        "unaryTrue": [
            ["1","opEqual","1","hyphen"],
            ["2","opEqual","2","hyphen"],
            ["3","opEqual","3","hyphen"],
            ["4","opEqual","4","hyphen"],
            ["5","opEqual","5","hyphen"],
            ["6","opEqual","6","hyphen"],
            ["7","opEqual","7","hyphen"],
            ["8","opEqual","8","hyphen"],
            ["9","opEqual","9","hyphen"],
            ["0","opEqual","0","hyphen"],
            ["squote","1","squote","opEqual","squote","1","squote","hyphen"],
            ["squote","2","squote","opEqual","squote","2","squote","hyphen"],
            ["squote","3","squote","opEqual","squote","3","squote","hyphen"],
            ["squote","4","squote","opEqual","squote","4","squote","hyphen"],
            ["squote","5","squote","opEqual","squote","5","squote","hyphen"],
            ["squote","6","squote","opEqual","squote","6","squote","hyphen"],
            ["squote","7","squote","opEqual","squote","7","squote","hyphen"],
            ["squote","8","squote","opEqual","squote","8","squote","hyphen"],
            ["squote","9","squote","opEqual","squote","9","squote","hyphen"],
            ["squote","0","squote","opEqual","squote","0","squote","hyphen"],


        ],
        "binaryTrue":[
            ["parOpen","1","opEqual","1","parClose","hyphen"],
            ["parOpen","2","opEqual","2","parClose","hyphen"],
            ["parOpen","3","opEqual","3","parClose","hyphen"],
            ["parOpen","4","opEqual","4","parClose","hyphen"],
            ["parOpen","5","opEqual","5","parClose","hyphen"],
            ["parOpen","6","opEqual","6","parClose","hyphen"],
            ["parOpen","7","opEqual","7","parClose","hyphen"],
            ["parOpen","8","opEqual","8","parClose","hyphen"],
            ["parOpen","9","opEqual","9","parClose","hyphen"],
            ["parOpen","0","opEqual","0","parClose","hyphen"],
            ["parOpen","squote","1","squote","opEqual","squote","1","squote","parClose","hyphen"],
            ["parOpen","squote","2","squote","opEqual","squote","2","squote","parClose","hyphen"],
            ["parOpen","squote","3","squote","opEqual","squote","3","squote","parClose","hyphen"],
            ["parOpen","squote","4","squote","opEqual","squote","4","squote","parClose","hyphen"],
            ["parOpen","squote","5","squote","opEqual","squote","5","squote","parClose","hyphen"],
            ["parOpen","squote","6","squote","opEqual","squote","6","squote","parClose","hyphen"],
            ["parOpen","squote","7","squote","opEqual","squote","7","squote","parClose","hyphen"],
            ["parOpen","squote","8","squote","opEqual","squote","8","squote","parClose","hyphen"],
            ["parOpen","squote","9","squote","opEqual","squote","9","squote","parClose","hyphen"],
            ["parOpen","squote","0","squote","opEqual","squote","0","squote","parClose","hyphen"],
            ["parOpen","squote","","squote","opEqual","squote","","squote","parClose","hyphen"],

        ],
        "parOpen":[
            ["("]
        ],
        "parClose":[
            [")"]
        ],
        "opEqual":[
            ["="]
        ],
        "hyphen":[
            ["--"]
        ],
        "squote":[
            ["'"]
        ]

    }
    def generate_items(items):
        for item in items:
            if isinstance(item, list):
                for subitem in generate_items(item):
                    yield subitem
            else:
                yield item

            # Our expansion algo
    def expansion(start):
        for element in start:
            if element in rules:
                loc = start.index(element)
                start[loc] = rd.choice(rules[element])
            result = [item for item in generate_items(start)]

        for item in result:
            if not isinstance(item, list):
                if item in rules:
                    result = expansion(result)

        return result


    def to_string(result):
        return ''.join(result)
    final=[]
    for i in range(0,500):
        result = ["booleanAttack"]
        result = expansion(result) # Expand our starting list
        final.append(to_string(result))
    print(*final, sep="\n")
    x=list(userid.split(" "))
    ml=list(userid.split(" "))
    ml.pop(0)
    sep=""
    mlsep=" "
    mlcheck=mlsep.join(ml)
    if(mlcheck==""):
        print("nothing")
    print(mlcheck)
    y=sep.join(x)
    print(y)
    if y in final:
        print('found attack pattern')
    else:
        print('attack pattern not found')# Print the final result


    conn1 = pypyodbc.connect('Driver={SQL Server};Server=DESKTOP-H8DJFBD\MSSQLSERVER01;Integrated_Security=true;Database=sqli', autocommit=True)

    cur1 = conn1.cursor()

    sqlcmd1 = "SELECT * FROM dbo.Users WHERE username = '"+userid+"' AND password = '"+password+"'";
    listsql=list(sqlcmd1.split(" "))
    checksql=sep.join(listsql)


    #SELECT * FROM dbo.Users WHERE username = 'rishi'-- AND password = 'ksdahfhkhfa'"
    print(sqlcmd1)
    print(checksql)

    # if sqlcmd1.find("'--") > 0:
    #
    #     print("SQl injection detected")
    #
    #     return render_template('index.html')

    cur1.execute(sqlcmd1)

    row = cur1.fetchone()



    if not row:

        return render_template('index.html')

    return render_template('dashboard.html')

if __name__ == "__main__":

    app.run()


from flask import Flask, jsonify, request

app = Flask(__name__)


pizzaDB = [ {"name": "tonno", "ingredienten": ['tomaat','kaas', 'tonijn', 'oliif']},
            {"name": "salami", "ingredienten": ['tomaat','kaas','salami']},
            {"name": "fungi", "ingredienten": ['tomaat','kaas','ham','ananas']}
          ]


@app.route("/", methods=['GET'])
def geefPizza():
    return jsonify({"pizzaDB":pizzaDB})

@app.route("/<string:name>", methods=['GET'])
def getOnePizza(name):
    resultPizza = []
    for pizzaSmaak in pizzaDB:
        if pizzaSmaak["name"] == name:
            return str(pizzaSmaak)

@app.route("/", methods=['POST'])
def addOnePizza():
    pizza = {'name': request.json['name']}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB': pizzaDB})


    #return jsonify({"pizzaDB":resultPizza})


if __name__ == "__main__":
    app.run(debug=True, port=8080)

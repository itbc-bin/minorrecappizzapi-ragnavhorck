from flask import Flask, jsonify, request

app = Flask(__name__)


pizzaDB = [ {"name": "tonno", "ingredienten": ['tomaat','kaas', 'tonijn', 'oliif'], "prijs": 5},
            {"name": "salami", "ingredienten": ['tomaat','kaas','salami'], "prijs": 6},
            {"name": "hawaii", "ingredienten": ['tomaat','kaas','ham','ananas'], "prijs": 20}
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

    pizzaNaam = request.json['name']
    ingredienten = request.json['ingredienten']

    for pizzaSmaak in pizzaDB:
        if pizzaSmaak['name'] == pizzaNaam:
            for pizzaSpul in ingredienten:
                if pizzaSpul not in pizzaSmaak["ingredienten"]:
                    pizzaSmaak.append(pizzaSpul)
                    return jsonify({'pizzaDB': pizzaDB})


    pizza = {'name': request.json['name'], 'ingredienten': ingredienten}
    pizzaDB.append(pizza)
    return jsonify({'pizzaDB': pizzaDB})


    #return jsonify({"pizzaDB":resultPizza})

@app.route("/prijs",methods=['POST'])
def addPricePizza():
    pizzaPrijs = request.json['prijs']
    pizzaNaam = request.json['name']

    for pizzaSmaak in pizzaDB:
        if pizzaSmaak['name']== pizzaNaam:
            if "prijs" in pizzaSmaak:
                pizzaSmaak['prijs'] = pizzaPrijs
                return jsonify({'pizzaDB': pizzaDB})

            else:
                pizzaSmaak['prijs'] = pizzaPrijs
                return jsonify({'pizzaDB': pizzaDB})

if __name__ == "__main__":
    app.run(debug=True, port=8080)

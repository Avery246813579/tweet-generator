# app.py (Flask server for CS2 Project)

import time
from flask import Flask, render_template
from stochastic_example import Stochastic
app = Flask(__name__)

@app.route("/")  # Flask routes to home route ("/")
def index():
    input_string = "it is a fair bet that if it is fair tomorrow then my fair haired wife and I will head to the spring fair which is held in a fair sized park in this fair city of ours and we may win a prize in a city wide game if we all play fair"
    user_cycles = 15

    output_first = "\nINPUT STRING: \"{}\"\n".format(input_string)
    output_second = "\nINPUT CYCLES: {}\n".format(user_cycles)

    # Create class instance of Stochastic() to randomly run methods
    s = Stochastic()
    output_sentence = s.word_frequency(input_string.split(" "), user_cycles)[0]
    output_freq = s.word_frequency(input_string.split(" "), user_cycles)[1]

    return render_template("index.html", output_first=output_first, output_second=output_second, output_sentence=output_sentence, output_freq=output_freq)

if __name__ == "__main__":
    # Refresh page and displays debug tips
    app.config["TRAP_BAD_REQUEST_ERRORS"]=True
    app.run(debug=True)

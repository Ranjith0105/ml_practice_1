from flask import Flask
import sys
from Housing.logger import logging
from Housing.exception import HousingException

app = Flask(__name__)

@app.route("/", methods =["GET","POST"])
def index():
    try:
        raise Exception("We are testing Custom Exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)


    #logging.info("We are testing logging")
    return "Starting Machine Learning Project Pipeline"

if __name__ == "__main__":
    app.run(debug=True)
    

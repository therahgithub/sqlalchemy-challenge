# Flask Import
from flask import Flask, jsonify
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save reference to the table
hawaii_weather = Base.classes.measurement

hawaii_station = Base.classes.station

# Flask Setup
app = Flask(__name__)

# Flask Routes

@app.route("/")
def Aloha():
    return (
        f"<b><u>Aloha and welcome to the Hawaii Weather API</u>!</b><br/>"
        f"<br/>"
        f"<b>Available Routes:</b><br/>"
        f"<br/>"
        f"1. Daily precipitation (12mo starting 2016-23-08) <b>-></b> /api/v1.0/precipitation<br/>"
        f"<br/>"
        f"2. Weather station list <b>-></b> /api/v1.0/stations<br/>"
        f"<br/>"
        f"3. Daily temperature for the most active station, USC00519281 (12mo starting 2016-23-08) <b>-></b> /api/v1.0/tobs<br/>"
        f"<br/>"
        f"4. Min, max, and avg temperature for 12mo from a specific date (replace YYYY-MM-DD with your date) <b>-></b> /api/v1.0/YYYY-MM-DD<start><br/>"
        f"<br/>"
        f"4. Avg, min, and max temperature for 12mo from a specific date (replace YYYY-MM-DD/YYYY-MM-DD with your date range) \
            <b>-></b> /api/v1.0/YYYY-MM-DD<start>/YYYY-MM-DD<end><br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    precipitation_results = session.query(hawaii_weather.date, hawaii_weather.prcp).filter(hawaii_weather.date > query_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    precipitation = []
    for date, prcp in precipitation_results:
        precipitation_dict = {}
        precipitation_dict["date"] = date
        precipitation_dict["precipitation"] = prcp
        precipitation.append(precipitation_dict)

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the station dataset
    stations_results = session.query(hawaii_station.name, hawaii_station.station, hawaii_station.elevation, hawaii_station.latitude, hawaii_station.longitude).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    stations = []
    for name, station, elevation, latitude, longitude in stations_results:
        station_dict = {}
        station_dict["name"] = name
        station_dict["station"] = station
        station_dict["elevation"] = elevation
        station_dict["latitude"] = latitude
        station_dict["longitude"] = longitude
        stations.append(station_dict)

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temps():
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Calculate the date one year from the last date in data set
    query_date = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the temp data
    temp_results = session.query(hawaii_weather.date, hawaii_weather.tobs).filter(hawaii_weather.station == 'USC00519281').\
        filter(hawaii_weather.date >= query_date).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    temperature = []
    for date, tobs in temp_results:
        temp_dict = {}
        temp_dict["date"] = date
        temp_dict["temperature"] = tobs
        temperature.append(temp_dict)

    return jsonify(temperature)

@app.route("/api/v1.0/<start>")
def start(start):

    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the temp data
    start_results = session.query(func.min(hawaii_weather.tobs), func.max(hawaii_weather.tobs), func.avg(hawaii_weather.tobs)).\
        filter(hawaii_weather.date >= start)

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    start_data = []
    for min, max, avg in start_results:
        start_dict = {}
        start_dict["min temperature"] = min
        start_dict["max temperature"] = max
        start_dict["avg temperature"] = avg
        start_data.append(start_dict)

    return jsonify(start_data)

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
    
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Perform a query to retrieve the temp data
    startend_results = session.query(func.min(hawaii_weather.tobs), func.max(hawaii_weather.tobs), func.avg(hawaii_weather.tobs)).\
        filter(hawaii_weather.date >= start).\
        filter(hawaii_weather.date <= end)

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    startend_data = []
    for min, max, avg in startend_results:
        startend_dict = {}
        startend_dict["min temperature"] = min
        startend_dict["max temperature"] = max
        startend_dict["avg temperature"] = avg
        startend_data.append(startend_dict)

    return jsonify(startend_data)

# Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
<img width="1000" alt="Screen Shot 2023-05-29 at 11 20 46 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/3c0fd2d0-e614-4413-bb1b-4b74e383bc8c">

# SQLAlchemy Challenge

## Hawaii Weather

Hypothetical Background: In preparation for a trip to Honolulu, I will conduct a climate analysis about the area.

## Analysis & Results

* __Precipitation Analysis__
  * Find the most recent date in the dataset.
  * Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data.
  * Select only the "date" and "prcp" values.
  * Load the query results into a Pandas DataFrame. Explicitly set the column names.
  * Sort the DataFrame values by "date".
  * Plot the results by using the DataFrame plot method.
  * Use Pandas to print the summary statistics for the precipitation data.

<img width="700" alt="Screen Shot 2023-05-29 at 11 29 29 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/d3f37cf1-6dc1-42fb-b78f-4138482551f4">

<img width="1067" alt="Screen Shot 2023-05-31 at 3 48 25 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/910af384-22fc-4ac2-a47e-75cb098fb8e4">

* __Station Analysis__
  * Design a query to calculate the total number of stations in the dataset.
  * Design a query to find the most-active stations.
  * List the stations and observation counts in descending order.
  * Which station id has the greatest number of observations? 

<img width="700" alt="Screen Shot 2023-05-29 at 11 35 09 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/2cf979d5-dc34-4d63-9142-8766455a8be2">

* __Climate App__

Design a Flask API based on the preceeding queries. To do so, use Flask to create the following routes:
  * `` / `` Start at the homepage and list all the available routes.

<img width="1392" alt="Screen Shot 2023-05-31 at 3 58 22 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/b2e921f6-51ae-447f-bff0-7fd7657ee446">

  * `` /api/v1.0/precipitation<br/> `` Convert the query results from the precipitation analysis to JSON and deply to the API.

<img width="1392" alt="Screen Shot 2023-05-31 at 3 58 39 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/de8cb59f-35b2-4dfd-9a2e-88ef9344906f">

  * `` /api/v1.0/stations<br/> `` Return a JSON of the stations dataset and deploy to the API.

<img width="1392" alt="Screen Shot 2023-05-31 at 3 58 55 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/21fb5638-2987-4129-986b-ca28846b422d">

  * `` /api/v1.0/tobs<br/> `` Convert the query results from the active station temperature analysis to JSON and deply to the API.

<img width="1392" alt="Screen Shot 2023-05-31 at 3 59 24 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/01217c8e-e88e-45d0-85aa-d7520eaddefa">

  * `` /api/v1.0/<start> `` and `` /api/v1.0/<start>/<end> `` Create variable queries to rerturn the minimum, maximum, and average temperature for a specified start or start-end range. Return a JSON of the stations dataset and deploy to the API.

<img width="1392" alt="Screen Shot 2023-05-31 at 4 00 07 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/c2636aaa-2d68-4882-bafe-5759500f6be0">

<img width="1392" alt="Screen Shot 2023-05-31 at 4 00 55 PM" src="https://github.com/therahgithub/sqlalchemy-challenge/assets/119986667/f03a3542-9c88-409d-95e9-67116addbd26">

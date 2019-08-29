# Workshop: Build your first Machine Learning model
This workshop will show you some basics of starting with `Machine Learning` with Python.<br>
Tech stack: Python, Scikit Learn, Pandas<br>

One reference for the structure and topics is chapter 2 of Hands-On Machine Learning with Scikit-Learn and TensorFlow - Aurélien Géron (2017, O’Reilly Media)

# Structure
## Data
-- Updated 2019-06-20 --
Data was downloaded  from https://data.deutschebahn.com/dataset/data-call-a-bike<br>
There are 3 source CSV files which contain:
* Stations
* Vehicles
* Bookings
*
Unfortunately data description and the website are only available in German language.<br>
You can find some English translations at the end in **[Data Description](#data-description)**

## Content
* Downloading Data and Creation of Dataframes
* Analysis and Visualization
* Data Cleansing
* Feature Engineering
* Training
* Prediction and Evaluation


# Appendix
## Data Description
http://download-data.deutschebahn.com/static/datasets/callabike/20170516/Dokumentation%20Daten%20Hackathon_190719.pdf
### hackathon_vehicle
| Fieldname       | Description                                          | Instance |
|-----------------|------------------------------------------------------|----------|
| vehicle_hal_id  | key vehicle                                          | xxx      |
| vehicle_hal_src | addition to vehicle_hal_id to generate an unique key | yyy      |
|                 |                                                      |          |

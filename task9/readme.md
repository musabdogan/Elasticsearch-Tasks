# Real-time Coronavirus Worldmap Project with Elasticstack

## Purpose of project: 
Purpose of this project is to monitor the daily number of cases, deaths, and recoveries for each countries related to the coronavirus.

_- Note: Since the majority of countries have now stopped reporting the data source is no longer being updated. Data source had switched from LIVE to Daily Update.
This Project was made 3 years ago._


## Which tools will use:
- Python, Beautiful package (to scrap the data from the website)
- Logstash (to send the data to Elasticsearch)
- Kibana (to monitor the sent data.)
- Bash script (to automatize python code which retrieves the data from source)

## Task
- We provided you with the Python code you needed. If there are any uncertainties about your expectations, please review the architecture in the link below.
- Pull the data from [https://www.worldometers.info/coronavirus/](url)
- Visualize the data using Kibana and create dashboards consist of 3 pages.
An example of project is avaliable [here](https://www.youtube.com/watch?v=8lqhow7WR28):

## Project steps:
In order to help you during the project, I have added the steps.

1. Analyze the website, columns and lines. Compare with python codes. It helps you to understand the logic of the code and project. 

2. Install Elasticsearch, Kibana and Logstash.

3. Install Python and Beautiful package and paste the code has given. You must analyze full of the code. Because it helps you understand what Elasticsearch wants to us. (It's better than write the code :))

4. Run the code, output will be exist on a .csv file. Take a look at the file, Everything must be clear.

5. To retrieve the data from .csv file, we have to create a pipeline. Creating pipeline may confusable sometimes. [This video](https://www.youtube.com/watch?v=FPLHS9Pmgk0) describes the Logstash's pipeline architecture. The .conf that you will create must contains three part. 
      - Input (where the data comes from) 
      - Filters (you are going to sculpt the data that comes from .csv file in order to be indexable to Elasticsearch.)
      - Output (where the data goes to)

6. Create a mapings compatible with pipeline file. **Even the smallest mistake here will reflect when you work with Kibana**. You have to ensure everything is clear.

7. Run the command that activate the pipeline.

8. Check the flow, ensure everything is clear in Elasticsearch side.

9. Create the dashboards as requested.

10. Create user for the delivery. Give the read permission only.









**All of the steps explained a [Medium blog](https://medium.com/@tumersevban/real-time-coronavirus-map-with-elasticsearch-7902adb0d973).**

~~Also the cheatsheets avaliable a [github repo](https://github.com/tumersevban/Elasticsearch-Coronavirus-map).~~

# PostgreSQL-Elasticsearch Sync

## Purpose of Task:
Purpose of project is create synchronization between Elasticsearch and PostgreSQL. Data in PostgreSQl will sent Elasticsearch.

*_Note: Please know that It is not real time sync. Any chnage in postgresql, Logstash must run again._*

## Which tool will use:
* Docker (You will create database via Docker)
* Logstash (Create a pipeline using Logstash)
* PostgreSQL (Our data is here)
* Elasticsearch (You should know :)
* a pc with keyboard
  
*Noteagain: I used Ubuntu during the task.*

## Task 
* Create a database and put a data in it. Pull the data from database. Check whether data pulled.

## Steps:
In order to help you during the project, I have added the steps.

#### 1. Install necessary environment.

[Docker](https://docs.docker.com/engine/install/), [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) and  [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html) must be installed.

#### 2. Create database in Docker

[This link](https://dev.to/andre347/how-to-easily-create-a-postgres-database-in-docker-4moj) helps you during the step. 

#### 3. Create ETL pipeline.

We will create a pipeline. We handled a example of it at #task9.  [This video](https://www.youtube.com/watch?v=FPLHS9Pmgk0) describes the Logstash's pipeline architecture. The .conf that you will create must contains three part. 
      - Input (where the data comes from) 
      - Filters (you are going to sculpt the data if needed)
      - Output (where the data goes to)

#### 4. Run it.

#### 5. Check the Elasticsearch side.

Check whether data succesfully indexed by writing some query. 

















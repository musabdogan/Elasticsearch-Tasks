# Task 13 | PostgreSQL-Elasticsearch Sync

## About Task:
Purpose of project is create synchronization between Elasticsearch and PostgreSQL. Data in PostgreSQl will sent Elasticsearch.

*_Note: Please know that It is not real time sync. Any chnage in postgresql, Logstash must run again._*

## Which tool will use:
* Docker (You will create database via Docker)
* Logstash (Create a pipeline using Logstash)
* PostgreSQL (Our data will be here)
* Elasticsearch 
* a pc with keyboard
  
*Noteagain: I used Ubuntu during the task.*

## Task 
* Create a database and put a data in it. Pull the data from database. Check whether data pulled.

  ![Flowcharts (1)](https://github.com/user-attachments/assets/e872b639-9e09-4939-a8a3-93b12f8424b3)


## Steps:
In order to help you during the project, I have added the steps.

#### 1. Install necessary environment.

[Docker](https://docs.docker.com/engine/install/), [Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html) and  [Logstash](https://www.elastic.co/guide/en/logstash/current/installing-logstash.html) must be installed.

#### 2. Create database in Docker

[This link](https://dev.to/andre347/how-to-easily-create-a-postgres-database-in-docker-4moj) helps you during the step. 

#### 3. Install JDBC driver for PostgreSQl
You need to install jdbc driver from [here. ](https://jdbc.postgresql.org/download/) 
 After installation, copy the downloaded .jar file to the logstash configuration directory. For example, you might copy it to /usr/share/logstash/logstash-core/lib/jars on the machine where Logstash is running.


#### 4. Create ETL pipeline.
We handled a example of it at #task9.  [This video](https://www.youtube.com/watch?v=FPLHS9Pmgk0) describes the Logstash's pipeline architecture.

Create a .conf file and add JDBC input plugin. Check the [documentation.](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-jdbc.html)
~~a copy of .conf file was attached~~

#### 5. Run it.

#### 6. Check the Elasticsearch side.

Check whether data succesfully indexed by writing some query. 

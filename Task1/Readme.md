# Elasticsearch Task 1 

## Area to Work:

- Install Elasticsearch, Kibana, and Elastic Agent on Linux.

## Task:

- You will be provided with Nginx Access and Error Logs, extract and parse the logs based on their file types, and index the Nginx logs into Elasticsearch through the Elastic Agent Integration. If there are any uncertainties about your expectations, please review the architecture in the link below.

#### Link: https://docs.elastic.co/integrations/nginx

- Display Nginx logs in Kibana with out-of-box Dashboards.

![nginxelasticagent](https://github.com/SeyyidhanTaskin/Collecting-Logs-with-Elastic-Agent/assets/109666785/9c9403d4-88ee-45c2-b6d4-d04f65e68b95)

## Delivery:

- Create a role and assign a user to this role. Create two users with different autherization. One user can only read access.logs another user can only read error.logs
  
- Were you able to obtain the requested visuals?
  
- Create out-of-box dashboards and observe the data.

- Compare document count in both Elasticsearch index/datastream and the log files. Make sure both access.log and access-log index has same number of documents.

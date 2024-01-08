# Elasticsearch Task 1 

## Area to Work:

- Install Elasticsearch, Kibana, and Elastic Agent on Linux.

## Task:

- You will be provided with Nginx Access and Error Logs, extract and parse the logs based on their file types, and index the Nginx logs into Elasticsearch through the Elastic Agent Integration. If there are any uncertainties about your expectations, please review the architecture in the link below.

#### Link: https://docs.elastic.co/integrations/nginx

- Display Nginx logs in Kibana with out-of-box Dashboards.

![nginxelasticagent](https://github.com/SeyyidhanTaskin/Collecting-Logs-with-Elastic-Agent/assets/109666785/9c9403d4-88ee-45c2-b6d4-d04f65e68b95)

## Delivery:
- Working Elasticsearch, Kibana, Integration Server, Elastic Agent on Linux that can consume the access.log and error.log continuously.

- Provide a Kibana Dashboard like the above.

- Verify that the document count in both the Elasticsearch index/datastream and the corresponding log files is consistent. In other words, ensure that both the access.log and access-log index have the same number of documents.

- Two users with different permissions: one can only read access logs, and the other can only read error logs.

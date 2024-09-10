# Task 1 | Nginx Log Monitroing

## Area to Work:

- Install Elasticsearch, Kibana, and Elastic Agent on Linux.
- Visualize the NGINX [access.logs](https://github.com/musabdogan/Elasticsearch-Tasks/blob/main/task1/access.log) and [error.logs](https://github.com/musabdogan/Elasticsearch-Tasks/blob/main/task1/error.log)

## Task:

- You will be provided with Nginx Access and Error Logs, extract and parse the logs based on their file types, and index the Nginx logs into Elasticsearch through the Elastic Agent Integration. If there are any uncertainties about your expectations, please review the architecture in the link below.

#### Link: https://docs.elastic.co/integrations/nginx

- Display Nginx logs in Kibana with out-of-box Dashboards.

![nginxelasticagent](https://github.com/musabdogan/Elasticsearch-Tasks/blob/main/task1/nginx-logs-dashboard.png)

## Delivery:
- Working Elasticsearch, Kibana, Integration Server, Elastic Agent on Linux that can consume the access.log and error.log continuously.

- Provide a Kibana Dashboard like the above.

- Verify that the document count in both the Elasticsearch index/datastream and the corresponding log files is consistent. In other words, ensure that both the access.log and access-log index have the same number of documents.

- Two users with different permissions: one can only read access logs, and the other can only read error logs.

# High Availability
https://www.elastic.co/guide/en/elasticsearch/reference/current/high-availability.html
https://opster.com/guides/elasticsearch/high-availability/elasticsearch-high-availability/

High Availability (HA) is crucial. Explain the HA and explain what is needed, how we make sure HA. 
* How it's possible to make sure HA on-prem clusters
* How can I make sure HA on cloud environment

Main aim: Elasticsearch 30 data + 3 master + 3 coordinator nodes. 10 physical server, 2 rack cabinet.
1. Design an architecture where elasticsearch can run even if a random physical server shut down.
2. Design an architecture where elasticsearch can run even if the entire rack cabinet goes down.

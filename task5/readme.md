# Task 5 | Coping with growing data

## About Task:
Dealing with growing data is the crucial things for cluster. When data contionusly coming from a source, we need to manage it. **Index lifecycle** should managed efficiently to avoid oversized indices, performance degradation or storage issues.

### Pre-informative Sources
- [Elastic Rollover Guide](https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-rollover-index.html)  
- [Elastic Data Streams](https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html)

---

## Step 1:
Install Elasticsearch through Docker and ensure the following endpoints are accessible:

- `http://localhost:9200` → Elasticsearch
- `http://localhost:5601` → Kibana

Check that everything is working correctly.

---
## Step 2:
ILM policy is can created through Stack management section or Dev console.
Create a new ILM policy that satisfies the following requirements:

| Phase  | Duration / min_age | Action |
|--------|-----------------|--------|
| Hot    | 2 minutes       | Rollover to new index after max_age |
| Warm   | 1 minute        | Make index read-only |
| Cold   | 2 minutes        | Set number of replicas to 0 |
| Delete | 3 minutes        | Delete the index |

* The name of the policy is my_ilm_policy
* The index is in the hot phase for 2 minutes.
* The index moves to the warm phase and makes the index read-only when it rolls over. and stays in warm for 1 minute.
* The index moves to the cold phase and the number of replicas is set to 0 after 2 minutes in the warm phase.
* The index is deleted 3 minutes after rolling over.
## Step 3:
Use the Console to create a new Index Template with the following requirements:
* The name is my-ds-template
* The priority is set to 500
* It applies the new ILM policy
* The number of replicas is set to 0
* Should matches anything begin with "logs-"
## Step 4
Use a Python script or any application to send logs frequently. For demonstration purposes, send a log every 10 seconds.

## Step 5:
* Observe the index rollover according to the ILM policy and hot-warm-delete data tiers


`GET logs-data/_ilm/explain `







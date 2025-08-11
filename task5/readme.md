# Task 5 | Coping with growing data

## About Task:
Dealing with growing data is the crucial things for cluster. When data contionusly coming from a source, we need to manage it. **Index lifecycle** should managed efficiently to avoid oversized indices, performance degradation or storage issues.
https://www.elastic.co/guide/en/elasticsearch/reference/current/indices-rollover-index.html
https://www.elastic.co/guide/en/elasticsearch/reference/current/data-streams.html

## Step 1:
Install Elasticsearch through Docker.

Check everything is completed correct. localhost:9200 & localhost:5601

## Step 2:
ILM policy is can created through Stack management section or Dev console.
Create a new ILM policy that satisfies the following requirements:
* The name of the policy is my_ilm_policy
* The index is in the hot phase for 2 minutes.
* The index immediately moves to the warm phase and makes the index read-only when it rolls over.
* The index moves to the cold phase and the number of replicas is set to 0 after 2 minutes in the warm phase.
* The index is deleted 5 minutes after rolling over.
## Step 3:
Use the Console to create a new Index Template with the following requirements:
* The name is my-ds-template
* The priority is set to 500
* It applies the new ILM policy
* The number of replicas is set to 0
* Should matches anything begin with "logs-"

## Step 4

  
## Step 5:
push data frequently with a python code or any application
## Step 6:
* observe the index rollover according to the ILM policy

## Step 7:


* observe hot-warm-delete data tiers





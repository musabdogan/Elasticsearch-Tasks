# Elasticsearch Task 2

## Area to Work:

- Enrich the data in [enrich_me.txt](https://github.com/musabdogan/Elasticsearch-Tasks/blob/main/Task1/access.log) with [lookup_table.csv](https://github.com/musabdogan/Elasticsearch-Tasks/blob/main/task2/lookup_table.csv) and index the enriched data into target_index.

## Task:

- You will be provided with source index data and enrichment data, use the Elasticsearch enrichment and ingest pipeline features to enrich your data. Source index will be a lookup table and whenever you index the data in enrich_me.txt you should see enriched data in target_index. If there are any uncertainties about your expectations, please review the architecture in the link below.

#### Link: https://www.elastic.co/blog/how-to-enrich-logs-and-metrics-using-an-elasticsearch-ingest-node

![enrich_process](https://github.com/musabdogan/Elasticsearch-Tasks/blob/main/task2/enrich-process.svg)

## Delivery:
- Working Elasticsearch, Kibana that can enrich the data in lookup_table.csv with enrich_me.txt and index the enriched data into target_index continuously.

- Provide a Kibana Discover for target_index.

- Verify that all document that can enrich are enriched with the data in lookup table.

- Check the enrichment index *enrich*, make sure the index is exist and it updating from time to time.

- Update the lookup_table and add new line, the new line available to enrich in at max 10 minutes by default. Test it and make sure it's working fine.

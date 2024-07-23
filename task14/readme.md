# Elasticsearch cross cluster search

https://www.elastic.co/guide/en/elasticsearch/reference/current/xpack-ccr.html

To do:
1. enable the CCR
2. disable the CCR
3. Create a scheme to send the search request to only follower cluster, and indexing request to only leader cluster


create two different cluster
docker-compose.yml
```
version: '2.2'
services:
  c1n1:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.2
    container_name: c1n1
    environment:
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - bootstrap.memory_lock=true
      - cluster.name=c1
      - node.name=c1n1
      - discovery.seed_hosts=c1n1
      - cluster.initial_master_nodes=c1n1
      - path.repo=/usr/share/elasticsearch/repo
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - ccs_c1n1:/usr/share/elasticsearch/data
      - ccs_c1n1:/usr/share/elasticsearch/repo
    ports:
      - 9200:9200
      - 9300:9300
    networks:
      - esnet
  c2n1:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.2
    container_name: c2n1
    environment:
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
      - bootstrap.memory_lock=true
      - cluster.name=c2
      - node.name=c2n1
      - discovery.seed_hosts=c2n1
      - cluster.initial_master_nodes=c2n1
      - path.repo=/usr/share/elasticsearch/repo
    ulimits:
      memlock:
        soft: -1
        hard: -1
    volumes:
      - ccs_c2n1:/usr/share/elasticsearch/data
      - ccs_c2n1:/usr/share/elasticsearch/repo
    ports:
      - 9201:9200
      - 9300:9300
    networks:
      - esnet
  c1k1:
    image: docker.elastic.co/kibana/kibana:7.17.2
    container_name: c1k1
    environment:
      ELASTICSEARCH_HOSTS: http://c1n1:9200
    ports:
      - 5601:5601
    networks:
      - esnet
  c2k1:
    image: docker.elastic.co/kibana/kibana:7.17.2
    container_name: c2k1
    environment:
      ELASTICSEARCH_HOSTS: http://c2n1:9200
    ports:
      - 5602:5601
    networks:
      - esnet

volumes:
  ccs_c1n1:
    driver: local
  ccs_c2n1:
    driver: local

networks:
  esnet:
    driver: bridge
    driver_opts:
      com.docker.network.enable_ipv6: "false"
```

#PUSH dummy data
while true; do
  curl -s -XPOST "http://localhost:9200/_reindex?refresh" -H 'Content-Type: application/json' -d' {"source":{"index":"kibana_sample_data_ecommerce"},"dest":{"index":"test_index"},"script":{"source":"ctx.remove('\''_id'\'')"}}' | grep -q '\"failures\":\[\]' && echo "#### reindex completed ####";
  echo "source cluster"; curl -s -XPOST "http://localhost:9200/test_index/_count?pretty" | grep "count";
  sleep 1;
  echo "destination cluster"; curl -s -XPOST "http://localhost:9201/test_index/_count?pretty" | grep "count";
done

#### reindex completed ####
source cluster
  "count" : 472175,
destination cluster
  "count" : 472175,


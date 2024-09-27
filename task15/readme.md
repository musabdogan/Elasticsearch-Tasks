# APM Server

![image](https://github.com/user-attachments/assets/30ed7bd8-e9bb-4af2-a383-40ca2248244c)


* the application http://localhost:3000/
* apm-server http://localhost:8200/
* elasticsearch https://localhost:9200/
* kibana http://localhost:5601/

# Steps:
1. install self-managed APM server https://www.elastic.co/guide/en/observability/current/apm-installing.html
2. Configure the apm-server.yml and run the APM server. This server will listen the agents on port 8200 and send the APM data to elasticsearch. `./apm-server -e`
3. Add the requeired information to track the application and run the application.js.
4. run the application `node application.js`

# Test:
`for i in {1..1000}; do echo "Sending request $i..." ;sleep 1; curl -s http://localhost:3000/; echo ""; done`

# Delivery:
An APM server

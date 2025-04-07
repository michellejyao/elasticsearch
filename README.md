# CLNC-141 - Setup Elasticsearch for logging
# Step 1:
The commands I ran were:
1. curl -fsSL https://elastic.co/start-local | sh
2. python -m pip install ecs-logging

To start the Elasticsearch and Kibana Docker services run: ./start.sh
To stop the Elasticsearch and Kibana Docker services: ./stop.sh

Learn more about the set up here: https://github.com/elastic/start-local 

![Step 2!](elastic-start-local\step2.png)
![Step 3!](elastic-start-local\step3.png)

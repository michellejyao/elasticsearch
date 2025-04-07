# CLNC-141 - Setup Elasticsearch for logging
Step 1:
The commands I ran were:
1. curl -fsSL https://elastic.co/start-local | sh
2. python -m pip install ecs-logging

Elastic home page where you can view the data: http://localhost:5601.
- Username: elastic
- Password: UzhwWhoJ

Elasticsearch API endpoint: http://localhost:9200

To start the Elasticsearch and Kibana Docker services run: ./start.sh
To stop the Elasticsearch and Kibana Docker services: ./stop.sh

Learn more about the set up here: https://github.com/elastic/start-local 

Step 2:
Creates a new handler to log to elasticsearch using the ECS logging formatter. This handler prints to the console. Screenshot showing this is here: https://drive.google.com/file/d/1BaVybklOz0YnmELHGVjdn5AJepVGwiRB/view?usp=sharing

Step 3:
Implemented the handler in step 2 to send logs into the local instance and verify that logs are indeed ingested by the local instance. Set up the connection with the local instance within logger.py. Screenshot showing this: https://drive.google.com/file/d/1SckAWziqpgXsj4juhO3Dwq7U2E7V3MOI/view?usp=sharing 

Step 4: Already set up using Docker

import logging
import ecs_logging
import requests
import json

# ECS Console Logger 
logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)

# Console Handler with ECS formatting
console_handler = logging.StreamHandler()
console_handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(console_handler)

# Elasticsearch Handler
class ElasticsearchHandler(logging.Handler):
    def __init__(self, es_host='http://localhost:9200', index_name='ecs-logs', username='elastic', password='UzhwWhoJ'):
        super().__init__()
        self.es_host = es_host
        self.index_name = index_name
        self.auth = (username, password)

    def emit(self, record):
        try:
            log_entry = ecs_logging.StdlibFormatter().format(record)
            log_entry_json = json.loads(log_entry)

            url = f"{self.es_host}/{self.index_name}/_doc"
            response = requests.post(
                url,
                headers={"Content-Type": "application/json"},
                json=log_entry_json,
                auth=self.auth
            )

            if response.status_code >= 400:
                print(f"Failed to send log to Elasticsearch: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Exception in ElasticsearchHandler: {e}")

# Add Elasticsearch handler
es_handler = ElasticsearchHandler()
logger.addHandler(es_handler)

# Emit a test log 
logger.debug("HELLLLLO message!", extra={"http.request.method": "get"})

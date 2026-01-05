import functions_framework
from google.cloud import pubsub_v1
import json
import os
import logging

logging.basicConfig(level=logging.INFO)

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT")
TOPIC_ID = "order-events"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

@functions_framework.http
def create_order(request):
    if request.method == "GET":
        return {
            "message": "Order API is running. Use POST with JSON body."
        }

    request_json = request.get_json(silent=True)
    if not request_json:
        return ("Invalid request body", 400)

    logging.info(f"Order received: {request_json}")

    message = json.dumps(request_json).encode("utf-8")
    publisher.publish(topic_path, message)

    return {
        "status": "ORDER_CREATED",
        "order": request_json
    }

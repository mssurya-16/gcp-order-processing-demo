# GCP Order Processing System (Cloud-Native)

## Overview
This project demonstrates a cloud-native, event-driven order ingestion system built on Google Cloud Platform.  
It is designed to showcase scalable, reliable, and cost-efficient architecture patterns commonly used in
modern e-commerce platforms.

The system exposes a stateless HTTP API to receive orders and publishes order events asynchronously
to Pub/Sub for downstream processing.

---

## Architecture
Client  
→ Cloud Run (Order API – Stateless)  
→ Pub/Sub (order-events topic)  

![Architecture](architecture.png)

### Key Characteristics
- Stateless API
- Asynchronous event-driven design
- Auto-scaling serverless compute
- Production-grade logging and observability

---

## GCP Services Used

| Requirement | GCP Service | Reason |
|------------|------------|--------|
| Stateless API | Cloud Run | Fully managed, auto-scaling, request-based billing |
| Event Messaging | Pub/Sub | Decouples producers and consumers, reliable delivery |
| Observability | Cloud Logging | Request tracing and business-level logs |
| Security | IAM Service Accounts | Least-privilege access control |

---

## Order Flow
1. Client sends an HTTP POST request with order details
2. Cloud Run service validates the request
3. Order event is published to Pub/Sub
4. Logs are generated for traceability and monitoring

---

## Sample Request

curl -X POST https://<cloud-run-url> \
  -H "Content-Type: application/json" \
  -d '{"orderId":"1001","amount":4999,"currency":"INR"}'
  
## Sample Response

{
  "status": "ORDER_CREATED",
  "order": {
    "orderId": "1001",
    "amount": 4999,
    "currency": "INR"
  }
}


## Observability & Reliability

Structured logging added for each order event

Cloud Run request logs used for traffic visibility

Logs can be converted into log-based metrics

Alerting can be configured to detect missing order events

## Security

Cloud Run service uses a dedicated service account

Only Pub/Sub Publisher role is granted

No hardcoded credentials

## Cost Considerations

Designed to operate within GCP free tier

Request-based billing ensures zero cost when idle

No always-on infrastructure

## Future Enhancements

Add order consumer service

Persist orders to Cloud SQL

Introduce DLQ and retry policies

Secure API with authentication and Cloud Armor


## Author

Surya S

Google Professional Cloud Architect



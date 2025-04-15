# Receipt Processor

## Run Locally

```bash
pip install -r requirements.txt
python app.py
```

## Run with Docker

```bash
docker build -t receipt-processor .
docker run -p 5000:5000 receipt-processor
```

## Endpoints

### POST /receipts/process

```bash
curl -X POST http://localhost:5000/receipts/process \
  -H "Content-Type: application/json" \
  -d @example-receipt.json
```

### GET /receipts/{id}/points

```bash
curl http://localhost:5000/receipts/<id>/points
```
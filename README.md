# RequestsWS
The Requests like WS module

# Usage
```python
import requestsWS

payload = {
    "Im a": "payload!"
}
resp = requestsWS.post("ws://localhost:8765", json=payload).text
print(resp)

payload = "Im a string!"
resp = requestsWS.post("ws://localhost:8765", data=payload).json()
print(resp)
```

# Documentation
Comming soon!

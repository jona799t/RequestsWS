# RequestsWS
The Requests like WS module

# Installation
```
pip install requestsWS
```

# Usage
Sessions is not documented yet, but it works like requests
```python
import requestsWS

payload = {
    "message": "hello world!"
}
resp = requestsWS.post("wss://localhost:8765", identifiers={"message": "Hi there!"}, json=payload)
print(resp.text)

payload = {
    "method": "server.ping"
}
requestsWS.keepConnection('ws://localhost:8765', interval=20, json=payload)

payload = "hello world"
resp = requestsWS.post("ws://localhost:8765", data=payload)
print(resp.json())
```

# TO DO
   - Multiple connections at once (Use array instead of string)
   - Sessions  
   - Add headers for opening connections  
   - Add support for identifiers that are deeper into the json  
<<<<<<< HEAD
   - Add string support for identifier (Check if identifier in string)
=======
   - Add string support for identifier (Check if identifier in string)  
   - Fix timeout  
>>>>>>> 23529901e18236d432c2b1f80288abbdf808b368

# Documentation
Coming soon!

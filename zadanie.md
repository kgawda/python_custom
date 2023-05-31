
# Zdanie

Napisać aplikację wystawiającą REST API.
Ma ona korzystać z innej aplikacji, która też wystawia API (call server).

## Odpowiedzi

Wasza aplikacja ma odpowiadać na zapytania:

1. GET /status 
  Return json: `{'status': "OK"}`

2. GET /call_server_status/<data_name>
  Return json containing this data from <call_server>/status

   Eg. if <call_server>/status returns `{"status": "Starting", "uptime": 0, "F": 1}`
   <data_name> is "status", return `{"status": "Starting"}`

3. GET /calls_summary
  Return json: `{"count": <number of calls, int>}`
  Based on <call_server>/calls


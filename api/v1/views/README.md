# 0x05. AirBnB clone - RESTful API

3. Status of your API
Create a folder views inside v1:
  . create a file __init__.py:
	. import Blueprint from flask doc
	. create a variable app_views which is an instance of Blueprint (url prefix must be /api/v1)
	. wildcard import of everything in the package api.v1.views.index => PEP8 will complain about it, don’t worry, it’s normal and this file (v1/views/__init__.py) won’t be check.
  . create a file index.py
	. import app_views from api.v1.views
	. create a route /status on the object app_views that returns a JSON: "status": "OK" (see example)

```
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET http://0.0.0.0:5000/api/v1/status
{
  "status": "OK"
}
guillaume@ubuntu:~/AirBnB_v3$
guillaume@ubuntu:~/AirBnB_v3$ curl -X GET -s http://0.0.0.0:5000/api/v1/status -vvv 2>&1 | grep Content-Type
< Content-Type: application/json
guillaume@ubuntu:~/AirBnB_v3$
```

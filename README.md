# caching hash retrieval server
* This application will server as a DNS for content based caching Network
* Allows addition and reading of queries

# Setup
* run setup.py
```bash
sudo bash setup.sh
```
* https://www.youtube.com/watch?v=kDRRtPO0YPA


## To Run content hash Server
```bash
gunicorn server:app
```

## To Run web server
```bash
cd webserver
gunicorn web:app

```

# Usage
* add a new node | format -> add/location_id,content_id,url
```bash
curl http://127.0.0.1:5000/add/2,333,google.com
```
* read content_id | format -> read/hash/location_id
```bash
curl http://127.0.0.1:5000/read/hash/2
```
* read url | format -> read/url/content_id
```bash
curl http://127.0.0.1:5000/read/url/333
```


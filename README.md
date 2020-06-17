# caching hash retrieval server
* to run server
```bash
gunicorn server:app
```

# How To
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

# Setup
* https://www.youtube.com/watch?v=kDRRtPO0YPA
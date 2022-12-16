# flap
This is a web server powered by Flask and its extensions

### Apis

#### GET /api/articles
desc: get the article list
method: GET
params: None
response:
[success]
```json
{
    "code": 0,
    "msg": "get article list success",
    "msgCN": "获取文章列表成功",
    "data": {
        "lists": []
    }
}
```
[failed]
```json
{
    "code": 9001,
    "msg": "get article list failed",
    "msgCN": ""
}
```

#### GET /api/article?id=XXX&title=XXX

#### POST /api/article

#### DELETE /api/article

#### PUT /api/article?id=XXX
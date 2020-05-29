## RESTful API 设计
`用户资源`将暂时提供一下几个 API：

| HTTP 方法 | 资源 URL        | 说明              |
| --------- |:---------------:| ----------------:|
| GET       | /api/users      | 返回所有用户的集合 |
| POST      | /api/users      | 注册一个新用户 |
| GET       | /api/users/<id> | 返回一个用户 |
| PUT       | /api/users/<id> | 修改一个用户 |
| DELETE    | /api/users/<id> | 删除一个用户 |

# Project name: FastAPI User Management API
**Project Description** : Create a RESTful API using FastAPI and SQLAlchemy to manage a simple database of users.

### Tasks:
1. Setup a new Python project with FastAPI and SQLAlchemy.
2. Define a User model with fields for `id`, `name`, `email`, and `password`. Create the corresponding SQLAlchemy table.
3. Implement CRUD operations for managing users:
    - Create a new user.
    - Retrieve a user by ID.
    - Update a user's information.
    - Delete a user.
4. Create a FastAPI router to handle the API endpoints for user management.
5. Implement input validation for user input and handle errors gracefully with appropriate status codes and error messages.
6. Start the FastAPI application and test the endpoints using tools like `curl` or `Postman`.

***

# Project name: FastAPI 使⽤者管理 API
**Project Description** : 使⽤ FastAPI 和 SQLAlchemy 創建⼀個簡單的使⽤者資料庫管理 RESTful API。

### 任務:
1. 設置⼀個新的 Python 專案，包含 FastAPI 和 SQLAlchemy。
2. 定義⼀個使⽤者模型，包括 `id` 、`name` 、`email` 和 `password` 欄位。建立對應的 SQLAlchemy 表格。
3. 實現⽤於管理使⽤者的 CRUD 操作:
    - 創建新使⽤者。
    - 透過 ID 檢索使⽤者。
    - 更新使⽤者資訊。
    - 刪除使⽤者。
4. 創建⼀個 FastAPI 路由器來處理使⽤者管理的 API 端點。
5. 為使⽤者輸入實施輸入驗證，並使⽤適當的狀態碼和錯誤訊息優雅地處理錯誤。
6. 啟動 FastAPI 應⽤程式，並使⽤ `curl` 或 `Postman` 等⼯具測試端點。

# Demo
Technical : Deploy the application on AWS EC2 using Nginx.

- Fast API Website:  `http://13.238.194.179`
- Fast API Document: `http://13.238.194.179/redoc`

***
# API Document
## Get All User
Statement : Get all user list from database

`$ curl -X GET http://13.238.194.179/usermanagement`

```
- 200 Successful Response
```

## Create User
Statement : Create one user

`$ curl.exe -X POST -H "Content-Type: application/json" -d '{"name": "Bill Gates", "email": "john@example.com", "password": "passwordA1"}' http://13.238.194.179/usermanagement`

- name: required
- email: required
- password: required

### Rules to add a new data
1. Name must contain a space
2. Password length should be at least 8 characters
3. Password should contain at least one digit
4. Password should contain at least one uppercase letter
5. Password should contain at least one lowercase letter
6. Email should follow Email format

```json
{
  "email": "helloworld@gmail.com",
  "name": "Bill Gates",
  "password": "Th1sA3eCREtP3D#"
}
```

```
- 201 Successful Response
- 422 Validation Error
```

## Get user by id
Statement : Get one user 

`$ curl http://13.238.194.179/usermanagement/{usermanagement_id}`

```
- 200 Successful Response
- 422 Validation Error
```

## Update user
Statement : Update *name*, *email*, *password*, by userid. 

- name: required
- email: required
- password: required

`$ curl -X PATCH -H "Content-Type: application/json" -d '{"name": "Bill Gates", "email": "helloworld@gmail.com", "password": "Th1sA3eCREtP3D#"}' http://13.238.194.179/usermanagement/{usermanagement_id}`

```json
{
  "email": "helloworld@gmail.com",
  "name": "Bill Gates",
  "password": "Th1sA3eCREtP3D#"
}
```
```
- 200 Successful Response
- 422 Validation Error
```

## Delete user
Statement : Delete specific user by id. Replace **usermanagement_id** to the real usermangement_id

`$ curl -X DELETE http://13.238.194.179/usermanagement/{usermanagement_id}`

```
- 204 Successful Response
- 422 Validation Error
```

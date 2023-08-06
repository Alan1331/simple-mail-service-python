# User Sevice API Documentation
This API is intended to be datasource for user data. Therefore, there are no authentication and authorization required to use this API. It provides CRUD operation for user data.
## API Reference

### Create new user

```http
  POST /api/users
```

JSON required on request body

Parameter location: JSON request body

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `mail_address` | `string` | **Required**. The user mail address to be created |
| `password` | `string` | **Required**. The user password to be created |

Response example:
- On successful (201):
```json
{
    "message": "User account was successfully stored"
}
```
- On database error (500):
```json
{
    "message": "Failed to store user data due to database error"
}
```


### Get user

```http
  GET /api/users/${mail_address}
```

Parameter location: Resource ID

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `mail_address`      | `string` | **Required**. Mail address of user to fetch |

Response example:
- On user found (200):
```json
{
    "message": "Requested user was successfully received",
    "result": {
        "_id": "64cfc2c4665f09e4c8a1e483",
        "mail_address": "sahlan.royale@gmail.com",
        "password": "P@ssw0rd1"
    }
}
```
- On user not found (404):
```json
{
    "message": "The user is not found"
}
```

### Delete user

```http
  DELETE /api/users/${mail_address}
```

Parameter location: Resource ID

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `mail_address`      | `string` | **Required**. Mail address of user to be deleted |

Response example:
- On successful (200):
```json
{
    "message": "The user with given mail_address was deleted"
}
```
- On user not found (404):
```json
{
    "message": "The user with given mail_address is not found"
}
```
- On database error (500):
```json
{
    "message": "The delete operation could not be performed due to database error"
}
```
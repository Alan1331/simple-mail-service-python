# Core API Documentation
This API is intended to be endpoint for simple-mail-app. Therefore, there will be authorization to access some endpoints. It provides CRUD operation and business logic for the entire application.
## API Reference

### Register a new user

```http
  POST /api/register
```

Parameter required on request form.

Parameter location: request form

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `mail_address` | `string` | **Required**. The user mail address to be created |
| `password` | `string` | **Required**. The user password to be created |
| `confirmation_password` | `string` | **Required**. retyped password for confirmation |

Response example:
- On successful (201):
```json
{
    "message": "User registered successfully",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```
- On database error (500):
```json
{
    "message": "Failed to store user data due to database error"
}
```
- On confirmation password not match (400):
```json
{
    "message": "Your confirmation password is wrong"
}
```
- On mail address already registered (400):
```json
{
    "message": "The mail address was already registered"
}
```
- On invalid parameters (400):
```json
{
    "message": "The browser (or proxy) sent a request that this server could not understand."
}
```

### User login

```http
  POST /api/login
```

Parameter required on request form.

Parameter location: request form

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `mail_address`      | `string` | **Required**. Mail address of user to be logged in |
| `password`      | `string` | **Required**. Password of user to be logged in |

Response example:
- On successful (200):
```json
{
    "message": "User logged in successfully",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```
- On wrong password (401):
```json
{
    "message": "Wrong password"
}
```
- On mail address not found (401):
```json
{
    "message": "The mail address unavailable"
}
```
- On invalid parameters (400):
```json
{
    "message": "The browser (or proxy) sent a request that this server could not understand."
}
```


### User logout

```http
  POST /api/logout
```

No parameter required.

Instead, JWT token required for authorized the user to be logged out.

Response example:
- On successful (200):
```json
{
    "message": "User logged in successfully",
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
}
```
- On wrong password (401):
```json
{
    "message": "Wrong password"
}
```
- On mail address not found (401):
```json
{
    "message": "The mail address unavailable"
}
```
- On invalid parameters (400):
```json
{
    "message": "The browser (or proxy) sent a request that this server could not understand."
}
```


### Get all mail for authorized user

```http 
  GET /api/mails?<querystring>
```

JWT token required to access this endpoint.

Parameter location: Query string

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `type`      | `string` | Either "inbox" or "sent", will be "all" if ignored |

Response example:
- On successful (200):
```json
{
    "message": "Requested mails were successfully received",
    "result": [
        {
            "_id": "64c52078ff9eea1bf7790124",
            "sender": "sahlan.royale@gmail.com",
            "receiver": "john@mail.com",
            "subject": "Greeting from Alan",
            "body": "Hello John, this is Alan"
        },
        {
            "_id": "64cfc91cb09c6117270438ba",
            "sender": "sahlan.royale@gmail.com",
            "receiver": "john@mail.com",
            "subject": "Greeting from Alan",
            "body": "Hello John, this is Alan!!"
        }
    ]
}
```
- On server code error (500):
```json
{
    "message": "Parameter code error on server"
}
```


### Get mail from given mail ID

```http
  GET /api/mails/${mail_id}
```
Parameter location: Resource ID
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `mail_id`      | `string` | **Required**. The ID of a single mail |

Response example:
- On successful (200):
```json
{
    "message": "Requested mail was successfully received",
    "result": {
        "_id": "64c52078ff9eea1bf7790124",
        "sender": "sahlan.royale@gmail.com",
        "receiver": "john@mail.com",
        "subject": "Greeting from Alan",
        "body": "Hello John, this is Alan"
    }
}
```
- On mail not found (404):
```json
{
    "message": "The mail is not found"
}
```
- On invalid mail ID (400):
```json
{
    "message": "Invalid mail id"
}
```


### Create new mail

```http
  POST /api/mails
```

form-data required on request body

Parameter location: form-data

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `receiver` | `string` | **Required**. Receiver mail address |
| `subject` | `string` | **Required**. Subject of the email |
| `body` | `string` | **Required**. Body of the email |

Response example:
- On successful (201):
```json
{
    "message": "The mail was sent successfully"
}
```
- On database error (500):
```json
{
    "message": "Failed to send the mail due to database error"
}
```
- On receiver not found (400):
```json
{
    "message": "The receiver mail address is not found"
}
```


### Delete mail by given ID

```http
  DELETE /api/mails/${mail_id}
```

Parameter location: Resource ID

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `mail_id`      | `string` | **Required**. ID of the mail to be deleted |

Response example:
- On successful (200):
```json
{
    "message": "The mail with given ID was deleted"
}
```
- On mail not found (404):
```json
{
    "message": "The mail with given ID is not found"
}
```
- On invalid mail ID (400):
```json
{
    "message": "Invalid mail id"
}
```
- On database error (500):
```json
{
    "message": "The delete operation could not be performed due to database error"
}
```
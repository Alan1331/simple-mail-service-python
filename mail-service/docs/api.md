# Mail Sevice API Documentation
This API is intended to be datasource for mail data. Therefore, there are no authentication and authorization required to use this API. It provides CRUD operation for mail data.
## API Reference

### Get all mail from given user

```http
  GET /api/mails?<querystring>
```
Parameter location: Query string
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `mail-address`      | `string` | **Required**. Mail address of the user |
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
- On empty mail-address parameter (400):
```json
{
    "message": {
        "mail-address": "Missing required parameter in the query string"
    }
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

JSON required on request body

Parameter location: JSON request body

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `sender` | `string` | **Required**. Sender mail address |
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
- On invalid response body (400):
```json
{
    "message": "Invalid JSON data in the request body"
}
```
- On database error (500):
```json
{
    "message": "Failed to send the mail due to database error"
}
```
- On sender or receiver not found (400):
```json
{
    "message": "The sender or receiver mail address is not found"
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
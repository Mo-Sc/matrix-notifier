# Matrix Notifier

a simple script to post a message into a Matrix room using the matrix-nio python API.

Can be installed as a python package and used to send a push notification, for example when your training has finished. It is designed to not throw any errors to not interrupt other scripts.

The notifier supports html formatted messages.


## Usage
 1. Clone the repo
 2. Install the package
 3. Create a credentials.json file, as described below (or simply fill out the template in the config folder)
 4. Send a notification:
 - By using the command line script:
    ```
    matrix-notify "Hello AIMI" --config path/to/credentials.json
    ```

 - Or importing it in your python code:
    ```
    from matrix_notify.notify import notify
    notify("<h1>html formatted message</h1>", "path/to/credentials.json")
    ```


## Credential File Template

credentials.json:
```
{
    "matrix_server": "https://matrix.fau.de", -> matrix server (example: fau matrix server)
    "user_id": "@<idm>:fau.de", -> user id: see e.g. Eement (Web)App -> all settings -> General
    "access_token": "<token>", -> access token (optional): see e.g. Element (Web)App -> all settings -> Help & About -> Advanced -> Access Token
    "password": "<password>", -> password (optional): password for your Matrix Account (Caution: FAU matrix server only allows token based access (or im too stupid to setup password))
    "room_id": "<room-id>" -> internal room id (NOT room name / address): see e.g. Element (Web)App -> click on room -> settings -> advanced -> internal room id
}
```
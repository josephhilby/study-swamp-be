# Study Swamp UI

<!-- Overview -->

## Project Overview

This repository contains the backend for the Study Swamp project, built as part of the Introduction to Software Engineering (CEN 3031) course at the University of Florida.

It consists of two containerized microservices:

- A PostgreSQL database
- A Django Rest Framework API

The frontend is available here: [study-swamp-ui](https://github.com/nenaroig/study-swamp-ui)

<!-- SETUP -->

## Project Setup & Initialization

### Prerequisites

Ensure the following tools are installed:

* Docker `v28.1.1`, or later
* Docker Compose `v2.36.0`, or later

### Initial Setup

1. Clone your forked repository and navigate to the project root:
    ```bash
    git clone <your-forked-repo-url>
    cd study-swamp-be
    ```

2. Make the control script executable:

    ```bash
    chmod +x container-control.sh
    ```

3. Build and start the containers:

    ```bash
    ./container-control.sh build
    ```

<div align="center">

💡 Run `./container-control.sh help` to view additional commands.

</div>


4. Visit the API at: <http://localhost:8000/api/v1/>

   - Log in using:
      - Username: `admin1`
      - Password: `password1`


5. Access the Swagger docs at: <http://localhost:8000/api/schema/swagger-ui/>
   - Select `'Authorize 🔒'` and use (username / password):
      - Admin → `admin1` / `password1`, or Basic User → `user1` / `password3`.
      - Select `'Authorize'`, then `close`.

<br />

<!-- API ENDPOINTS -->

## Example API Endpoint
### Headers
- `'Authorization': 'Basic ${btoa("username:password")}'`
- `'Accept': 'application/vnd.api+json'`
- `'Content-Type': 'application/json'`

Note: Only add `'Content-Type': 'application/json'` for PUT/PATCH/POST requests.

<details>
<summary> <code>GET localhost:8000/api/v1/users/</code> </summary>

>**Description**
> - Get a list of users. Or single user `GET localhost:8000/api/v1/users/:id/`.
>
>**Response**
>#### 200 OK
>
> ```json
> {
>   "data": [
>     {
>       "type": "User",
>       "id": "int",
>       "attributes": 
>         {
>           "username": "str",
>           "email": "str",
>           "first_name": "str",
>           "last_name": "str",
>           "points": "int",
>           "is_superuser": "bool"
>         }
>      },
>      {...}
>    ]
> }
>```
>
>**Notes**
>
> * Student users will not see Admin user info at `api/v1/users/`. Admin will see all users. 
> * `is_superuser: bool` will only be seen by Admin users.

</details>


<details>
<summary> <code>POST localhost:8000/api/v1/users/:id/</code> </summary>

>**Description**
> - Post a new user.
> 
>**Body (data-raw)**
>
> ```json
> {
>   "username": "str",
>   "password": "str",
>   "email": "str",
>   "first_name": "str",
>   "last_name": "str"
> }
>```
>
>**Response**
>#### 201 Created
>
> ```json
> {
>   "data": {
>       "type": "User",
>       "id": "int",
>       "attributes": 
>         {
>           "username": "str",
>           "email": "str",
>           "first_name": "str",
>           "last_name": "str",
>           "points": "int"
>         }
>   }
> }
>```
>
>**Notes**
>
> * You will not be able to create Admin users.

</details>

<details>
<summary> <code>PATCH localhost:8000/api/v1/users/:id/</code> </summary>

>**Description**
> - Update an existing user.
> 
>**Body (data-raw)**
>
> ```json
> {
>   "username": "str",
>   "password": "str",
>   "email": "str",
>   "first_name": "str",
>   "last_name": "str"
> }
>```
>
>**Response**
>#### 200 OK
>
> ```json
> {
>   "data": {
>       "type": "User",
>       "id": "int",
>       "attributes": 
>         {
>           "username": "str",
>           "email": "str",
>           "first_name": "str",
>           "last_name": "str",
>           "points": "int"
>         }
>   }
> }
>```
>
>**Notes**
>
> * You only need to include the fields you want to change in the Body.

</details>

<details>
<summary> <code>DELETE localhost:8000/api/v1/users/:id/</code> </summary>

>**Description**
> - Delete an existing user.
>
>**Response**
>#### 204 No Content
>
> ```json
> 
>```
>
>**Notes**
>
> * None yet.

</details>

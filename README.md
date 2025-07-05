# Study Swamp UI

## Project Setup & Initialization

### Prerequisites

Make sure you have the following installed on your system:

* Docker 28.1.1
* Docker Compose 2.36.0

### Initial Setup

1. Fork and clone the repository:

```bash
git clone <your-forked-repo-url>
cd study-swamp-be
```

2. Navigate to root (study-swamp-be)

3. Run:

```bash
chmod +x container-control.sh
./container-control.sh build
```

Note 1: You can run `./container-control.sh help` for more info.

4. Navigate to: <http://localhost:8000/api/v1/>

5. Login with...
  - Username: `admin1`
  - Password: `password1`

6. Check the swagger docs: <http://localhost:8000/api/schema/swagger-ui/>

7. Select 'Authorize 🔒'
  - basicAuth
    - Username: `admin1`
    - Password: `password1`
  - Select 'Authorize', then close the window.

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

## Frontend

This repo was created for a school project. The frontend repo can be found [here](https://github.com/nenaroig/study-swamp-ui).
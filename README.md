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

4. Navigate to <http://localhost:8000/api/v1/>

5. Login with...
  - username: `admin1`
  - password: `password1`

<br />

<!-- API ENDPOINTS -->

## Example API Endpoint
### Headers
- `'Authorization': 'Basic ${btoa("username:password")}'`
- `'Accept': 'application/vnd.api+json'`

<details>
<summary> <code>GET localhost:8000/api/v1/users</code> </summary>

>**Description**
> - Get a list of users.
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
>      {"..."}
>    ]
> }
>```
>
>**Notes**
>
> * Student users will not see Admin user info at `api/v1/users`. Admin will see all users. 
> * `is_superuser: bool` will only be seen by Admin users.

</details>


<details>
<summary> <code>POST localhost:8000/api/v1/users</code> </summary>

>**Description**
> - Post a new user.
> 
>**Body**
>
> ```json
> {
>   "data": {
>       "type": "User",
>       "attributes": 
>         {
>           "username": "str",
>           "password": "str",
>           "email": "str",
>           "first_name": "str",
>           "last_name": "str"
>         }
>   }
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
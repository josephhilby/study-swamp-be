# Study Swamp UI

## Project Setup & Initialization

### Prerequisites

Make sure you have the following installed on your system:

* Python 3.13.3
* Django 5.2.1
* PostgreSQL
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
docker compose up --build
```

4. Navigate to <http://localhost:8000/api/v1/>

5. Login with...
  - username: `admin1`
  - password: `password1`

<br />

<!-- API ENDPOINTS -->

## API Endpoints
### GET

<details>
<summary> <code>localhost:8000/api/v1/users</code> </summary>

>**Description**
> - Get a list of users.
>
>**Parameters**
> - N/A
>
>**Response**
>#### 200 OK
>
> ```json
> {
>   "data": [
>     {
>       "type": "str",
>       "id": "int",
>       "attributes": 
>         {
>           "username": "str",
>           "email": "str",
>           "first_name": "str",
>           "last_name": "str"
>         }
>      },
>      {"..."}
>    ]
> }
>```
>
>#### 404 Not Found
>
>```json
>{
>   "errors": [
>     {
>       "detail": "Not found.",
>       "status": "404",
>       "code": "not_found"
>     }
>    ]
>}
>```
>
>**Notes**
>
> * none... yet

</details>

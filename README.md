### Local Installation

This back-end application was made with the following:

* Python 3.13.3
* Django 5.2.1

To install and run on your personal computer you will need to do the following:

1. Fork and clone the repo to your local machine.
2. Install requirements.
    ```zsh
    pip install -r requirements.txt
    ```
3. Migrate and seed database (see Note 1 & 2).
    ```zsh
    $ python3 manage.py migrate
    $ python3 manage.py loaddata user.json
    ```
4. Start a server.
    ```zsh
    python3 manage.py runserver
    ```
5. Navigate to <http://localhost:8000/api/v1/>

Note 1: If you have not set up the venv for python all commands that say `python3` should be replaced with `./.venv/bin/python3.13`. You can also set up the venv with `python3 -m venv .venv`, then `source .venv/bin/activate` to connect and `deactivate` to exit.

Note 2: If you are getting an error about the database 'study_swamp_db' not existing. Run the command `psql` to enter PostgreSQL, then `CREATE DATABASE study_swamp_db OWNER hero;` you should see the response 'CREATE DATABASE', then type `\q` to exit.

<br />

<!-- API ENDPOINTS -->

## API Endpoints
### GET

<details>
<summary> <code>localhost:8000/api/v1/user</code> </summary>

>**Description**
> - Get a list of restaurants.
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
>           "name": "str"
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

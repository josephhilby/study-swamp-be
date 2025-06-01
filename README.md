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
3. Migrate and seed database.
    ```zsh
    $ python3 manage.py migrate
    $ python3 manage.py loaddata user.json
    ```
4. Start a server.
    ```zsh
    python3 manage.py runserver
    ```
5. Navigate to <http://localhost:8000/api/v1/>

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
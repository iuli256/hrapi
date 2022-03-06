# HR API

The project is using Django, Postgres and Docker.

### How to run
1. Make sure you have Docker
2. Clone the repository
```
$ git clone https://github.com/iuli256/hrapi.git
$ cd hrapi
```
### Development
The application uses the default Django server for the development.

1. To run application in the dev mod
```
 $ docker-compose up -d --build
 ```
Before the application launching the migrations will be applied and after that the fixtures will load the HR data.

Test it out at http://localhost:8000.

2. To stop application use
```
$ docker-compose down
```

## API description
The API have 5 endpoints: 1 for CRUD and the 4 that are statistics. The statistics can be retrived using GET

```
{
    "employees": "http://127.0.0.1:8000/employees/",
    "statistics/average_age_per_industry": "http://127.0.0.1:8000/statistics/average_age_per_industry/",
    "statistics/average_salaries_per_industry": "http://127.0.0.1:8000/statistics/average_salaries_per_industry/",
    "statistics/average_salaries_per_years_of_experience": "http://127.0.0.1:8000/statistics/average_salaries_per_years_of_experience/",
    "statistics/average_salaries_per_gender_and_experience": "http://127.0.0.1:8000/statistics/average_salaries_per_gender_and_experience/"
}
```
For the CRUD endpoint we have 4 HTTP methods (GET, POST, PUT, DELETE):

### GET

1. To retrive all records paginated
```angular2html
http://127.0.0.1:8000/employees/
```
2. To search by first_name, last_name or id
```angular2html
http://127.0.0.1:8000/employees/?first_name=Annmarie
```
3. To search in any field by string
```angular2html
http://127.0.0.1:8000/employees/?search=cro
```
### POST
To create a new record use next endpoint
```angular2html
http://127.0.0.1:8000/employees/
```
with following body
```angular2html
{
            "first_name": "122Annmarie",
            "last_name": "122Crooke",
            "email": "acrooke0@gizmodo.com",
            "gender": null,
            "date_of_birth": "1978-07-09",
            "industry": "Other Specialty Stores",
            "salary": "180466.37",
            "years_of_experience": 10
}
```
### PUT
To update an existing record use next endpoint
```
http://127.0.0.1:8000/employees/<id>/ # where <id> is the id of the record that you want to update
```
with following body
```angular2html
{
            "first_name": "122Annmarie",
            "last_name": "122Crooke",
            "email": "acrooke0@gizmodo.com",
            "gender": null,
            "date_of_birth": "1978-07-09",
            "industry": "Other Specialty Stores",
            "salary": "180466.37",
            "years_of_experience": 10
}
```
### DELETE
To delete an existing record use next endpoint
```
http://127.0.0.1:8000/employees/<id>/ # where <id> is the id of the record that you want to delete
```

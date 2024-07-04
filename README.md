# Sporty-RestAPI-test

## Steps to run tests
- Create a python virtual environment and activate it
- Install the required dependencies

  ```pip install -r requirements.txt```

- Run the tests

  ```pytest```
or 
 ```pytest --html=report.html``` to generate the html report

## Tests Cases
Here is the test cases definition

| Test Case ID | Description                        | Steps                                                                                                     | API Endpoint                        | Method | Parameters | Output validation                                                                                     | Status |
|--------------|------------------------------------|-----------------------------------------------------------------------------------------------------------|-------------------------------------|--------|------------|-------------------------------------------------------------------------------------------------------|--------|
|TC_001| Validate the poems for each author | 1. Get all the authors from the author endpoint <br /> 2.For each author get all the poems <br /> 3. Validate each poem | /author<br /> /author/<author_name> | GET    | author name| For each poem we validate the author name matches and the non empty poem lines matches the line count | Fail   | 
|TC_002| Validate the poems for each title  | 1. Get all the titles from the title endpoint <br /> 2.For each title get all the poems<br /> 3.Validate each poem | /title<br /> /title/<poem_title>    |GET |poem title |For each poem we validate the title name matches and the non empty poem lines matches the line count| Fail   |


### TC_001 failed tests
- Geoffrey Chaucer poem Troilus and Criseyde: Book II line length mismatch expected 2014 != found 1759 <br />
The empty lines for this poem are not removed from the count
-  George Gordon, Lord Byron poem Stanzas for Music length mismatch expected 17 != found 16 <br />
The empty lines for this poem are not removed properly from the count
- Robert Browning poem In a Gondola length mismatch expected 245 != found 244 <br />
The empty lines for this poem are not removed properly from the count

These are also present as errors in TC_002

More details in the failing tests can be found in the [report.html](report.html)
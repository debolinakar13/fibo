### Fibonacci

Rest API has been used to return Fibonacci number of Nth term in simple template view. In order to run the web service after cloning we need to download the packages mentioned in requirements.txt

- To run the web service use the following command
**Run command**
```
python manage.py runserver
```

To access the template view we can use http://127.0.0.1:8000/api and put the number i.e N in search field for which we want to see the Nthfibonacci number. E.g for number 6 it will return 8 as the fibonacci series goes like [1,1,2,3,5,8]

- To test the testcases use the following command
**Run Command**
```
python tests.py
```



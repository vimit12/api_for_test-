# api_for_test-

Search all the three API providers simultaneously (use multi-threading or any other strategy) – one API may respond faster than other so you need to display results as soon as they arrive – no more and no less than 50 records in a page or all the results if less than 50 records returned for APIs combined.

Display Product Name, URL, Image and Price from the API results

Aggregate results into your local database – Product Name, URL, Image and Price are the mandatory fields

These APIs use pagination, so you need to ensure all records are retrieved

If the results already exist in local database, update existing records

Display matching records from your local database (first time nothing would be there) – You may expose it as another API provider, if required.

Frontend - used bootstrap , HTML, CSS Backend - Django

This project gives the search result from all 3 API and save those to local database(sQlite3).

Room for Improvement - 
1) Make the front end bit responsive.
2) I ll try to implement Pool thread instead of using Thread with django db connection pool.
3) Look to solve for memory management from API response.
4) All three API has different internal data structures so I ll try to look for solutions for that.
5) try to shorten the codes if needed.

Install pacakges : pip install -r requirements.txt

Run project :
window machine: 

                cd Scripts > activate

                cd Search
                
                python manage.py runserver
                
linux machine :

      source Scripts\activate

      cd Search

      python manage.py runserver

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT DISTINCT City FROM station Where LOWER(substr(city,1,1)) IN ('a','e','i','o','u');

/*
Enter your query here.
Please append a semicolon ";" at the end of the query and enter your query in a single line to avoid error.
*/
SELECT City, city_length FROM 
  (
  SELECT City, Length(City) as city_length 
  FROM station 
  WHERE Length(City) = (SELECT Max(Length(City)) FROM STATION)
  ORDER BY City ASC
  )
  WHERE 
  rownum = 1
  union
  SELECT City, city_length
  FROM
  (
    Select City, Length(City) as city_length
    FROM station
    WHERE Length(City) = (SELECT Min(Length(City)) FROM STATION)
    ORDER BY City ASC
  )
  WHERE rownum = 1;
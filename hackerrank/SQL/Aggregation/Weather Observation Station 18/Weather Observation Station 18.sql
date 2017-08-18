SELECT round(abs(p1.a - p2.c) + abs(p1.b - p2.d),4) from
(SELECT MAX(lat_n) as a, min(lat_n) as b FROM station where lat_n>0) p1, 
(SELECT MAX(long_w) as c, MIN(long_w) as d FROM station where long_w >0) p2;
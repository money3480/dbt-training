select * from AIRBNB.PROD.dim_listings_cleansed
where MINIMUM_NIGHTS < 1
limit 10
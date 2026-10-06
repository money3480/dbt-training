SELECT * FROM {{ ref('dim_listings_cleansed') }} A
INNER JOIN {{ ref('fct_reviews') }} B-- ON (A.LISTING_ID = B.LISTING_ID)
USING(LISTING_ID)
WHERE A.CREATED_AT > B.REVIEW_DATE
limit 10
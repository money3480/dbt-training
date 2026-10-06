from textblob import TextBlob

def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

def model(dbt, session):
    dbt.config(
        materialized = "table",
        packages = ["TextBlob", "snowflake-connector-python[pandas]"]
    )

    fct_reviews_df = dbt.ref("fct_reviews")

    df = fct_reviews_df.to_pandas()

    df["SENTIMENT_SCORE"] = df["REVIEW_TEXT"].apply(get_sentiment)

    # return final dataset (Pandas DataFrame)
    return df
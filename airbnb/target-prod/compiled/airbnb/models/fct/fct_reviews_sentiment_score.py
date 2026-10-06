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


# This part is user provided model code
# you will need to copy the next section to run the code
# COMMAND ----------
# this part is dbt logic for get ref work, do not modify

def ref(*args, **kwargs):
    refs = {"fct_reviews": "AIRBNB.PROD.fct_reviews"}
    key = '.'.join(args)
    version = kwargs.get("v") or kwargs.get("version")
    if version:
        key += f".v{version}"
    dbt_load_df_function = kwargs.get("dbt_load_df_function")
    return dbt_load_df_function(refs[key])


def source(*args, dbt_load_df_function):
    sources = {}
    key = '.'.join(args)
    return dbt_load_df_function(sources[key])


config_dict = {}
meta_dict = {}


class config:
    def __init__(self, *args, **kwargs):
        pass

    @staticmethod
    def get(key, default=None):
        return config_dict.get(key, default)

    @staticmethod
    def meta_get(key, default=None):
        return meta_dict.get(key, default)

class this:
    """dbt.this() or dbt.this.identifier"""
    database = "AIRBNB"
    schema = "PROD"
    identifier = "fct_reviews_sentiment_score"
    
    def __repr__(self):
        return 'AIRBNB.PROD.fct_reviews_sentiment_score'


class dbtObj:
    def __init__(self, load_df_function) -> None:
        self.source = lambda *args: source(*args, dbt_load_df_function=load_df_function)
        self.ref = lambda *args, **kwargs: ref(*args, **kwargs, dbt_load_df_function=load_df_function)
        self.config = config
        self.this = this()
        self.is_incremental = False

# COMMAND ----------



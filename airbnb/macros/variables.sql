{% macro learn_variables() %}
    {% set your_name_jinja = "Marvin" %}
    {{ log("Hello " ~ your_name_jinja, info=True) }}

    {{log("Hello DBT User: " ~ var("user_name", "Username is empty") ~ "!",info=True ) }}
{% endmacro %}
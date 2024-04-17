{#
This macro returns the person sex as Male or Female or Unknown
#}
{% macro get_person_sex_type(type) %}
    case
        {{ type }}
        when 'M'
        then 'Male'
        when 'm'
        then 'Male'
        when 'F'
        then 'Female'
        when 'f'
        then 'Female'
        else 'Unknown'
    end
{% endmacro %}

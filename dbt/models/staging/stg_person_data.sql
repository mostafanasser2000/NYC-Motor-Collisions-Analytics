with persons as (
    select * from {{ source('staging', 'persons') }}
    where collision_id is not null and DATE(crash_datetime) between '2013-01-01' AND '2023-12-31'
)

select
    -- identifiers
    cast(unique_id as integer) as unique_id,
    cast(collision_id as integer) as collision_id,
    -- timestamp
    cast(crash_datetime as timestamp) as crash_datetime,

    -- person info
    person_type,
    person_age,
    {{get_person_sex_type("person_sex")}} as person_sex,
    person_injury,
    safety_equipment,
    emotional_status,
    bodily_injury


from persons

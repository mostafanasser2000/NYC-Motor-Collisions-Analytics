with persons as (
    select * from {{ ref('stg_person_data') }}
),


persons_data as (
    select unique_id,
    collision_id,
    person_age,
    person_sex
    from persons
)

select * from persons_data
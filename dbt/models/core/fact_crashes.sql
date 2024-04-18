{{
    config(
        partition_by={
            "field": "crash_datetime",
            "data_type": "datetime",
            "granularity": "year"
        },
    )
}}

with
    crashes as (
        select * from {{ ref('stg_crash_data') }}
    ),
    persons as (
       select collision_id,
       sum(case when person_sex = 'Male' then 1 else 0 end) as number_of_males_affected,
       sum(case when person_sex = 'Female' then 1 else 0 end) as number_of_females_affected,
       sum(case when person_sex = 'Unknown' then 1 else 0 end) as number_of_unknowns_affected
       from {{ ref('dim_persons') }}
       group by collision_id
    ),
    vechiles as (
        select collision_id,
        count(*) AS number_of_vehicle_affected
        from {{ ref('dim_vehicle') }}
        group by collision_id
    )

select c.collision_id,
    c.crash_datetime,
    c.borough,
    c.number_of_persons_injured,
    c.number_of_persons_killed,
    c.number_of_pedestrians_injured,
    c.number_of_pedestrians_killed,
    c.number_of_cyclist_injured,
    c.number_of_cyclist_killed,
    c.number_of_motorist_injured,
    c.number_of_motorist_killed,
    -- Total killed in this collision
    c.number_of_motorist_killed+
    c.number_of_cyclist_killed +
    c.number_of_persons_killed +
    c.number_of_pedestrians_killed as total_killed,
    -- Total injured in this collision
    c.number_of_motorist_injured +
    c.number_of_cyclist_injured +
    c.number_of_persons_injured +
    c.number_of_pedestrians_injured as total_injured,
    pd.number_of_males_affected,
    pd.number_of_females_affected,
    pd.number_of_unknowns_affected,
    c.contributing_factor_vehicle_1,
    c.contributing_factor_vehicle_2,
    c.contributing_factor_vehicle_3,
    c.contributing_factor_vehicle_4,
    c.contributing_factor_vehicle_5,
    c.vehicle_type_code_1,
    c.vehicle_type_code_2,
    c.vehicle_type_code_3,
    c.vehicle_type_code_4,
    c.vehicle_type_code_5,
    vcd.number_of_vehicle_affected
from crashes c
    left join persons pd on c.collision_id = pd.collision_id
    left join vechiles vcd on c.collision_id = vcd.collision_id

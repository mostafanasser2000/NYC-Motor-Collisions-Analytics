with crashes as (
    select * from {{ source('staging', 'crashes') }}
    where collision_id is not null and DATE(crash_datetime) between '2013-01-01' AND '2023-12-31'
)

select
    -- identifiers
    cast(collision_id as integer) as collision_id,
    -- timestamp
    cast(crash_datetime as timestamp) as crash_datetime,

    -- crash info 
    borough,
    coalesce(cast(number_of_persons_injured as integer), 0) as number_of_persons_injured,
    coalesce(cast(number_of_persons_killed as integer), 0) as number_of_persons_killed,
    coalesce(cast(number_of_pedestrians_injured as integer), 0) as number_of_pedestrians_injured,
    coalesce(cast(number_of_pedestrians_killed as integer),0) as number_of_pedestrians_killed,
    coalesce(cast(number_of_cyclist_injured as integer), 0) as number_of_cyclist_injured,
    coalesce(cast(number_of_cyclist_killed as integer),0 ) as number_of_cyclist_killed,
    coalesce(cast(number_of_motorist_injured as integer), 0) as number_of_motorist_injured,
    coalesce(cast(number_of_motorist_killed as integer), 0) as number_of_motorist_killed,
    contributing_factor_vehicle_1,
    contributing_factor_vehicle_2,
    contributing_factor_vehicle_3,
    contributing_factor_vehicle_4,
    contributing_factor_vehicle_5,
    vehicle_type_code_1,
    vehicle_type_code_2,
    vehicle_type_code_3,
    vehicle_type_code_4,
    vehicle_type_code_5

from crashes

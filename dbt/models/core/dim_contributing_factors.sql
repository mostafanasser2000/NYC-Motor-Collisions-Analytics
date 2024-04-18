with crashes as (
    select * from {{ ref('stg_crash_data') }}
),


contributing_factors as (
    select collision_id, contributing_factor_vehicle_1 as contributing_factor
    from crashes
    where contributing_factor_vehicle_1 != 'Unspecified'
    union all
    select collision_id, contributing_factor_vehicle_2
    from crashes
    where contributing_factor_vehicle_2 != 'Unspecified'
    union all
    select collision_id, contributing_factor_vehicle_3
    from crashes
    where contributing_factor_vehicle_3 != 'Unspecified'
    union all
    select collision_id, contributing_factor_vehicle_4
    from crashes
    where contributing_factor_vehicle_4 != 'Unspecified'
    union all
    select collision_id, contributing_factor_vehicle_5
    from crashes
    where contributing_factor_vehicle_5 != 'Unspecified'

)

select distinct collision_id, contributing_factor
from contributing_factors
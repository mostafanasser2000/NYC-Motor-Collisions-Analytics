with crashes as (
    select * from {{ ref('stg_crash_data') }}
),


vehicles_type_codes as (
    select collision_id, vehicle_type_code_1 as vehicle_type_code
    from crashes
    where vehicle_type_code_1 is not null
    union all
    select collision_id, vehicle_type_code_2
    from crashes
    where vehicle_type_code_2 is not null
    union all
    select collision_id, vehicle_type_code_3
    from crashes
    where vehicle_type_code_3 is not null
    union all
    select collision_id, vehicle_type_code_4
    from crashes
    where vehicle_type_code_4 is not null
    union all
    select collision_id, vehicle_type_code_5
    from crashes
    where vehicle_type_code_5 is not null

)

select distinct collision_id, vehicle_type_code
from vehicles_type_codes
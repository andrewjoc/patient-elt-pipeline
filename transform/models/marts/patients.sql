with patients as (
    select *
    from {{ ref('stg_synthea__patients') }}
)
select *
from patients
select
    payers.Id as payer_id,
    payers.NAME as name,
    payers.OWNERSHIP as ownership
from 
    {{ source('raw_data', 'payers') }}
order by id asc
with claims as (
    select *
    from {{ ref('stg_synthea__claims') }}
), claims_transactions as (
    select *
    from {{ ref('stg_synthea__claims_transactions') }}
)
select
    c.*,
    ct.claim_transaction_id,
    ct.transaction_type,
    ct.transaction_amount,
    ct.transaction_payment
from claims c 
inner join claims_transactions ct
on c.claim_id = ct.claim_id
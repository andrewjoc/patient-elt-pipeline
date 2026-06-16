with claims_claims_transactions_joined as (
    select *
    from {{ ref('int_claims_claims_transactions_joined') }}
)
select *
from claims_claims_transactions_joined
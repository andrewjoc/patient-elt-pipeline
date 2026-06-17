SELECT
    claims_transactions.ID as claim_transaction_id,
    claims_transactions.CLAIMID as claim_id,
    claims_transactions.PATIENTID as patient_id,
    claims_transactions.TYPE as transaction_type,
    claims_transactions.AMOUNT as transaction_amount,
    claims_transactions.PAYMENTS as transaction_payment,
    claims_transactions.PATIENTINSURANCEID as patient_insurance_id
FROM
    {{ source('raw_data', 'claims_transactions') }}
order by claim_transaction_id asc

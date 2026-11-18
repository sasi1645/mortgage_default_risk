"""Column names for the Fannie Mae Single-Family Loan Performance (primary) files.

Order follows the Glossary and File Layout PDF (dated 11/9/2026).
The files have 114 fields: PDF positions 1-111, then 114, 117, 118.
PDF positions 112, 113, 115, 116 are marked NA for SF Loan Performance
and are assumed to be absent from the file (still to be verified).
"""

COLUMNS = [
    "reference_pool_id",  # 1  (NA for SF Loan Performance, always blank)
    "loan_id",  # 2
    "reporting_period",  # 3  MMYYYY
    "channel",  # 4
    "seller_name",  # 5
    "servicer_name",  # 6
    "master_servicer",  # 7  (NA)
    "orig_interest_rate",  # 8
    "current_interest_rate",  # 9
    "orig_upb",  # 10
    "upb_at_issuance",  # 11  (NA)
    "current_actual_upb",  # 12
    "orig_loan_term",  # 13
    "orig_date",  # 14  MMYYYY
    "first_payment_date",  # 15  MMYYYY
    "loan_age",  # 16
    "remaining_months_to_legal_maturity",  # 17
    "remaining_months_to_maturity",  # 18
    "maturity_date",  # 19  MMYYYY
    "orig_ltv",  # 20
    "orig_cltv",  # 21
    "num_borrowers",  # 22
    "dti",  # 23
    "borrower_credit_score_orig",  # 24
    "co_borrower_credit_score_orig",  # 25
    "first_time_buyer_flag",  # 26
    "loan_purpose",  # 27
    "property_type",  # 28
    "num_units",  # 29
    "occupancy_status",  # 30
    "property_state",  # 31
    "msa",  # 32
    "zip_code_short",  # 33
    "mi_percentage",  # 34
    "amortization_type",  # 35
    "prepayment_penalty_flag",  # 36
    "interest_only_flag",  # 37
    "io_first_principal_and_interest_payment_date",  # 38
    "months_to_amortization",  # 39
    "current_delinquency_status",  # 40
    "loan_payment_history",  # 41
    "modification_flag",  # 42
    "mi_cancellation_flag",  # 43
    "zero_balance_code",  # 44
    "zero_balance_effective_date",  # 45
    "upb_at_removal",  # 46
    "repurchase_date",  # 47
    "scheduled_principal_current",  # 48
    "total_principal_current",  # 49
    "unscheduled_principal_current",  # 50
    "last_paid_installment_date",  # 51
    "foreclosure_date",  # 52
    "disposition_date",  # 53
    "foreclosure_costs",  # 54
    "property_preservation_repair_costs",  # 55
    "asset_recovery_costs",  # 56
    "misc_holding_expenses_credits",  # 57
    "holding_property_taxes",  # 58
    "net_sales_proceeds",  # 59
    "credit_enhancement_proceeds",  # 60
    "repurchase_make_whole_proceeds",  # 61
    "other_foreclosure_proceeds",  # 62
    "modification_non_interest_bearing_upb",  # 63
    "principal_forgiveness_amount",  # 64
    "orig_list_start_date",  # 65
    "orig_list_price",  # 66
    "current_list_start_date",  # 67
    "current_list_price",  # 68
    "borrower_credit_score_issuance",  # 69
    "co_borrower_credit_score_issuance",  # 70
    "borrower_credit_score_current",  # 71
    "co_borrower_credit_score_current",  # 72
    "mi_type",  # 73
    "servicing_activity_flag",  # 74
    "current_period_modification_loss",  # 75
    "cumulative_modification_loss",  # 76
    "current_period_credit_event_net_gain_loss",  # 77
    "cumulative_credit_event_net_gain_loss",  # 78
    "special_eligibility_program",  # 79
    "foreclosure_principal_writeoff",  # 80
    "relocation_mortgage_flag",  # 81
    "zero_balance_code_change_date",  # 82
    "loan_holdback_flag",  # 83
    "loan_holdback_effective_date",  # 84
    "delinquent_accrued_interest",  # 85
    "property_valuation_method",  # 86
    "high_balance_loan_flag",  # 87
    "arm_initial_fixed_le_5yr_flag",  # 88
    "arm_product_type",  # 89
    "initial_fixed_rate_period",  # 90
    "interest_rate_adjustment_frequency",  # 91
    "next_interest_rate_adjustment_date",  # 92
    "next_payment_change_date",  # 93
    "arm_index",  # 94
    "arm_cap_structure",  # 95
    "initial_interest_rate_cap_up",  # 96
    "periodic_interest_rate_cap_up",  # 97
    "lifetime_interest_rate_cap_up",  # 98
    "mortgage_margin",  # 99
    "arm_balloon_flag",  # 100
    "arm_plan_number",  # 101
    "borrower_assistance_plan",  # 102
    "hltv_refinance_option_flag",  # 103
    "deal_name",  # 104
    "repurchase_make_whole_proceeds_flag",  # 105
    "alt_delinquency_resolution",  # 106
    "alt_delinquency_resolution_count",  # 107
    "total_deferral_amount",  # 108
    "payment_deferral_modification_flag",  # 109
    "interest_bearing_upb",  # 110
    "orig_classic_fico",  # 111
    "orig_vantagescore_4",  # 114
    "pricing_indicator",  # 117
    "orig_fannie_score",  # 118
]
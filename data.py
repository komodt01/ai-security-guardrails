# Simulated customer data for the AI security guardrail lab

CUSTOMERS = {
      "CUST1001": {
        "name":  "Jane Doe",
        "account number":  "4837123412349281",
        "transaction": {
          "transaction_id":  "TX84721",
          "status":  "FAILED",
          "failure_reason": "Issuer declined authorization"
        },
        "fraud_notes": "Customer is under review for suspicious activity."
      }
  }
USERS = {
    "alice": {
        "role": "payment_investigator"
    },
    "bob": {
        "role": "customer_service"
    },
    "charlie": {
        "role": "marketing"
    }
}
        


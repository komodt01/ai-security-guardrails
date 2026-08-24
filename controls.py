# Security controls for authorization and data protection
from data import CUSTOMERS
def authorize(role, request_type):
  permissions = {
     "payment_investigator": {
       "payment_failure",
       "transaction_status"
    },

    "customer_service": {
      "transaction_status"
    },

    "marketing": set()
  }  
  return request_type in permissions.get(role, set())

def minimize_data(customer, request_type):
          if request_type == "payment_failure":  
             return {
            "transaction_id": customer["transaction"]["transaction_id"],
            "status": customer["transaction"]["status"],
            "failure_reason": customer["transaction"]["failure_reason"]
             }  

          if request_type == "transaction_status":
             return {
            "transaction_id": customer["transaction"]["transaction_id"],
            "status": customer["transaction"]["status"]
        }

          return {}
def process_access(role, customer, request_type): 
    if not authorize(role, request_type):
        return {
             "status": "DENIED",
             "data": {}
        } 

    safe_data = minimize_data(customer, request_type)

    return {
        "status": "ALLOWED",
        "data": safe_data
    }

customer = CUSTOMERS["CUST1001"]

print(process_access(
    "customer_service",
    customer,
    "transaction_status"
))

customer = CUSTOMERS["CUST1001"]

print(process_access(
    "payment_investigator",
  customer,
 "payment_failure"
))


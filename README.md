# AI Security Guardrails

A lightweight Python implementation demonstrating how security guardrails can be applied to AI-enabled access to sensitive payment data.

The project focuses on enforcing authorization and data-minimization controls before information is exposed to an AI system or downstream user.

## Security Objectives

The design demonstrates several core security principles:

- **Role-Based Access Control (RBAC)** – Access is determined by the user's business role.
- **Least Privilege** – Roles receive only the permissions required for their function.
- **Data Minimization** – Even when access is authorized, only the minimum necessary data is returned.
- **Deny by Default** – Requests that are not explicitly authorized are rejected.
- **Separation of Authorization and Data Exposure** – Permission to perform an action is evaluated separately from determining which data fields may be returned.

## Example Scenario

The project models access to payment transaction information.

A `payment_investigator` may access:

- Payment failure information
- Transaction status

A `customer_service` user may access:

- Transaction status

A `marketing` user has no access to these payment investigation functions.

The same underlying customer record can therefore produce different results depending on the requesting role and business purpose.

## Guardrail Flow

```text
User / AI Request
       |
       v
Role + Request Type
       |
       v
Authorization Check
       |
   +---+---+
   |       |
 DENY     ALLOW
   |       |
   v       v
No Data   Data Minimization
              |
              v
       Approved Fields Only

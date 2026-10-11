# Goldman Sachs Operations Job Simulation

Forage, October 2026. Tasks: foundations of operations, and facilitating ultra high net worth (UHNW) transactions.

**Deliverable:** [`Trade_Fail_Report.pdf`](Trade_Fail_Report.pdf) (Word version: [`Trade_Fail_Report.docx`](Trade_Fail_Report.docx))
**Certificate:** [`certificate.pdf`](certificate.pdf)

## The task

Client A, a UHNW client, is buying a Takashi Murakami painting. A Financial Data Report lists the client's recent trades, several of which have not settled. As an operations analyst, find what could stop the purchase from being funded on time, decide which team should fix each problem, and write it up as a Trade Fail Report.

## What I found

Only one of Client A's trades had settled (a $2.0M sale on 2 July). The rest were stuck for three different reasons:

| Issue | Trades | Why it matters | Team |
|---|---|---|---|
| Funds not cleared | TXN001 ($1.0M buy, awaiting funds transfer), TXN008 ($0.7M buy, funds not available), TXN010 ($2.2M sale, awaiting documentation) | $5.7M of buys and $2.2M of sale proceeds were pending, so the client might not have cleared cash on the payment date | Trading Desk, Trading & Settlement Operations |
| Compliance hold | TXN003 ($1.5M buy, pending compliance review) | A large art purchase triggers KYC/AML and source of funds checks; the trade cannot settle until they are cleared | Compliance and Risk Management |
| Missing approval and documents | TXN006 ($2.5M buy, awaiting approval), TXN010 | The two largest open items were blocked by internal sign-off and client paperwork | Asset Transfer and Authorization, the client's Private Wealth advisor, IT if the approval system is at fault |

I also flagged TXN004 (Client B, technical issue detected) to IT so the same system problem would not hit Client A's trades.

## What the report covers

For each issue: the action taken, the team involved, a risk assessment (settlement failure, regulatory and reputational risk, operational risk from incomplete approvals), mitigation, and follow-up. It ends with four process recommendations:

1. Pre-clear funding, KYC/AML and documents before a client commits to a large, time-sensitive purchase.
2. Automatic alerts for trades pending more than 24 to 48 hours, routed to the responsible team.
3. A standard document checklist for UHNW transfers.
4. Consult a senior colleague early on high-value transactions and keep written records of decisions.

## Skills

Trade settlement, reconciliation, KYC/AML, operational risk assessment, escalation and written reporting.

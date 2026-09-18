# GenLayer Milestone Change Order

A GenLayer intelligent contract for managing milestone requirement changes through client and provider approval.

## Overview

**GenLayer Milestone Change Order** is an intelligent contract designed to manage changes to milestone requirements in a structured and transparent way.

The contract allows clients and providers to propose changes to existing requirements while ensuring that both parties must approve the proposed changes before they are applied.

It helps maintain a clear revision history and provides a structured workflow for handling milestone requirement changes.

## Key Features

* **Change Proposals** — Clients and providers can propose updates to milestone requirements.
* **Mutual Approval** — Both parties must approve a proposal before it becomes effective.
* **Change Rejection** — Either party can reject an active proposal.
* **Revision Tracking** — The contract tracks requirement revisions.
* **Access Control** — Only the client and provider can propose, approve, or reject changes.
* **Contract State** — Retrieve the current requirement, proposal details, approval status, and revision.

## Workflow

1. Initialize the contract with a provider address and the initial milestone requirement.
2. The client or provider proposes a requirement change with a reason.
3. The proposer is automatically recorded as having approved the proposal.
4. The other party reviews and approves or rejects the proposal.
5. Once both parties approve, the new requirement is applied and the revision number increases.

If a proposal is rejected, it is cancelled without changing the current requirement.

## Contract Methods

| Method                 | Description                         |
| ---------------------- | ----------------------------------- |
| `propose_change()`     | Propose a new milestone requirement |
| `approve_change()`     | Approve an active proposal          |
| `reject_change()`      | Reject an active proposal           |
| `get_contract_state()` | Retrieve the current contract state |

## State Management

The contract tracks:

* Client and provider addresses
* Current milestone requirement
* Proposed requirement and reason
* Proposal status
* Client and provider approval status
* Current revision number
* Last change status

## Testing

The contract was tested in GenLayer Studio using its transaction interface.

Test scenarios included:

* Proposing a milestone requirement change
* Rejecting a proposed change
* Approving a change through both parties
* Applying an approved change
* Checking the updated contract state and revision

The successful approval flow updated the requirement to `Deliver 20 units instead of 5` and advanced the revision to `3`.

## Technology

* GenLayer
* GenLayer Intelligent Contracts
* Python
* GenLayer Studio

## Project Status

**Implemented and tested in GenLayer Studio.**

This project is part of my ongoing journey exploring intelligent contracts and decentralized applications with GenLayer.

---

Built as part of my GenLayer developer journey.

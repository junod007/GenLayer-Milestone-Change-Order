# GenLayer Milestone Change Order

A GenLayer intelligent contract for managing milestone requirement changes through client and provider approval.

## Overview

**GenLayer Milestone Change Order** is an intelligent contract designed to manage changes to milestone requirements in a structured and transparent way.

The contract allows a client to propose a change to an existing requirement. The provider can then review the proposal and approve or reject it.

The contract tracks the proposal status, approval states, requirement revisions, and the parties involved.

## Key Features

* **Change Proposals** — Clients can propose updates to milestone requirements with a reason.
* **Dual-Party Approval** — Tracks client and provider approval independently.
* **Approval Workflow** — Supports approving or rejecting proposed changes.
* **Revision Tracking** — Maintains a revision number for requirement changes.
* **On-Chain State** — Stores proposal details, approval status, and change history state.

## Workflow

1. The client proposes a new milestone requirement and provides a reason.
2. The proposal becomes active and awaits approval.
3. The client and provider can approve the proposed change.
4. The provider can reject a proposal.
5. The contract updates its state to reflect the outcome.

## Contract State

The contract tracks:

| Field                  | Description                   |
| ---------------------- | ----------------------------- |
| `client`               | Client address                |
| `provider`             | Provider address              |
| `requirement`          | Current milestone requirement |
| `proposed_requirement` | Proposed new requirement      |
| `proposal_active`      | Whether a proposal is active  |
| `client_approved`      | Client approval status        |
| `provider_approved`    | Provider approval status      |
| `revision`             | Requirement revision number   |
| `last_change_status`   | Status of the latest change   |

## Contract Methods

| Method                 | Description                      |
| ---------------------- | -------------------------------- |
| `get_contract_state()` | Reads the current contract state |
| `propose_change()`     | Proposes a requirement change    |
| `approve_change()`     | Approves a proposed change       |
| `reject_change()`      | Rejects a proposed change        |

## Testing

The contract was deployed and tested using GenLayer Studio.

Test scenarios included:

* Proposing a milestone requirement change.
* Approving a proposed change.
* Rejecting a proposed change.
* Checking the resulting contract state.
* Verifying proposal status and revision updates.

Transactions were executed through GenLayer Studio's Run and Debug interface.

## Technology

* GenLayer
* Python
* GenLayer Studio
* Intelligent Contracts

## Project Purpose

This project explores how intelligent contracts can support milestone-based workflows by making requirement changes traceable and requiring participation from both parties.

It is part of my ongoing journey of learning and building on GenLayer.

## Disclaimer

This project is an experimental testnet implementation and is not intended for production use.

## Author

Built by [@junod07](https://github.com/junod07) as part of my GenLayer builder journey.

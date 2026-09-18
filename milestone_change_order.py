# v0.2.16
# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }

from genlayer import *


class MilestoneChangeOrder(gl.Contract):
    client: Address
    provider: Address

    requirement: str
    proposed_requirement: str
    proposal_reason: str

    revision: u256
    proposal_active: bool
    proposed_by: Address
    client_approved: bool
    provider_approved: bool

    last_change_status: str

    def __init__(
        self,
        provider: str,
        requirement: str
    ):
        self.client = gl.message.sender_address
        self.provider = Address(provider)

        self.requirement = requirement
        self.proposed_requirement = ""
        self.proposal_reason = ""

        self.revision = 1
        self.proposal_active = False
        self.proposed_by = self.client

        self.client_approved = False
        self.provider_approved = False

        self.last_change_status = "NO_CHANGE"

    @gl.public.write
    def propose_change(
        self,
        new_requirement: str,
        reason: str
    ) -> None:
        sender = gl.message.sender_address

        if sender not in [self.client, self.provider]:
            raise gl.vm.UserError(
                "Only the client or provider can propose changes."
            )

        if self.proposal_active:
            raise gl.vm.UserError(
                "An active change proposal already exists."
            )

        if new_requirement == "":
            raise gl.vm.UserError(
                "New requirement cannot be empty."
            )

        if new_requirement == self.requirement:
            raise gl.vm.UserError(
                "New requirement must differ from current requirement."
            )

        if reason == "":
            raise gl.vm.UserError(
                "A reason for the change is required."
            )

        self.proposed_requirement = new_requirement
        self.proposal_reason = reason
        self.proposed_by = sender

        self.proposal_active = True
        self.client_approved = False
        self.provider_approved = False

        if sender == self.client:
            self.client_approved = True
        else:
            self.provider_approved = True

        self.last_change_status = "PENDING_APPROVAL"

    @gl.public.write
    def approve_change(self) -> None:
        sender = gl.message.sender_address

        if not self.proposal_active:
            raise gl.vm.UserError(
                "There is no active change proposal."
            )

        if sender == self.client:
            if self.client_approved:
                raise gl.vm.UserError(
                    "Client has already approved."
                )
            self.client_approved = True

        elif sender == self.provider:
            if self.provider_approved:
                raise gl.vm.UserError(
                    "Provider has already approved."
                )
            self.provider_approved = True

        else:
            raise gl.vm.UserError(
                "Only the client or provider can approve."
            )

        if self.client_approved and self.provider_approved:
            self.requirement = self.proposed_requirement
            self.revision = self.revision + 1

            self.proposal_active = False
            self.last_change_status = "APPROVED_AND_APPLIED"

            self.proposed_requirement = ""
            self.proposal_reason = ""

    @gl.public.write
    def reject_change(self) -> None:
        sender = gl.message.sender_address

        if not self.proposal_active:
            raise gl.vm.UserError(
                "There is no active change proposal."
            )

        if sender not in [self.client, self.provider]:
            raise gl.vm.UserError(
                "Only the client or provider can reject."
            )

        self.proposal_active = False
        self.proposed_requirement = ""
        self.proposal_reason = ""

        self.client_approved = False
        self.provider_approved = False

        self.last_change_status = "REJECTED"

    @gl.public.view
    def get_contract_state(self) -> dict[str, str]:
        return {
            "client": self.client.as_hex,
            "provider": self.provider.as_hex,
            "requirement": self.requirement,
            "revision": str(self.revision),
            "proposal_active": str(self.proposal_active),
            "proposed_requirement": self.proposed_requirement,
            "proposal_reason": self.proposal_reason,
            "proposed_by": self.proposed_by.as_hex,
            "client_approved": str(self.client_approved),
            "provider_approved": str(self.provider_approved),
            "last_change_status": self.last_change_status
        }

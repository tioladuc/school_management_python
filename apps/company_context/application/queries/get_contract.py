from dataclasses import dataclass
@dataclass(frozen=True)
class GetContractQuery:
    contract_id: int

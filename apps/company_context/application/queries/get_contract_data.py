from dataclasses import dataclass
@dataclass(frozen=True)
class GetContractDataQuery:
    contract_id: int

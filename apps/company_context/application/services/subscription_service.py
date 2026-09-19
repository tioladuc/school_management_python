from ...domain.exceptions import NotFoundError
from ..dto.subscription_dto import SubscriptionDto

class SubscriptionApplicationService:
    def __init__(self, subscriptions): self.subscriptions = subscriptions
    def activate(self, command):
        s=self.subscriptions.get(command.subscription_id)
        if s is None: raise NotFoundError('Subscription not found.')
        s.status='ACTIVE'; return self.to_dto(self.subscriptions.save(s))
    def suspend(self, command):
        s=self.subscriptions.get(command.subscription_id)
        if s is None: raise NotFoundError('Subscription not found.')
        s.status='SUSPENDED'; return self.to_dto(self.subscriptions.save(s))
    @staticmethod
    def to_dto(s): return SubscriptionDto(s.id,s.company_id,s.plan_code,s.start_date,s.end_date,s.status)

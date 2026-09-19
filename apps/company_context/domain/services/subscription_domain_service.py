from ..exceptions import BusinessRuleError

class SubscriptionDomainService:
    @staticmethod
    def ensure_active(status):
        if status != 'ACTIVE':
            raise BusinessRuleError('Subscription is not active.')

from abc import ABC, abstractmethod

class SplitStrategy(ABC):

    @abstractmethod
    def calculate(self, total_amount, splits):
        pass


class EqualSplit(SplitStrategy):
    def calculate(self, total_amount, splits):
        per_person = total_amount / len(splits)
        return {s.user_id: per_person for s in splits}


class ExactSplit(SplitStrategy):
    def calculate(self, total_amount, splits):
        total = sum(s.value for s in splits)
        if total != total_amount:
            raise ValueError("Exact split does not sum to total amount")
        return {s.user_id: s.value for s in splits}


class PercentageSplit(SplitStrategy):
    def calculate(self, total_amount, splits):
        total_percent = sum(s.value for s in splits)
        if total_percent != 100:
            raise ValueError("Percentage split must sum to 100")
        return {s.user_id: (s.value / 100) * total_amount for s in splits}


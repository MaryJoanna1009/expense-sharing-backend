from app.splits import EqualSplit, ExactSplit, PercentageSplit

def get_split_strategy(split_type):
    if split_type == "equal":
        return EqualSplit()
    if split_type == "exact":
        return ExactSplit()
    if split_type == "percentage":
        return PercentageSplit()
    raise ValueError("Invalid split type")
 

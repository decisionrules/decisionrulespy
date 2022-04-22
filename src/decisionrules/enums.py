import enum


class SolverStrategies(enum.Enum):
    STANDARD = "STANDARD"
    ARRAY = "ARRAY"
    FIRST_MATCH = "FIRST_MATCH"
    EVALUATE_ALL = "EVALUATE_ALL"


class Protocols(enum.Enum):
    HTTP = "http"
    HTTPS = "https"


class SolverType(enum.Enum):
    RULE = "rule"
    RULEFLOW = "composition"

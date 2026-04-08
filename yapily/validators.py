from pydantic import AfterValidator

Unique = AfterValidator(lambda x: list(dict.fromkeys(x)))

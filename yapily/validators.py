from pydantic import AfterValidator


def _check_unique(v):
    seen = set()
    for item in v:
        if item in seen:
            raise ValueError(f"List must contain unique items, duplicate found: {item!r}")
        seen.add(item)
    return v


Unique = AfterValidator(_check_unique)

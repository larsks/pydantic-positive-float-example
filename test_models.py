from typing import Annotated
from pydantic import ValidationError, BaseModel, Field
import pytest

positiveFloat = Annotated[float, Field(ge=0)]


class OtherClass(BaseModel):
    f1: positiveFloat | list[positiveFloat] | None = None
    f2: positiveFloat | list[positiveFloat] | None = None
    f3: positiveFloat | None = None


@pytest.mark.parametrize(
    "f1,f2,f3,valid",
    (
        (1, 1, 1, True),
        (None, None, None, True),
        ([None], None, None, False),
        (-1, 1, 1, False),
        (1, -1, 1, False),
        (1, 1, -1, False),
        ([-1], 1, 1, False),
        ([1, 2, -1], 1, 1, False),
        (1, [-1], 1, False),
        (1, 1, [-1], False),
        ("one", 1, 1, False),
    ),
)
def test_validation(f1: float, f2: float, f3: float, valid: bool):
    if valid:
        obj = OtherClass(f1=f1, f2=f2, f3=f3)
        assert obj.f1 == f1
        assert obj.f2 == f2
        assert obj.f3 == f3
    else:
        with pytest.raises(ValidationError):
            obj = OtherClass(f1=f1, f2=f2, f3=f3)

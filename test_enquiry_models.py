
import pytest
from pydantic import ValidationError

from enquiry_models import Enquiry


def test_valid_enquiry():
    enquiry = Enquiry(
        name="Arun",
        phone="9876543210",
        intent="Need a website",
        urgency="high",
    )

    assert enquiry.name == "Arun"
    assert enquiry.phone == "9876543210"
    assert enquiry.urgency == "high"


def test_invalid_urgency():
    with pytest.raises(ValidationError):
        Enquiry(
            name="Arun",
            phone="9876543210",
            intent="Need a website",
            urgency="extreme",
        )


def test_missing_phone_is_allowed():
    enquiry = Enquiry(
        name="Arun",
        intent="Need a website",
        urgency="high",
    )

    assert enquiry.phone is None


def test_invalid_phone_is_rejected():
    with pytest.raises(ValidationError):
        Enquiry(
            name="Arun",
            phone="123",
            intent="Need a website",
            urgency="high",
        )

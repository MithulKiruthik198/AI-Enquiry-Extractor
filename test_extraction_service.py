
from types import SimpleNamespace
import json
import pytest
from extraction_service import extract_enquiry
from pydantic import ValidationError


def test_extract_enquiry_valid_response(monkeypatch):
    fake_response = SimpleNamespace(
        text='{"name":"Arun","phone":"9876543210",'
             '"intent":"Need a website","urgency":"high"}'
    )

    monkeypatch.setattr(
        "extraction_service.ask_gemini",
        lambda prompt: fake_response,
    )

    result = extract_enquiry("I need a website urgently.")

    assert result["name"] == "Arun"
    assert result["phone"] == "9876543210"
    assert result["urgency"] == "high"

def test_extract_enquiry_invalid_json(monkeypatch):
    fake_response = SimpleNamespace(
        text="This is not valid JSON"
    )

    monkeypatch.setattr(
        "extraction_service.ask_gemini",
        lambda prompt: fake_response,
    )

    with pytest.raises(json.JSONDecodeError):
        extract_enquiry("I need a website urgently.")


def test_extract_enquiry_invalid_urgency(monkeypatch):
    fake_response = SimpleNamespace(
        text='{"name":"Arun","phone":"9876543210",'
             '"intent":"Need a website","urgency":"extreme"}'
    )

    monkeypatch.setattr(
        "extraction_service.ask_gemini",
        lambda prompt: fake_response,
    )

    with pytest.raises(ValidationError):
        extract_enquiry("I need a website urgently.")

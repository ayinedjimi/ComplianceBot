"""
Tests for ComplianceBot

Author: Ayi NEDJIMI
"""

import pytest
from compliancebot import ComplianceAssistant


def test_initialization():
    """Test assistant initialization"""
    assistant = ComplianceAssistant()
    assert assistant.version == "1.0.0"
    assert assistant.author == "Ayi NEDJIMI"


def test_frameworks():
    """Test framework listing"""
    assistant = ComplianceAssistant()
    frameworks = assistant.get_frameworks()
    assert "GDPR" in frameworks
    assert "ISO27001" in frameworks

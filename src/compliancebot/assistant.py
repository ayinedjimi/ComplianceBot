"""
Compliance Assistant using Transformers

Author: Ayi NEDJIMI
"""

import logging
from typing import Dict, List, Optional
from transformers import pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ComplianceAssistant:
    """AI-powered compliance assistant"""

    FRAMEWORKS = {
        "GDPR": "General Data Protection Regulation",
        "ISO27001": "Information Security Management",
        "NIST": "NIST Cybersecurity Framework",
        "PCI-DSS": "Payment Card Industry Data Security Standard",
        "HIPAA": "Health Insurance Portability and Accountability Act",
        "SOC2": "Service Organization Control 2"
    }

    def __init__(self, model_name: str = "distilbert-base-uncased-distilled-squad"):
        """Initialize the compliance assistant"""
        self.version = "1.0.0"
        self.author = "Ayi NEDJIMI"
        logger.info(f"Initializing ComplianceBot v{self.version}")

        try:
            self.qa_pipeline = pipeline("question-answering", model=model_name)
            logger.info(f"Loaded model: {model_name}")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            self.qa_pipeline = None

    def ask(self, question: str, context: str) -> Dict[str, any]:
        """Ask a compliance question"""
        if not self.qa_pipeline:
            return {"error": "Model not loaded"}

        try:
            result = self.qa_pipeline(question=question, context=context)
            return {
                "answer": result["answer"],
                "confidence": result["score"],
                "question": question
            }
        except Exception as e:
            logger.error(f"Error processing question: {e}")
            return {"error": str(e)}

    def get_frameworks(self) -> List[str]:
        """Get list of supported compliance frameworks"""
        return list(self.FRAMEWORKS.keys())

    def get_framework_info(self, framework: str) -> Optional[str]:
        """Get information about a framework"""
        return self.FRAMEWORKS.get(framework.upper())

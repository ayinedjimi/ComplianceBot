"""
Basic usage example for ComplianceBot

Author: Ayi NEDJIMI
"""

from compliancebot import ComplianceAssistant


def main():
    print("=== ComplianceBot Example ===\n")

    # Initialize assistant
    assistant = ComplianceAssistant()

    # Example question
    context = """
    GDPR requires organizations to implement data protection by design and by default.
    Personal data must be processed lawfully, fairly and transparently.
    Organizations must obtain consent before processing personal data.
    """

    question = "What does GDPR require for data processing?"

    # Ask question
    result = assistant.ask(question, context)

    print(f"Question: {result['question']}")
    print(f"Answer: {result['answer']}")
    print(f"Confidence: {result['confidence']:.2%}")


if __name__ == "__main__":
    main()

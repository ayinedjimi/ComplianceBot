"""
Gradio Web Interface for ComplianceBot

Author: Ayi NEDJIMI
"""

import gradio as gr
from .assistant import ComplianceAssistant


def create_interface():
    """Create Gradio interface"""
    assistant = ComplianceAssistant()

    def answer_question(question, context):
        """Handle question answering"""
        if not question or not context:
            return "Please provide both a question and context."

        result = assistant.ask(question, context)

        if "error" in result:
            return f"Error: {result['error']}"

        return f"Answer: {result['answer']}\n\nConfidence: {result['confidence']:.2%}"

    # Create interface
    demo = gr.Interface(
        fn=answer_question,
        inputs=[
            gr.Textbox(label="Your Compliance Question", placeholder="What are the key requirements?"),
            gr.Textbox(label="Context/Document", placeholder="Paste relevant policy or regulation text...", lines=10)
        ],
        outputs=gr.Textbox(label="Answer"),
        title="🔐 ComplianceBot - AI Compliance Assistant",
        description=f"""
        **ComplianceBot v{assistant.version}** by Ayi NEDJIMI
        
        Ask questions about compliance frameworks (GDPR, ISO27001, NIST, etc.)
        
        Website: [ayinedjimi-consultants.fr](https://ayinedjimi-consultants.fr)
        """,
        examples=[
            ["What are the key principles?", "GDPR requires data protection by design and by default..."],
            ["What encryption is required?", "ISO 27001 mandates cryptographic controls for sensitive data..."]
        ]
    )

    return demo


if __name__ == "__main__":
    demo = create_interface()
    demo.launch(server_name="0.0.0.0", server_port=7860)

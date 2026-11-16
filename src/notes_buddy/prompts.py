from notes_buddy.conversation_turn import ConversationTurn
import textwrap

SYSTEM_PROMPT = textwrap.dedent("""
    This is a notes taking application. User inputs needs to be considered in relation to notes.
    At the start of the conversation if the user want to create notes for the topic user is talking about
""")

def build_messages_for_llm(conversation_history: list):
    messages: list = [{
        "role": "system",
        "content": SYSTEM_PROMPT
    }]

    for conversation_turn in conversation_history:
        messages.append({
            "role": conversation_turn.role,
            "content": conversation_turn.text
        })

    return messages


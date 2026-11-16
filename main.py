from notes_buddy.conversation_turn import LLMResponse, UserInput
from notes_buddy.prompts import build_messages_for_llm
from notes_buddy.llm import call_llm

EXIT_PHRASES = ["exit", "quit"]


def main():

    conversation: list[UserInput | LLMResponse] = []

    while True:
        raw_user_text: str = input("Put your thoughts to be noted here: ")
        clean_text = raw_user_text.strip()
        if not clean_text:
            continue
        if clean_text.lower() in EXIT_PHRASES:
            break
        user_input = UserInput(text=clean_text)
        conversation.append(user_input)

        messages_for_llm = build_messages_for_llm(conversation_history=conversation)

        call_llm(model="liquid/lfm-3-1.7b:free", messages=messages_for_llm)

        conversation.append(LLMResponse(text="That's great"))
        print(conversation[-1].text)


if __name__ == "__main__":
    main()

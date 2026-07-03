from chatbot import DenoBot
from speech import listen, speak


def main() -> None:
    bot = DenoBot()
    print(f"{bot.name} Assistant is ready. Type 'exit' to quit.")

    while True:
        try:
            user_input = input("You: ").strip()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

        if user_input.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not user_input:
            print("Listening for voice input...")
            user_input = listen()
            print(f"You (voice): {user_input}")

        if not user_input:
            print(f"{bot.name}: I could not hear you clearly. Please try again.")
            speak("I could not hear you clearly. Please try again.")
            continue

        response = bot.respond(user_input)
        print(f"{bot.name}: {response}")
        speak(response)


if __name__ == "__main__":
    main()

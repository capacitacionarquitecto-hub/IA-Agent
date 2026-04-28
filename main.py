"""
Interactive chat module (v2) for making chat completion requests
using the official OpenAI library against a local Ollama server.

This version extends the previous script (v1) by introducing an
interactive command-line loop that allows the user to have a
continuous conversation with the model until an exit command
is issued.

Changes compared to v1:
    - Added an infinite loop (while True) to enable interactive chat.
    - User input is now read dynamically from the terminal using input().
    - Introduced exit conditions ("exit", "quit", "salir") to gracefully
      terminate the program.
    - Added console prompts and labels ("You:", "Bear:") for clearer
      interaction.
    - The system persona remains persistent across all user messages,
      instead of being used for a single request.

Author: Enrique Barros Fernández
Version: v2
Dependencies:
    - openai (compatible OpenAI client library)
    - Ollama running at http://localhost:11434
"""

from openai import OpenAI

# Initialize the client pointing to your local Ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"  # Required by the library, but ignored by Ollama
)

print("--- Bear Chat Activated (Type 'exit' to quit) ---")

while True:
    # Get custom input from the user via terminal
    user_message = input("\nYou: ")

    # Condition to break the loop
    if user_message.lower() in ["exit", "quit", "salir"]:
        print("Bye bye! *Grows and leaves*")
        break

    # Create the chat completion request
    resp = client.chat.completions.create(
        model="qwen3.5:397b-cloud",
        messages=[
            # System role: Persistent persona rules
            {
                "role": "system", 
                "content": "Eres Un Asesor financiero experto, con un tono amigable y cercano. Respondes a las preguntas de los usuarios de manera clara y sencilla, utilizando ejemplos prácticos para explicar conceptos financieros complejos. Siempre buscas ayudar a los usuarios a entender mejor sus finanzas personales y a tomar decisiones informadas."
            },
            # User role: Now uses the variable from input()
            {
                "role": "user", 
                "content": user_message
            }
        ]
    )

    # Print the bear's response
    print("Bear:", resp.choices[0].message.content)
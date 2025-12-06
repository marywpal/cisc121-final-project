import random as r
import gradio as gr

def start_game():
    low = 1
    high = 100
    guess = r.randint(low, high)  # The first guess is random for more variety
    message = f"Is your number {guess}?"
    guess_count = 1
    first_guess = True  # Keep track that this was the first guess
    return message, low, high, guess, guess_count, first_guess

def next_guess(response, low, high, guess, guess_count, first_guess):
    if response == "Higher":
        low = guess + 1
    elif response == "Lower":
        high = guess - 1
    else:
        return f"I got your number in {guess_count} guesses!", low, high, guess, guess_count, False

    if low <= high:
        if first_guess:
            # After the first arbitrary guess, it switchs over to binary search
            guess = (low + high) // 2
            first_guess = False
        else:
            guess = (low + high) // 2
        guess_count += 1
        message = f"Is your number {guess}?"
    else:
        message = "Your responses were inconsistent. Make sure to stick with the same number."
        first_guess = False

    return message, low, high, guess, guess_count, first_guess

with gr.Blocks() as demo:
    gr.Markdown("## Think of a number between 1 and 100, and I will try to guess it!")

    low_state = gr.State(1)
    high_state = gr.State(100)
    guess_state = gr.State(None)
    guess_count_state = gr.State(0)
    first_guess_state = gr.State(True)

    response_box = gr.Textbox(label="Computer's Guess")
    rb = gr.Radio(["Higher", "Lower", "Correct"], label="Your Response")

    start_btn = gr.Button("Start Game")
    next_btn = gr.Button("Submit Response")

    start_btn.click(
        start_game,
        outputs=[response_box, low_state, high_state, guess_state, guess_count_state, first_guess_state]
    )

    next_btn.click(
        next_guess,
        inputs=[rb, low_state, high_state, guess_state, guess_count_state, first_guess_state],
        outputs=[response_box, low_state, high_state, guess_state, guess_count_state, first_guess_state]
    )

demo.launch()



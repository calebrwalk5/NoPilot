from NoPilot import GPT2

def run():
    gpt2 = GPT2()

    print("Reading Code...")
    while True:
        try:
            text = input("> ")
            prediction = gpt2.predict_next(text, 5)
            print("{} {}".format(text, prediction))

        except KeyError:
            pass

if __name__ == "__main__":
    run()

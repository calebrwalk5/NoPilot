from NoPilot import GPT2

def run():
    gpt2 = GPT2()
    line = 1
    print("Reading Code...")
    while True:
        try:
            text = input(line " | ")
            prediction = gpt2.predict_next(text, 1)
            print("{} {}".format(text, prediction))
            line += 1
            
        except KeyError:
            pass

if __name__ == "__main__":
    run()

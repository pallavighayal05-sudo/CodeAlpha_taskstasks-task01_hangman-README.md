import random

# List of 5 predefined words
words = ["python", "hangman", "programming", "developer", "console"]

# Select a random word
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎯 Welcome to Hangman!")
print("You have 6 chances to guess the word.")
print(" ".join(guessed))

while attempts > 0 and "_" in guessed:
    guess = input("\nEnter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Enter a single letter only.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts -= 1
        print(f"❌ Wrong guess! Attempts left: {attempts}")

    print("Word: " + " ".join(guessed))
    print("Guessed letters:", ", ".join(guessed_letters))

# Final result
if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over! The word was:", word)

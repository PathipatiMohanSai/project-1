def ask_question(question, options):
  """
  Presents a question with multiple choice options and returns user input.

  Args:
      question: The question to be asked.
      options: A list of strings representing the answer choices.

  Returns:
      The user's input as a string (converted to uppercase).
  """
  print(question)
  for i, option in enumerate(options):
    print(f"{i+1}. {option}")
  answer = input("Enter your answer (number): ").upper()
  return answer

def check_answer(answer, correct_answer):
  """
  Checks if the user's answer matches the correct answer.

  Args:
      answer: The user's answer as a string.
      correct_answer: The correct answer (zero-based index).

  Returns:
      True if the answer is correct, False otherwise.
  """
  return int(answer) - 1 == correct_answer

def display_feedback(answer, correct_answer, options):
  """
  Provides feedback based on the user's answer.

  Args:
      answer: The user's answer as a string.
      correct_answer: The correct answer (zero-based index).
      options: A list of strings representing the answer choices.
  """
  if check_answer(answer, correct_answer):
    print("Correct!")
  else:
    print("Incorrect.")
    print(f"The correct answer was: {options[correct_answer]}")

def main():
  """
  The main function that runs the quiz game.
  """
  # Define quiz data
  questions = [
      "What is the capital of France?",
      ["London", "Berlin", "Paris", "Madrid"],
      "What is the largest planet in our solar system?",
      ["Earth", "Jupiter", "Mars", "Venus"],
      "What is the meaning of life?",
      ["42", "There is none", "It's a personal journey", "Love"]
  ]

  score = 0
  for i in range(0, len(questions), 2):
    question = questions[i]
    options = questions[i+1]
    answer = ask_question(question, options)
    correct_answer = 2  # Modify this for each question (correct answer index)
    display_feedback(answer, correct_answer, options)
    if check_answer(answer, correct_answer):
      score += 1

  print(f"You scored {score} out of {len(questions) // 2} questions.")

if __name__ == "__main__":
  main()

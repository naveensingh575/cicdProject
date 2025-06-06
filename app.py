def to_uppercase(input_string):
  """
  Converts the given input string to its uppercase equivalent.

  Args:
    input_string (str): The string to be converted to uppercase.

  Returns:
    str: The uppercase version of the input string.
  """
  if not isinstance(input_string, str):
    raise TypeError("Input must be a string.")
  return input_string.upper()

if __name__ == "__main__":
  # This block only runs when the script is executed directly (not imported as a module)

  print("--- Uppercase Function Demonstration ---")

  # Example 1: A regular string
  text1 = "hello world"
  uppercase_text1 = to_uppercase(text1)
  print(f"Original: '{text1}'")
  print(f"Uppercase: '{uppercase_text1}'\n")

  # Example 2: A string with mixed case
  text2 = "PyThOn PrOgRaMmInG"
  uppercase_text2 = to_uppercase(text2)
  print(f"Original: '{text2}'")
  print(f"Uppercase: '{uppercase_text2}'\n")

  # Example 3: An empty string
  text3 = ""
  uppercase_text3 = to_uppercase(text3)
  print(f"Original: '{text3}'")
  print(f"Uppercase: '{uppercase_text3}'\n")

  # Example 4: A string with numbers and symbols
  text4 = "123 Test!@#"
  uppercase_text4 = to_uppercase(text4)
  print(f"Original: '{text4}'")
  print(f"Uppercase: '{uppercase_text4}'\n")

  # Example 5: Demonstrating error handling for non-string input
  try:
    to_uppercase(123)
  except TypeError as e:
    print(f"Caught expected error: {e}")

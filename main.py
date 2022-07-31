alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet = []
for xyz in range(0, 10000):
  alphabet += alphabet1
numbers_first = ""
for i in range(0, 10):
  numbers_first += f"{i} "
numbers1 = numbers_first.split()
numbers = []
for number in range(0, 10000):
  numbers += numbers1

end_of_program = False

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  for char in start_text:
    if char not in alphabet:
      if char in numbers:
        thing = numbers
        if shift_amount > 10:
          shift_amount = shift_amount % 10
      else:
        end_text += char
        continue
    else:
      thing = alphabet
      if shift_amount > 26:
        shift_amount = shift_amount % 26
    if cipher_direction == "encode":
      position = (thing.index(char)) + shift_amount
    elif cipher_direction == "decode":
      position = (thing.index(char)) - shift_amount
    end_text += thing[position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

from art import logo
print(logo)

def the_way():
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
while end_of_program == False:
  the_way()
  restart = input("\nDo you want to restart the cypher program? Yes, or No. ").lower()
  if restart == "yes":
    end_of_program = False
  elif restart == "no":
    print("Bye.")
    end_of_program = True



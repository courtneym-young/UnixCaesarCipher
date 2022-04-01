#Caesar Cipher
import sys

key = sys.argv #key for Cipher

original_msg = input("Enter your message: ")
original_msg = original_msg.upper()

key = int(key[1])


key %= 26
cipher_msg = ""

#encrypt message
for char in original_msg:
  if char.isalpha():
    ascii_num = ord(char)

    if (ascii_num >= 65) and (ascii_num <= 90):
      new_letter_num = ascii_num + key

      if (new_letter_num >= 65) and (new_letter_num <= 90):
        cipher_msg += chr(new_letter_num)

      else:
        new_letter_num = new_letter_num - 26
        cipher_msg += chr(new_letter_num)
  
#correct the formatting (chunks of 5, no more than 10 chunks in one line)
n = 5
chunks = [cipher_msg[i:i+n] for i in range(0, len(cipher_msg), n)]
final_output = ""

i = 0
while i < (len(chunks) - 1):
  final_output += chunks[i] + " "
  i += 1
  if (i % 10) == 0:
    final_output += "\n"
final_output += chunks[i]

print(final_output)  

      


# XOR Encryptor / Decryptor

This project implements a simple **text encryptor and decryptor** using the logical **XOR** operation with a randomly generated binary key.  
It demonstrates how XOR encryption works and how the same process can be reversed to recover the original text.
## How It Works
XOR (exclusive OR) is a logical operation that compares two bits:
- If the bits are the same → result is `0`
- If the bits are different → result is `1`
The key property of XOR is that **the same process can be used for both encryption and decryption**
### Program steps:
1. Convert the input text into its binary representation (8 bits per character).  
2. Generate a **random 8-bit key**.  
3. Repeat the key (keystream) to match the length of the binary text.  
4. Apply XOR bit by bit between the binary text and the keystream.  
5. Return the resulting binary string as the encrypted text.
To decrypt, the program takes the encrypted text and applies XOR again with the same key, recovering the original message.
### Example Usage
<img width="1052" height="88" alt="image" src="https://github.com/user-attachments/assets/b42ac6d0-e439-45ab-9bfc-48289126300e" />

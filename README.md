# Diffie-Hellman-Key-Exchange

This script implements the Diffie-Hellman-Key-Exchange by creating a "random" prime number (p) and it's primitive root modulo (p). Random private keys for both Alice and Bob are then created. Once the random prime number, the primitive root modulo, and the private keys are created, both Alice and Bob exchange their public keys using the p and g values. using each other's public keys and the p and g values, they create their shared secret value that eve can't know.

# NO INPUT REQUIRED FOR THIS PYTHON SCRIPT

# Output

It will show the shared secret value of Alice and Bob. Under will be a table showing what Alice, Bob, and Eve know throughout each step in the key exchange.

import re

# Define some regular expressions for tokens
token_patterns = [
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'\bwhile\b', 'WHILE'),
    (r'\b\d+\b', 'NUMBER'),
    (r'\b[a-zA-Z]+\b', 'IDENTIFIER'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'MULTIPLY'),
    (r'/', 'DIVIDE'),
    (r'=', 'EQUALS'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
]

# Sample input code
code = "if x > 0: y = 2 * x + 1"

# Tokenize the input code
tokens = []
for pattern, token_type in token_patterns:
    tokens.extend((token_type, token) for token in re.findall(pattern, code))

print(tokens)

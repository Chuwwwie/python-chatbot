import random

# Define responses
responses = {
    "hi": ["Hello! sweety my love may tanong ako sayo", "Hi there shine! may tanong ako sayo", "Hey my sugar plum ampiyampiyam may question ako sayo!"],
    "ano": ["may chance ba ako sayo?(⁠╥⁠﹏⁠╥⁠)", "pwede ba ako maging bf mo?(⁠٥⁠↼⁠_⁠↼⁠)"," pwede ba maging akin ka na lang?"],
    "yes": ["yessss!!! ILOVEYOU(⁠•⁠ө⁠•⁠)⁠♡.", "YEEEYY ILOVEYOU(⁠*⁠＾⁠3⁠＾⁠)⁠/⁠～⁠♡."],
    "no": ["Bahala ka sa Buhay mo akin ka lang>⁠.⁠<", "oopppsss error", "agoiಠ⁠ω⁠ಠ:("],
}

# Start the conversation
print("Helloo! I'm a Chuwieee chat bot! type hi to start (⁠◠⁠‿⁠◕⁠).")
while True:
    user_input = input("emerald: ").lower()
    if user_input in responses:
        response = random.choice(responses[user_input])
        print("chuwiee:", response)
        if user_input == 'quit':
            break
    else:
        print("chuwiee: mahal kita(⁠ ⁠˘⁠ ⁠³⁠˘⁠)⁠♥.")
        
  

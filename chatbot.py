import aiml

# Create the kernel and learn AIML files
kernel = aiml.Kernel()
kernel.learn("bot2.aiml")

# Press CTRL-C to break this loop
while True:
    print (kernel.respond(input("Enter your message >> ")))
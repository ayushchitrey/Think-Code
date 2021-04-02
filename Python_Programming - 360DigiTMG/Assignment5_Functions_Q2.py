''' Q2. Write a simple user defined function that greets a person in such a way that:
    i) It should accept both name of person and message you want to deliver.
    ii) If no message is provided, it should greet a default message ‘How are you’
    Ex: Hello ---xxxx---, How are you - default message.
    Ex: Hello ---xxxx---, --xx your message xx--- '''
    

name = input("Enter the name: ")
msg = input("Enter the message: ")
if msg == "":                       #In-case of No personal message
    print("Hello " + name + ". " + "How are you ?")
else:                               #In-case of personal message
    print("Hello " + name + ". " + msg)
    
    
    

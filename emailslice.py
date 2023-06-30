def main():
    print("Welcome to the Email Slicer! ")
    print("")

    email_imput = input ("Please enter your email: ")
    
    # for (int i = 0; i < email_imput; i++)
    # {

    # }
    (username, domain) = email_imput.split("@")
    (domain, extension) = domain.split(".")

    print("Username: ", username)
    print("Domain: ", domain)
    print("Extension ", extension)

while True:
    main()


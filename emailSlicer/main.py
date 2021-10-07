email = input("Email: ").strip()
name = email[:email.index("@")]
domainName = email[email.index("@")+1:]
print(f"Name: '{name}'\nDomain: '{domainName}'")
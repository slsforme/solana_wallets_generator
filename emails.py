def add_password_to_emails():
    result = []
    with open("emails.txt", 'r') as f:
        for email in f:
            line = email.strip()
            password = line.split(':', 1)[1]
            new_line = f"{line}:{password}"
            result.append(new_line)

    with open("emails.txt", 'w') as f:
        for line in result:
            f.write(line + '\n')


add_password_to_emails()
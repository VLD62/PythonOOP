class EmailValidator:
    def __init__(self, min_length: int, mails: list, domains: list):
        self.min_length = min_length
        self.mails = mails
        self.domains = domains

    def __validate_name(self, name):
        return  len(name) >= self.min_length

    def __validate_mail(self, mail):
        return mail in self.mails

    def __validate_domain(self, domain):
        return domain in self.domains

    def validate(self, email):
        email_parts = email.split("@")
        name = email_parts[0]
        mail, domain = email_parts[1].split(".")
        return self.__validate_name(name) and self.__validate_mail(mail) \
                    and self.__validate_domain(domain)


mails = ["gmail", "softuni"]
domains = ["com", "bg"]
email_validator = EmailValidator(6, mails, domains)
print(email_validator.validate("pe77er@gmail.com"))
print(email_validator.validate("georgios@gmail.net"))
print(email_validator.validate("stamatito@abv.net"))
print(email_validator.validate("abv@softuni.bg"))
print(email_validator.validate("abv@softuni.bg.com"))
print(email_validator.validate("abvsoftunibg"))
print(email_validator.validate("213232132"))

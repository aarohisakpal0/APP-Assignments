# Experiment 2: Dynamic Report Generator
# Advanced Python Programming Lab

# Decorator for bold formatting
def bold_text(func):
    def wrapper(*args, **kwargs):
        return "***************\n" + func(*args, **kwargs) + "\n***************"
    return wrapper


class Report:
    # Class variable
    templates = {}

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    @classmethod
    def add_template(cls, name, template):
        cls.templates[name] = template

    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method
    def __call__(self, template_name):
        template = Report.get_template(template_name)
        if template:
            return template(self)
        return "Template not found."

    # Magic method
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"


def simple_template(report):
    return f"Title: {report.title}\nContent: {report.content}"


@bold_text
def fancy_template(report):
    return f"Title: {report.title}\nContent: {report.content}"


def main():
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    title = input("Enter Report Title: ")
    content = input("Enter Report Content: ")

    report = Report(title, content)

    print("\n--- Simple Report ---")
    print(report("simple"))

    print("\n--- Fancy Report ---")
    print(report("fancy"))

    print("\n--- Using __str__() ---")
    print(report)


if __name__ == "__main__":
    main()

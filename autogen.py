import names
import inquirer
from random import randint, choice


ATTRIBUTE = {
    "names": "varchar(255) default NULL",
    "phone": "varchar(100) default NULL",
    "email": "varchar(255) default NULL",
    "group_names": "char(1) default NULL",
    "salary": "integer NULL",
    "create_at": "timestamp default now()"
}


def create_name():
    return names.get_full_name()


def create_phone():
    phone = "0"
    for _ in range(9):
        phone += str(randint(0, 7))
    return phone


def create_email():
    email = names.get_first_name() + "@gmail.com"
    return email


def create_salary():
    return randint(1e3, 1e6)


def create_table(table_name, attribute_name):
    script = f"CREATE TABLE \"{table_name}\" (\n\tid SERIAL PRIMARY KEY, \n"
    for i in attribute_name:
        script += f"\t{i} {ATTRIBUTE[i]},\n"

    script = script[:-2] + "\n);"
    return script


def create_group_names():
    group_list = ['A', 'B', 'C']
    return choice(group_list)


def main():
    sql_text = ""
    script_insert = ""
    AMOUNT = int(input("Amount of data: "))
    TABLE_NAME = input("Table name: ")

    select_attribute = [
        inquirer.Checkbox('Attribute',
                          message="Spacebar to select Attribute or enter to generate",
                          choices=ATTRIBUTE.keys(),
                          ),
    ]

    attribute = inquirer.prompt(select_attribute)
    attribute = attribute["Attribute"]
    sql_create_table = create_table(TABLE_NAME, attribute)

    for i in range(AMOUNT):
        temp = "\t("
        for i in attribute:
            if i == "names":
                temp += f"'{create_name()}', "
            elif i == "phone":
                temp += f"'{create_phone()}', "
            elif i == "email":
                temp += f"'{create_email()}', "
            elif i == "salary":
                temp += f"{create_salary()}, "
            elif i == "group_names":
                temp += f"'{create_group_names()}', "

        temp = temp[:-2]
        temp += "),\n"
        script_insert += temp
    script_insert = script_insert[:-2] + ";"

    sql_text += f"DROP TABLE IF EXISTS \"{TABLE_NAME}\";\n\n"
    sql_text += f"{sql_create_table}\n\n"
    sql_text += f"INSERT INTO {TABLE_NAME} ("

    # create table
    for i in attribute:
        if i != "create_at":
            sql_text += f"{i}, "

    sql_text = sql_text[:-2]

    sql_text += ")\nVALUES\n"
    sql_text += script_insert
    try:
        with open('script.sql', 'x') as f:
            f.write(sql_text)
        print("Seccess to create script")
    except:
        print("Error to create")


if __name__ == '__main__':
    main()

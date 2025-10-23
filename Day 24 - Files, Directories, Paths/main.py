PLACEHOLDER = "[name]"
with open(r".\Input\Names\invited_names.txt", mode="r") as name_list:
    names = name_list.readlines()
for name in names:
    name_clear = name.strip()
    with open(fr".\Output\ReadyToSend\{name_clear}.txt", mode="w") as mail:
        with open(r".\Input\Letters\starting_letter.txt", mode="r") as starting_letter:
            content = starting_letter.read()
        if PLACEHOLDER in content:
            n = content.replace(PLACEHOLDER,name_clear)
        mail.write(n)
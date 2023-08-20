from id_validator import validator

id_card_number = "410823198509119532"
valid = validator.is_valid(id_card_number)

if valid:
    parsed_info = validator.get_info(id_card_number)
    print(parsed_info)

    print(parsed_info['address'])
    print(parsed_info['birthday_code'])
    print(parsed_info['chinese_zodiac'])
    print(parsed_info['age'])
    print(parsed_info['sex'])
else:
    print("无效的身份证号码")

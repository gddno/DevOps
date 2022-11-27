
    # def create_record(name, telephone, address):
    #     """Create Record"""
    #     record = {
    #         'name': name,
    #         'phone': telephone,
    #         'address': address
    #     }
    #     return record

    # user1 = create_record("Vasiliy", "89183288814", "Novoizm, 34")
    # user2 = create_record("Vladimir", "89183288815", "Novoizm, 33")
    # user3 = create_record("Irinr", "89183288816", "Novoizm, 32")

    # print(user1)
    # print(user3)

def give_award(medal, *persons):
    """Give Medals to persons"""
    for person in persons:
        print("Tovarish " + person.title() + " nagragdaetsya medalyu " + medal)

give_award("Berlin", "Dima", "Petya", "Tema")
give_award("Varshavu", "Denis", "Fedor", "Ivan")
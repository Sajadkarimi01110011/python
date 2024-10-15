#برای پاکسازی ترمینال os  فراخوانی کتابخانه  
from os import system

# برای اشخاص حقیقی (از 1000 شروع میشود) generator
def haghighi_id_generator():
    id = 1000
    while True:
        yield id 
        id += 1 

# برای اشخاص حقوقی (از 5000 شروع میشود) generator
def hoghoghi_id_generator():
    id = 5000
    while True:
        yield id
        id += 1 

# Information تعریف یک کلاس والد به نام 
class Information:
    def __init__ (self , id , name , phone_number ,
                   email , code_city , type ):
        self.__id = id
        self.__name = name
        self.__phone_number = phone_number
        self.__email = email
        self.__code_city = code_city
        self.__type = type

# استفاده از پراپرتی مقادیر پرایوت بالا
    @property
    def id (self):
        return self.__id
    @id.setter
    def id(self , ID):
        self.__id = ID

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self , fname):
        self.__name = fname

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self , Phone_number):
        self.__phone_number = Phone_number

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self , Email):
        self.__email = Email

    @property
    def code_city(self):
        return self.__code_city
    @code_city.setter
    def code_city(self , Code_city):
        self.__code_city = Code_city

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self , Type):
        self.__type = Type

    def __str__(self):
        return f'{self.id}{self.name}{self.phone_number}{self.email}{self.code_city}'

#ارث می‌برد Information که برای اشخاص حقیقی است و از کلاس  Haghighi تعریف یک کلاس به نام 
class Haghighi (Information):
    def __init__(self, id, name, family , relation ,
                  phone_number, email, code_city , type):
        super().__init__(id, name, phone_number,
                          email, code_city , type)
        self.__family = family
        self.__relation = relation

    # استفاده از پراپرتی مقادیر پرایوت بالا
    @property
    def family(self):
        return self.__family
    @family.setter
    def family(self , lname):
        self.__family = lname

    @property
    def relation(self):
        return self.__relation
    @relation.setter
    def relation (self , Relation):
        self.__relation = Relation

    def __str__(self):
        return f'{self.id:<5}{self.name:<15}{self.family:<15}{self.relation:<15}{self.phone_number:<15}{self.email:<20}{self.code_city:<11}'
    
#ارث می‌برد Information که برای اشخاص حقوقی است و از کلاس  Hoghighi تعریف یک کلاس به نام        
class Hoghoghi (Information):
    def __init__(self, id, name, phone_number, email,fax_number , address , code_city, type ):
        super().__init__(id, name, phone_number,email, code_city , type )
        self.__fax_number = fax_number
        self.__address = address

    # استفاده از پراپرتی مقادیر پرایوت بالا
    @property
    def fax_number(self):
        return self.__fax_number
    @fax_number.setter
    def fax_number(self , Fax_number):
        self.__fax_number = Fax_number

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self , Address):
        self.__address = Address
    
    def __str__(self):
        return f'{self.id:<5}{self.name:<20}{self.phone_number:<15}{self.email:<20}{self.fax_number:<15}{self.address:<25}{self.code_city:<11}'

# برای نوشتن آپشن های برنامه Phone_book تعریف یک کلاس به نام 
class Phone_book:
    def __init__(self):
        self.contact_list = []

    # تعریف یک تابع برای اضافه کردن مخاطبان به لیست
    def append_contact_list(self , contact):
        self.contact_list.append(contact)
    
    # تعریف یک تابع برای نمایش مخاطبان به سه مدل مختلف
    def show_contact_list(self):
        print('1-Show all contact')
        print('2-Show haghighi contact')
        print('3-Show hoghoghi contact')
        show_contact_list_user_choice=input('Please choice a number : ')
        system('cls')
        match show_contact_list_user_choice:
            case '1':
                if not self.contact_list:
                    print('There are no contacts ')
                    input('Press to contniue')
                else:
                    for all in self.contact_list:
                        if all.type == 'ha':
                            print(f'{'ID :'}{all.id:<5}{'NAME :'}{all.name:<10}{'FAMILY :'}{all.family:<15}{'RELATION :'}{all.relation:<15}{'PHONE NUMBER :'}{all.phone_number:<13}{'EMAIL :'}{all.email:<20} {'CODE CITY :'}{all.code_city:<4}')
                            
                        if all.type == 'ho':
                            print(f'{'ID :'}{all.id:<5}{'TItle :'}{all.name:<10}{'PHONE NUMBER :'}{all.phone_number:<13}{'EMAIL :'}{all.email:<20}{'FAX NUMBER :'}{all.fax_number:<13}{'ADDRESS :'}{all.address:<20}{'CODE CITY :'}{all.code_city:<4}')
                    input('Press to continue ')
            case '2':
                if not self.contact_list:
                    print('There are no contacts ')
                    input('Press to contniue')
                else:
                    print(f'{'ID':<5}{'NAME':<15}{'FAMILY':<15}{'RELATION':<15}{"PHONE NUMBER":<15}{'EMAIL':<20}{'CODE CITY':<11}')
                    print(96 * '=')
                    for show_ha in self.contact_list:
                        if show_ha.type == 'ha':
                            print(show_ha)
                    input('Press to contniue')
            case '3':
                if not self.contact_list:
                    print('There are no contacts ')
                    input('Press to contniue')
                else:
                    print(f'{'ID':<5}{'TITLE':<20}{'PHONE NUMBER':<15}{'EMAIL':<20}{'FAX NUMBER':<15}{'ADDRESS':<25}{'CODE CITY':<11}')
                    print(111 * '=') 
                    for show_ho in self.contact_list:
                        if show_ho.type == 'ho':
                            print(show_ho)
                    input('Press to contniue')
            case '_':
                print('invalid number try again ......')
    
    # صورت میگیرد ID تعریف یک تابع برای برای ادیت کردن اطلاعات مخاطبان که پیدایش مخاطب توسط 
    def edit_contact_list(self):
        p = False
        try:search_id_to_edit = int(input('Enter ypur desired ID : '))
        except ValueError:
            print('ERORR : Please Enter digit')
            p = True
            input('Press for continue ')
        system('cls')
        for person in self.contact_list : 
            if person.type == 'ha' and search_id_to_edit == person.id:
                print(f'{'ID':<5}{'NAME':<15}{'FAMILY':<15}{'RELATION':<15}{"PHONE NUMBER":<15}{'EMAIL':<20}{'CODE CITY':<11}')
                print(96 * '=')
                print(person)
                name = input('New name :')
                family = input('New family :')
                relation = input('New relation :')
                while True:
                    phone_number = input('Mobile Phone Number : ')
                    if check_number_haghighi(phone_number):
                        break
                    else:
                        input('Mobile number is 11 digits ')
                        continue 
                email = input('New email :')
                code_city = input('New code city :')
                person.name = name
                person.family = family
                person.relation = relation
                person.phone_number = phone_number
                person.email = email
                person.code_city = code_city
                system('cls')
                print('New information saved')
                input('Press for continue ')
                p=True
                print()
            elif person.type == 'ho' and search_id_to_edit == person.id:
                print(f'{'ID':<5}{'TITLE':<20}{'PHONE NUMBER':<15}{'EMAIL':<20}{'FAX NUMBER':<15}{'ADDRESS':<25}{'CODE CITY':<11}')
                print(111 * '=') 
                print(person)
                title = input('New title :')
                while True:
                    phone_number = input('Phone Number : ')
                    if check_number_hoghoghi(phone_number):
                        break
                    else:
                        input('Phone number is 8 digits')
                        continue
                ho_email = input('New email :')
                fax = input('New fax number :')
                address = input('New address :')
                ho_code_city = input('New code city :')
                person.name = title
                person.phone_number = phone_number 
                person.email = ho_email
                person.fax_number = fax
                person.address = address
                person.code_city = ho_code_city
                system('cls')
                print('New information saved')
                input('Press for continue ')
                p=True 
                print() 
        if p :
            pass
        else :
            print('Contact not found ')
            input('Press to continue ')

    # ID تعریف یک تابع برای جستجوی مخاطبان از طریق 
    def search_id_contact_list(self):
        p = False
        try:search_id = int(input('Enter ypur desired ID : '))
        except ValueError:
            print('ERORR : Please Enter digit')
            p = True
            input('Press for continue ')
        system('cls')
        for person in self.contact_list :
            if person.id == search_id :
                if person.type == 'ha':
                    print(f'{'ID':<5}{'NAME':<15}{'FAMILY':<15}{'RELATION':<15}{"PHONE NUMBER":<15}{'EMAIL':<20}{'CODE CITY':<11}')
                    print(96 * '=')
                    print(person)
                    p = True
                elif person.type == 'ho':
                    print(f'{'ID':<5}{'TITLE':<20}{'PHONE NUMBER':<15}{'EMAIL':<20}{'FAX NUMBER':<15}{'ADDRESS':<25}{'CODE CITY':<11}')
                    print(111 * '=') 
                    print(person)
                    p = True
                input('Press to contniue')
        if p:
            pass
        else:
            system('cls')
            print('Contact not found')
            input('Press for continue ')

    # صورت میگیرد ID تعریف یک تابع برای حذف مخاطب که پیدایش مخاطب از طریق 
    def remove_contact_list(self):
        p = False
        try:search_id_to_delete = int(input('Enter ypur desired ID : ')) 
        except ValueError:
            print('ERORR : Please Enter digit')
            p = True 
            input('Press for continue ')
        system('cls') 
        for person in self.contact_list :
            if person.id == search_id_to_delete :
                if person.type == 'ha':
                    print(f'{'ID':<5}{'NAME':<15}{'FAMILY':<15}{'RELATION':<15}{"PHONE NUMBER":<15}{'EMAIL':<20}{'CODE CITY':<11}')
                    print(96 * '=')
                    p = True
                    print(person)
                elif person.type == 'ho':
                    print(f'{'ID':<5}{'TITLE':<20}{'PHONE NUMBER':<15}{'EMAIL':<20}{'FAX NUMBER':<15}{'ADDRESS':<25}{'CODE CITY':<11}')
                    print(111 * '=') 
                    print(person)
                    p = True
                question_to_delete = input('Are you sure to delete (YES/No) ? ').lower()
                match question_to_delete:
                    case 'yes':
                        system('cls')
                        self.contact_list.remove(person)
                        print('Contact deleted')
                        input('Press for continue ')
                    case 'no':
                        input('Press for continue ')
        if p:
            pass
        else:
            system('cls')
            print('Contact not found !')
            input('Press to continue ')
        
    # Phone book تعریف یک تابع برای ذخیره اطلاعات مخاطبان در فایلی به نام 
    def save_to_file(self):
        with open('Phone book.txt' , 'a') as file:
            for contact in self.contact_list:
                    file.write(str(contact) + '\n') 
        print(f"Contacts saved to Phone book.txt")

# تعریف تابع برای گرفتن اطلاعات مخاطبان حقیقی
haghighi_id_generator_var = haghighi_id_generator()
def haghighi_insert_info():
    print("Please Complete the information :")
    id = next(haghighi_id_generator_var)
    name = input('Name : ')
    family = input('Family : ')
    relation = input('Relation : ')
    while True:
        phone_number = input('Mobile Phone Number : ')
        check_number_haghighi(phone_number)
        if check_number_haghighi(phone_number):
            break
        else:
            input('Mobile number is 11 digits ')
            continue 
    email = input('Email : ')
    code_city = input('Code City : ')
    type = 'ha'
    system('cls')
    print(f'ID : {id} , NAME : {name} , FAMILY : {family} , RELATION : {relation} ,PHONE NUMBER : {phone_number} , EMAIL : {email} , CODE CIty : {code_city}')
    haghighi_confirm_user_choice = input('do you confirm the information (YES/NO) ? ').lower()
    if haghighi_confirm_user_choice == 'yes':
        system('cls')
        print('Your information has been saves ')
        input('Press to continue ')
        return Haghighi( id , name , family , relation ,phone_number , email , code_city , type)
    elif haghighi_confirm_user_choice == 'no':
        system('cls')
        print('Your information was not saved')
        input('press for continue ')

# تعریف تابع برای گرفتن اطلاعات مخاطبان حقوقی
hoghoghi_id_generator_var = hoghoghi_id_generator()
def hoghoghi_insert_info():
    print("Please Complete the information :")
    id = next(hoghoghi_id_generator_var)
    title  = input('Title : ')
    while True:
        phone_number = input('Phone Number : ')
        check_number_hoghoghi(phone_number)
        if check_number_hoghoghi(phone_number):
            break
        else:
            input('Phone number is 8 digits') 
    email = input ('Email : ')
    fax_number = input ('Fax Number : ')
    address = input('Address : ')
    code_city = input ('Code city : ')
    type = 'ho'
    system('cls')
    print(f'ID : {id} , NAME : {title} , PHONE NUMBER : {phone_number} ,EMAIL : {email} , FAX NUMBER : {fax_number} ,ADDRESS : {address}, CODE CIty : {code_city}')
    hoghighi_confirm_user_choice = input('do you confirm the information (YES/NO) ? ').lower()
    if hoghighi_confirm_user_choice == 'yes':
        system('cls')
        print('Your information has been saved ')
        input('Press to continue ')
        return Hoghoghi(id , title , phone_number , email ,fax_number , address , code_city , type)
    elif hoghighi_confirm_user_choice == 'no':
        system('cls')
        print('Your information was not saved ') 
        input('press for continue')

# (مربوط به اطلاعات حقیقی)تعریف تابع برای بررسی شماره تلفن همراه 
def check_number_haghighi(number=''):
    if len(number) == 11 and number.isdigit():
        check = True
    else :
        check = False
    return check

# (مربوط به اطلاعات حقوقی)تعریف تابع برای بررسی شماره تلفن ثابت   
def check_number_hoghoghi(number=''):
    if len(number) == 8 and number.isdigit():
        check = True
    else:
        check = False
    return check

#ایجاد یک شی
phonebook = Phone_book()

#تعریف تابع برای منو و اجرای برنامه
def program():
    system('cls')
    while True:
        print('-----Phone Book-----')
        print('1-Insert Information')
        print('2-Show Contact')
        print('3-Edit Contact')
        print('4-Search Contact')
        print('5-Delete Contact')
        print('6-Exit')
        program_user_choice = input('Plaese choice a number : ')
        match program_user_choice:
            case '1':
                system('cls')
                insert_info_user_choice = input('Please enter your contact type (HA/HO & for exit X) : ').lower()
                system('cls')
                match insert_info_user_choice:
                    case 'ha':
                        hoghoghi_person_var = haghighi_insert_info()
                        phonebook.append_contact_list(hoghoghi_person_var)
                    case 'ho':
                        haghighi_person_var = hoghoghi_insert_info()
                        phonebook.append_contact_list(haghighi_person_var)
                system('cls')
            case '2':
                system('cls')
                phonebook.show_contact_list()
                system('cls')
            case '3':
                system('cls')
                phonebook.edit_contact_list()
                system('cls')
            case '4':
                system('cls')
                phonebook.search_id_contact_list()
                system('cls')
            case '5':
                system('cls')
                phonebook.remove_contact_list()
                system('cls')
            case '6':
                system('cls')
                save_choice = input("Do you want to save the contactsbefore exiting (YES/NO) ?: ").lower()
                system('cls')
                if save_choice == 'yes':
                    phonebook.save_to_file()
                    print('Good bye')
                    break
                elif save_choice == 'no' :
                    print('Good bye')
                    break
            case '_':
                input('Invalid number plaese try again ....')
                continue

# اجرای کامل برنامه 
if __name__ == "__main__":
    program()

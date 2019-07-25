from contactclass import Contact
from beautifultable import BeautifulTable

class InMemoryImpl:
    contacts = []

    @classmethod
    def addContact(cls):
        name=input("Enter the name?")
        email=input("Enter the email?")
        mobile=input("Enter the mobile?")
        address=input("Enter the address")
        cls.contacts.append(Contact(name,email,mobile,address))
        print("Contact is added Successfully!")

    @classmethod
    def deleteContact(cls):
        name=input("Enter the name to delete:")
        data=cls.get_contact_by_name(name)
        if data:
            cls.contacts.remove(data)
            print("Contact Deleted Successfully...")
        else:
            print(f"Contact with name {name} is not found!")

    @classmethod
    def viewContact(cls):
        InMemoryImpl._paint(cls.contacts)
    
    @classmethod
    def search(cls):
        if (len(cls.contacts)) >0:
            name=input("Enter the name to search:")
            s_list=list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contacts))  
            if len(s_list) > 0:
                InMemoryImpl._paint(s_list)
            else:
                print(f"Sorry, no such contact exist...")      
        else:
            print(f"Contact Book is Empty")

    @classmethod
    def get_contact_by_name(cls,name):
        if len(cls.contacts)>0:
            contactt=list(filter(lambda x:x.get__name().lower()==name.lower(),cls.contacts))
            return contactt[0] if contactt else None

    @classmethod    
    def updateContact(cls):
        name=input("Enter the name to be updated")
        data=cls.get_contact_by_name(name)
        if data:
            print("1.New Name 2.New Email 3.New Mobile 4.New Address")
            ch=int(input("Enter your choice?"))
            if ch==1:
                print(f"Old name:{data.get__name()}")
                name=input("Enter the new Name:")
                if name:
                    data.set__name(name)
            elif ch==2:
                print(f"Old Email:{data.get__email()}")
                email=input("Enter the new Email:")
                if email:
                    data.set__email(email)
            elif ch==3:
                print(f"Old Mobile:{data.get__mobile()}")
                mobile=input("Enter the new Mobile:")
                if mobile:
                    data.set__mobile(mobile)
            else:
                print(f"Old Address:{data.get__address()}")
                address=input("Enter the new Address:")
                if address:
                    data.set__address(address)
        else:
            print(f"Contact with name:{name} not found...")
            


    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table=BeautifulTable()
            table.column_headers=['Name','Email','Mobile','Address']
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])
            print(table)
        else:
            print(f"Contact book is empty!")


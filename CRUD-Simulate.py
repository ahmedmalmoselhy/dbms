created_databases = []
created_tables = []
colNumber = 1

class Database:
    def __init__(self , name):
        self.name = name
        created_databases.append(self.name)
        #open the file handler
        fh = open(str(self.name + ".txt"),"w")
        fh.write("Database {} Created Successfully\n".format(self.name))
        fh.close()
    def addTable(self , tableName , firstCol , *args):
        colNumber = len(args) + 1
        # Create a table
        self.tableName = tableName
        self.firstCol = firstCol
        created_tables.append(self.tableName)
        fh = open(str(self.name+".txt") , "a")
        fh.write(str("Table [ "+self.tableName+" ] Created Successfully\n"))
        fh.write("---------------------------------------------\n")
        # add columns
        fh.write(str(self.firstCol))
        for i in args:
            fh.write("\t\t")
            fh.write(i)

        fh.write("\n")
        fh.close()

    def removeTable(self , tableName):
        self.tableName = tableName
        if self.tableName not in created_tables :
            print("No Table With This Name ! ")
        else :
            print("Removed Successfully ! ")


    def addRecord(self, *args):
        # Check if data entered = number of columns in the table
        if args.__len__() < colNumber:
            print("Error in Entering Data")
        else:
            # adding data inside the table
            fh = fh = open(str(self.name+".txt") , "a")
            for i in args:
                fh.write(i)
                fh.write("\t\t\t")
            fh.write("\n")
            fh.close()


    def clearFile(self):
        fh = open(str(self.name+".txt"),'w')
        fh.write("")
        fh.close()

    def removeRecord(self, fname):
        fh = open(str(self.name+".txt"), "r")
        mydata = fh.read()
        lines = mydata.split("\n")
        fh.close()
        initials = []
        initials.append(lines.pop(0))
        initials.append(lines.pop(0))
        initials.append(lines.pop(0))
        initials.append(lines.pop(0))
        lines.pop()
        # print(lines)
        for line in lines:
            if line.startswith(fname):
                lines.pop(lines.index(line))

        students.clearFile()
        fh = open(str(self.name + ".txt"), "w")
        for line in initials:
            fh.write(line)
            fh.write("\n")

        for line in lines:
            fh.write(line)
            fh.write("\n")
        print("Record Removed Successfully!")



students = Database("students")

def recordAdding():
    firstname = input("Enter The First Name : ")
    lastname = input("Enter The Last Name : ")
    dep = input("Enter Department : ")
    phone = input("Enter Phone Number : ")

    students.addRecord(firstname,lastname,dep,phone)


# testing

# students.addTable("names" , "First_Name" , "Second_Name" , "Department" , "Phone_Number")
# students.removeTable("names")
# students.addRecord("Ahmed", "Hani", "CSED", "11111")
# students.addRecord("Ali", "Adel", "ECED", "25556")

print("Please select an option to continue\n")
print("1) Add a table\n2) Add a record\n3) Clear the whole file\n4) Delete a record\nEND) Close app")
while True:
    opt = input("Inter A Number : ")
    if opt == '1':
        students.addTable("names", "First_Name", "Second_Name", "Department", "Phone_Number")
        print("Table added successfully")
    elif opt == '2':
        # students.addRecord("Ahmed", "Hani", "CSED", "11111")
        recordAdding()
        print("Record added successfully")
    elif opt == '3':
        students.clearFile()
        print("File cleared successfully")
        students = Database("students")
    elif opt == '4':
        f_name = input("Enter The First Name of The Record You Want To Delete : ")
        students.removeRecord(f_name)
    elif opt.upper() == "END":
        break
    else:
        print("Wrong Input, Try Again")

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

    def clearFile(self):
        fh = open(str(self.name+".txt"),'w')
        fh.write("")
# testing
students = Database("students")
# students.addTable("names" , "First_Name" , "Second_Name" , "Department" , "Phone_Number")
# students.removeTable("names")
# students.addRecord("Ahmed", "Hani", "CSED", "11111")
# students.addRecord("Ali", "Adel", "ECED", "25556")

print("Please select an option to continue\n")
print("1) Add a table\n2)Add a record\n3)Clear the whole file")
while True:
    opt = input("Inter A Number \t\t:")
    if opt == '1':
        students.addTable("names", "First_Name", "Second_Name", "Department", "Phone_Number")
        print("Table added successfully")
    elif opt == '2':
        students.addRecord("Ahmed", "Hani", "CSED", "11111")
        print("Record added successfully")
    elif opt == '3':
        students.clearFile()
        print("File cleared successfully")
        students = Database("students")
    else:
        print("Wrong Input, Try Again")

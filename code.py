created_databases = []
created_tables = []

class Database:
    def __init__(self , name):
        self.name = name
        created_databases.append(self.name)
        fh = open(str(self.name + ".txt"),"w")
        fh.write("Database {} Created Successfully\n".format(self.name))
        fh.close()
    def addTable(self , tableName , firstCol , *args):
        self.tableName = tableName
        self.firstCol = firstCol
        created_tables.append(self.tableName)
        fh = open(str(self.name+".txt") , "a")
        fh.write(str("Table [ "+self.tableName+" ] Created Successfully\n"))
        fh.write("---------------------------------------------\n")
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


# testing
students = Database("students")
students.addTable("names" , "First_Name" , "Second_Name" , "Department" , "Phone_Number")
students.removeTable("namexxxs")

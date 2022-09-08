import mysql.connector





def executeScriptsFromFile(filename, connection):
    # Open and read the file as a single buffer
    with open(filename, "r") as fd:
        sqlFile = " ".join(fd.readlines())

    cursor = connection.cursor()
    cursor.execute(sqlFile)




    cursor.execute("SHOW TABLES")


    # Execute every command from the input file
    for command in sqlFile:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
        except IOError , msg:
            print "Command skipped: ", msg


    connection.close()



executeScriptsFromFile("Data1/Course_Material_Part2/Video_Lecture_NBs/HousingDB17092019.sql")
connection.commit()





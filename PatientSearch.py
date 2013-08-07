print ("\n" * 100)
resetcommand = "nothing"
while resetcommand != "exit":
    nurseext = "661-775-1500"
    print ('Welcome to the Nexus Patient Locator')
    patientname = input('Please enter the name of the Patient you are looking for: ')
    found_patient_name=False
    with open('testdata.txt', 'r') as searchfile:
                for line in searchfile:
                    if patientname in line:
                        found_patient_name=True
                        nurseext = line[-11:]
                        my_url="http://patient-name-lookup.healthcare.com?patientID="+str(nurseext)
                        print (' ')
                        print(my_url)
                        print ('Please dial the following extension: '+str(nurseext))

                if not found_patient_name:
                    print ("\n")
                    print   ("Sorry, we cannot find the Droid you are looking for. Maybe call 1-800-Sir-Mix-A-Lot?")
                    print ("\n")
                    print ('Please dial the following number: '+str(nurseext))
                    print ("\n")
    resetcommand = input("Press Enter when complete or to search again.")
    print ("\n" * 100)


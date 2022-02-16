import pandas as pd
import Femut as ft

count = 0

Number_list = []
Sex_list = []
Length_list = []
Pearson_male_list = []
TnG_male_list = []
Huzii_male_list = []
Pearson_female_list = []
Huzii_female_list = []

#First Page
print("""
   ___                    _   
  / __\__ _ __ ___  _   _| |_ 
 / _\/ _ \ '_ ` _ \| | | | __|
/ / |  __/ | | | | | |_| | |_ 
\/   \___|_| |_| |_|\__,_|\__|
                              
""")

while True : 
    print("Male : 1\nFemale : 2\nExit : 3")
    print(" ")
    Sex = input(">>> ")
    print(" ")
    if Sex == '1': #Male
        print("""
        You choose a Male
        You can use Pearson formula, Trotter&Glaser formula, Huzii formula
        Enter to 0, you go to First Page

        """)
        while True:
            Length = float(input("Input the femur length >>> "))
            if Length > 0:
                male_Pearson = ft.pearson(Length, Sex='Male')
                male_TnG = ft.tng(Length)
                male_Huzii = ft.huzii(Length, Sex='Male')

                count += 1

                print("- Pearson formula : %0.3fcm" % male_Pearson)
                print("- Huzii formula : %0.3fcm" % male_Huzii)
                print("- Trotter&Glaser formula : %0.3fcm" % male_TnG)
                print(" ")

                Number_list.append(count)
                Sex_list.append("Male")
                Length_list.append(Length)
                Pearson_male_list.append(male_Pearson)
                Huzii_male_list.append(male_Huzii)
                TnG_male_list.append(male_TnG)
                Pearson_female_list.append('')
                Huzii_female_list.append('')

            elif Length == 0 :
                print("""

        Go to First Page

                """)
                break

            else :
                pass

    elif Sex == '2': #Female
        print("""

        You choose a Female
        You can use Pearson formula, Huzii formula
        Enter to 0, you go to First Page

        """)
        while True:
            Length = float(input("Input the femur length >>> "))
            if Length > 0:
                female_Pearson = ft.pearson(Length, Sex='Female')
                female_Huzii = ft.huzii(Length, Sex='Male')

                count += 1

                print("- Pearson formula : %0.3fcm"  % female_Pearson)
                print("- Huzii formula : %0.3fcm" % female_Huzii)
                print(" ")

                Number_list.append(count)
                Sex_list.append("Female")
                Length_list.append(Length)
                Pearson_female_list.append(female_Pearson)
                Huzii_female_list.append(female_Huzii)
                Pearson_male_list.append('')
                TnG_male_list.append('')
                Huzii_male_list.append('')

            elif Length == 0 :
                print("""

        Go to First Page

                """)
                break

            else :
                pass
            
    elif Sex == '3': #Exit
        result_dict = dict(
            num = Number_list,
            Sex = Sex_list,
            Femur_Length = Length_list,
            Male_Pearson = Pearson_male_list,
            Male_Huzii = Huzii_male_list,
            Male_TG = TnG_male_list,
            Female_Pearson = Pearson_female_list,
            Female_Huzii = Huzii_female_list
        )
        savename = "Result"
        csv_Name = "./{}.csv".format(savename)
        xlsx_Name = "./{}.xlsx".format(savename)

        DB = pd.DataFrame(result_dict)
        DB.to_csv(csv_Name)
        DB.to_excel(xlsx_Name)

        print("""
        Exit

        """)
        break

    else: #Error
        print("""
        Error
        
        """)
        pass

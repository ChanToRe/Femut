import pandas as pd

#Male
def M_pearson(number):
    result = 81.306 + 1.880 * number
    return result

def M_Trotter(number):
    result = 2.15 * number + 72.57
    return result

def M_huzii(number):
    result = (2.47 * (number*10) + 549.01)/10
    return result

#Female
def F_pearson(number):
    result = 72.844 + 1.945 * number
    return result

def F_huzii(number):
    result = (2.24 * (number*10) + 610.43)/10
    return result

count = 0

Number = []
Sexe = []
Femur_Length = []
M_PF = []
M_HF = []
M_TGF = []
F_PF = []
F_HF = []

#First Page
print("="*30)
print("="*9 + "femurtotall" + "="*10)
print("="*30)
print(" ")

while True : 
    print("Male : 1\nFemale : 2\nExit : 3")
    print(" ")
    Sex = input(">>> ")
    print(" ")
    if Sex == '1': #Male
        print("You choose a Male")
        print("You can use Pearson formula, Trotter&Glaser formula, Huzii formula")
        print("Enter to 0, you go to First Page")
        print(" ")
        while True:
            femur = float(input("Input the femur length >>> "))
            if femur != 0:
                MP = M_pearson(femur)
                MT = M_Trotter(femur)
                MH = M_huzii(femur)

                count += 1

                print("- Pearson formula : %0.3fcm" % MP)
                print("- Huzii formula : %0.3fcm" % MH)
                print("- Trotter&Glaser formula : %0.3fcm" % MT)
                print(" ")

                Number.append(count)
                Sexe.append("Male")
                Femur_Length.append(femur)
                M_PF.append(MP)
                M_HF.append(MH)
                M_TGF.append(MT)
                F_PF.append('')
                F_HF.append('')

            elif femur == 0 :
                print(" ")
                print("=" * 30)
                print("=" * 2 + "Go to First Page" + "=" * 2)
                print("=" * 30)
                print(" ")
                break

    elif Sex == '2': #Female
        print("You choose a Female")
        print("You can use Pearson formula, Huzii formula")
        print("Enter to 0, you go to First Page")
        print(" ")
        while True:
            femur = float(input("Input the femur length >>> "))
            if femur != 0:
                FP = F_pearson(femur)
                FH = F_huzii(femur)

                count += 1

                print("- Pearson formula : %0.3fcm"  % FP)
                print("- Huzii formula : %0.3fcm" % FH)
                print(" ")

                Number.append(count)
                Sexe.append("Female")
                Femur_Length.append(femur)
                F_PF.append(FP)
                F_HF.append(FH)
                M_PF.append('')
                M_HF.append('')
                M_TGF.append('')

            elif femur == 0 :
                print(" ")
                print("=" * 30)
                print("=" * 2 + "Go to First Page" + "=" * 2)
                print("=" * 30)
                print(" ")
                break
            
    elif Sex == '3': #Exit
        result_dict = dict(
            num = Number,
            Sex = Sexe,
            Femur_Length = Femur_Length,
            Male_Pearson = M_PF,
            Male_Huzii = M_HF,
            Male_TG = M_TGF,
            Female_Pearson = F_PF,
            Female_Huzii = F_HF
        )
        savename = "Result"
        csv_Name = "~/Desktop/{}.csv".format(savename)
        xlsx_Name = "~/Desktop/{}.xlsx".format(savename)

        DB = pd.DataFrame(result_dict)
        DB.to_csv(csv_Name)
        DB.to_excel(xlsx_Name)

        print("="*30)
        print("="*11 + "Exit" + "="*10)
        print("="*30)
        print(" ")
        break

    else: #Error
        print(" ")
        print("Error")
        print(" ")

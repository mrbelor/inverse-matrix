# -*- coding: utf8 -*- 
# Эта программа вычисляет обратную матрицу 9 на 9 к данной и показывает решение
print("Эта программа вычисляет обратную данной матрицу 9 на 9 и показывает решение\n    ⎡🞎🞎🞎⎦\nA = ⎡🞎🞎🞎⎤\n    ⎣🞎🞎🞎⎦")
run = True
while run:
    A = input("Введите элементы матрицы по книжному порядку через точки,запятые или пробелы (9 штук)\nНапример: -1 -7 10 -1 8 8 9 1 1\n")
    A = A.replace(",", " ")
    A = A.replace(".", " ")
    A = A.split()

    # проверка 1
    if len(A) != 9:
        print("\nВы ввели ошибочное количество элементов!")
        continue
    # проверка 2
    StrA = ""
    for i in A:
        StrA += i
    StrA = StrA.replace("-", "")
    if not StrA.isdigit():
        print("\nВ списке должны быть только цифры!")
        continue
    
    # --------ЭТАП1--------
    print("\n1)Посчитаем определитель")
    opred_A = (int(A[0])*int(A[4])*int(A[8])+int(A[1])*int(A[5])*int(A[6])+int(A[3])*int(A[2])*int(A[7])-int(A[6])*int(A[4])*int(A[2])-int(A[1])*int(A[3])*int(A[8])-int(A[0])*int(A[5])*int(A[7]))

    # сделаем чтобы отрицательные числа в скобочки заключались
    output_A = []
    for i in A:
        if int(i) < 0:
            output_A.append("("+i+")")
        else:
            output_A.append(i)
    # вывод решения
    print("{}*{}*{} + {}*{}*{} + {}*{}*{} - {}*{}*{} - {}*{}*{} - {}*{}*{} = {}\n".format(output_A[0], output_A[4], output_A[8], output_A[1], output_A[5], output_A[6], output_A[3], output_A[2], output_A[7], output_A[6], output_A[4], output_A[2], output_A[1], output_A[3], output_A[8], output_A[0], output_A[5], output_A[7], opred_A))

    # --------ЭТАП2--------
    print("2)Равен ли определитель 0?")
    if opred_A != 0:
        print(opred_A, "≠ 0  Это значит что всё хорошо\n")
    else:
        input("Да, определитель твоей матрицы равен 0.\nВроде как это значит что обратной матрицы не существует..\nНа этом мои полномочия всё.")
        quit()
    # --------ЭТАП3--------
    print("3)Считаем D строки\n")
    output = []
    for i in A:
        if int(i) < 0:
            output.append(i)
        else:
            output.append(" "+i)
    
    D11 = (int(A[4])*int(A[7])-int(A[5])*int(A[8]))*(-1)**2
    D12 = (int(A[3])*int(A[8])-int(A[5])*int(A[6]))*(-1)**3
    D13 = (int(A[3])*int(A[7])-int(A[4])*int(A[6]))*(-1)**4

    D21 = (int(A[1])*int(A[8])-int(A[2])*int(A[7]))*(-1)**3
    D22 = (int(A[0])*int(A[8])-int(A[2])*int(A[6]))*(-1)**4
    D23 = (int(A[0])*int(A[7])-int(A[1])*int(A[6]))*(-1)**5

    D31 = (int(A[1])*int(A[5])-int(A[2])*int(A[4]))*(-1)**4
    D32 = (int(A[0])*int(A[5])-int(A[2])*int(A[3]))*(-1)**5
    D33 = (int(A[0])*int(A[4])-int(A[1])*int(A[3]))*(-1)**6

    print("D₁₁=(-1)²({} {}) = {}\n         ({} {})".format(output[4], output[5], D11, output[7], output[8]))
    print("D₁₂=(-1)³({} {}) = {}\n         ({} {})".format(output[3], output[5], D12, output[6], output[8]))
    print("D₁₃=(-1)⁴({} {}) = {}\n         ({} {})\n".format(output[3], output[4], D13, output[6], output[7]))
    
    print("D₂₁=(-1)³({} {}) = {}\n         ({} {})".format(output[1], output[2], D21, output[7], output[8]))
    print("D₂₂=(-1)⁴({} {}) = {}\n         ({} {})".format(output[0], output[2], D22, output[6], output[8]))
    print("D₂₃=(-1)⁵({} {}) = {}\n         ({} {})\n".format(output[0], output[1], D23, output[6], output[7]))

    print("D₃₁=(-1)⁴({} {}) = {}\n         ({} {})".format(output[1], output[2], D31, output[4], output[5]))
    print("D₃₂=(-1)⁵({} {}) = {}\n         ({} {})".format(output[0], output[2], D32, output[3], output[5]))
    print("D₃₃=(-1)⁶({} {}) = {}\n         ({} {})\n".format(output[0], output[1], D33, output[3], output[4]))
   
    # --------ЭТАП4--------
    print("4)Вставляем D элементы в матрицу\n")
    Dmat = []
    Dmat.append(D11)
    Dmat.append(D12)
    Dmat.append(D13)
    Dmat.append(D21)
    Dmat.append(D22)
    Dmat.append(D23)
    Dmat.append(D31)
    Dmat.append(D32)
    Dmat.append(D33)

    output = []
    for i in Dmat:
        if len(str(i)) == 1:
            output.append("   "+str(i))
        elif len(str(i)) == 2:
            output.append("  "+str(i))
        elif len(str(i)) == 3:
            output.append(" "+str(i))
        else:
            output.append(str(i))    
    
    print("({} {} {})\n|{} {} {}|\n({} {} {})\n".format(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8]))
    # --------ЭТАП5--------
    print("5)Трансформируем полученную матрицу")
    At = []
    At.append(Dmat[0])
    At.append(Dmat[3])
    At.append(Dmat[6])
    At.append(Dmat[1])
    At.append(Dmat[4])
    At.append(Dmat[7])
    At.append(Dmat[2])
    At.append(Dmat[5])
    At.append(Dmat[8])

    output = []
    for i in At:
        if len(str(i)) == 1:
            output.append("   "+str(i))
        elif len(str(i)) == 2:
            output.append("  "+str(i))
        elif len(str(i)) == 3:
            output.append(" "+str(i))
        else:
            output.append(str(i))    
    
    print("     ({} {} {})\nAᵗ = ({} {} {})\n     ({} {} {})\n".format(output[0], output[1], output[2], output[3], output[4], output[5], output[6], output[7], output[8]))
    # --------ЭТАП6--------
    print("6)Находим обратную матрицу")
    print("A⁻¹ = 1/|A|")
    print(" "*(9+len(str(opred_A)))+"({} {} {})\n".format(output[0], output[1], output[2])+"A⁻¹ = 1/{}*|{} {} {}|\n".format(opred_A,output[3], output[4], output[5])+" "*(9+len(str(opred_A)))+"({} {} {})\n".format(output[6], output[7], output[8]))
    print("     ({}/{} {}/{} {}/{})\nAᵗ = ({}/{} {}/{} {}/{})\n     ({}/{} {}/{} {}/{})\n".format(output[0], opred_A, output[1], opred_A, output[2], opred_A, output[3], opred_A, output[4], opred_A, output[5], opred_A, output[6], opred_A, output[7], opred_A, output[8], opred_A))
    print("Ответ ↑\n")
    print("Здесь можно матрицу выше прогнать через программу \"Photomath\" и упростить её\n")
    # ------ЭТАП1(Проверка)--------
    print("1)ПРОВЕРКА")
    print("A*A⁻¹ = E")
    # сделаем чтобы отрицательные числа в скобочки заключались
    output = []
    for i in At:
        if int(i) < 0:
            output.append("("+str(i)+")")
        else:
            output.append(str(i))
    print("Каждая строка - элемент еденичной матрицы")
 
    print("{}*{}+{}*{}+{}*{} / {}".format(output[0], output_A[0], output[3], output_A[1], output[6], output_A[2], opred_A))
    print("{}*{}+{}*{}+{}*{} / {}".format(output[1], output_A[0], output[4], output_A[1], output[7], output_A[2], opred_A))
    print("{}*{}+{}*{}+{}*{} / {}\n".format(output[2], output_A[0], output[5], output_A[1], output[8], output_A[2], opred_A))

    print("{}*{}+{}*{}+{}*{} / {}".format(output[0], output_A[3], output[3], output_A[4], output[6], output_A[5], opred_A))
    print("{}*{}+{}*{}+{}*{} / {}".format(output[1], output_A[3], output[4], output_A[4], output[7], output_A[5], opred_A))
    print("{}*{}+{}*{}+{}*{} / {}\n".format(output[2], output_A[3], output[5], output_A[4], output[8], output_A[5], opred_A))

    print("{}*{}+{}*{}+{}*{} / {}".format(output[0], output_A[6], output[3], output_A[7], output[6], output_A[8], opred_A))
    print("{}*{}+{}*{}+{}*{} / {}".format(output[1], output_A[6], output[4], output_A[7], output[7], output_A[8], opred_A))
    print("{}*{}+{}*{}+{}*{} / {}\n".format(output[2], output_A[6], output[5], output_A[7], output[8], output_A[8], opred_A))
    # ------ЭТАП2(Проверка)--------
    print("2)ПРОВЕРКА")
    print("Каждая строка - элемент еденичной матрицы\n")

    print("{}+{}+{} / {}".format(int(At[0])*int(A[0]), int(At[3])*int(A[1]), int(At[6])*int(A[2]), opred_A))
    print("{}+{}+{} / {}".format(int(At[1])*int(A[0]), int(At[4])*int(A[1]), int(At[7])*int(A[2]), opred_A))
    print("{}+{}+{} / {}\n".format(int(At[2])*int(A[0]), int(At[5])*int(A[1]), int(At[8])*int(A[2]), opred_A))

    print("{}+{}+{} / {}".format(int(At[0])*int(A[3]), int(At[3])*int(A[4]), int(At[6])*int(A[5]), opred_A))
    print("{}+{}+{} / {}".format(int(At[1])*int(A[3]), int(At[4])*int(A[4]), int(At[7])*int(A[5]), opred_A))
    print("{}+{}+{} / {}\n".format(int(At[2])*int(A[3]), int(At[5])*int(A[4]), int(At[8])*int(A[5]), opred_A))

    print("{}+{}+{} / {}".format(int(At[0])*int(A[6]), int(At[3])*int(A[7]), int(At[6])*int(A[8]), opred_A))
    print("{}+{}+{} / {}".format(int(At[1])*int(A[6]), int(At[4])*int(A[7]), int(At[7])*int(A[8]), opred_A))
    print("{}+{}+{} / {}\n".format(int(At[2])*int(A[6]), int(At[5])*int(A[7]), int(At[8])*int(A[8]), opred_A))
    
    # ------ЭТАП3(Проверка)--------
    print("3)ПРОВЕРКА")    

    print("({}/{} {}/{} {}/{})".format(int(At[0])*int(A[0])+int(At[3])*int(A[1])+int(At[6])*int(A[2]), opred_A, int(At[1])*int(A[0])+int(At[4])*int(A[1])+int(At[7])*int(A[2]), opred_A, int(At[2])*int(A[0])+int(At[5])*int(A[1])+int(At[8])*int(A[2]), opred_A))
    print("({}/{} {}/{} {}/{})".format(int(At[0])*int(A[3])+int(At[3])*int(A[4])+int(At[6])*int(A[5]), opred_A, int(At[1])*int(A[3])+int(At[4])*int(A[4])+int(At[7])*int(A[5]), opred_A, int(At[2])*int(A[3])+int(At[5])*int(A[4])+int(At[8])*int(A[5]), opred_A))
    print("({}/{} {}/{} {}/{})\n".format(int(At[0])*int(A[6])+int(At[3])*int(A[7])+int(At[6])*int(A[8]), opred_A, int(At[1])*int(A[6])+int(At[4])*int(A[7])+int(At[7])*int(A[8]), opred_A, int(At[2])*int(A[6])+int(At[5])*int(A[7])+int(At[8])*int(A[8]), opred_A))

    # ------ЭТАП4(Проверка)--------
    print("4)ПРОВЕРКА")
    print("({} {} {})".format((int(At[0])*int(A[0])+int(At[3])*int(A[1])+int(At[6])*int(A[2]))/opred_A, (int(At[1])*int(A[0])+int(At[4])*int(A[1])+int(At[7])*int(A[2]))/opred_A, (int(At[2])*int(A[0])+int(At[5])*int(A[1])+int(At[8])*int(A[2]))/opred_A))
    print("({} {} {})".format((int(At[0])*int(A[3])+int(At[3])*int(A[4])+int(At[6])*int(A[5]))/opred_A, (int(At[1])*int(A[3])+int(At[4])*int(A[4])+int(At[7])*int(A[5]))/opred_A, (int(At[2])*int(A[3])+int(At[5])*int(A[4])+int(At[8])*int(A[5]))/opred_A))
    print("({} {} {})\n".format((int(At[0])*int(A[6])+int(At[3])*int(A[7])+int(At[6])*int(A[8]))/opred_A, (int(At[1])*int(A[6])+int(At[4])*int(A[7])+int(At[7])*int(A[8]))/opred_A, (int(At[2])*int(A[6])+int(At[5])*int(A[7])+int(At[8])*int(A[8]))/opred_A))


    print(" "*31+"(1 0 0)"+"\n"+"Если эта матрица выглядит так: (0 1 0)\n"+"то всё хорошо"+" "*18+"(0 0 1)\n")
    
input("Нажмите любую клавишу...")

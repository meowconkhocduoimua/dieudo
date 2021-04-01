from tkinter import *
# Vẽ sơ đồ gantt
def gantt(BoSo,pj,Min_c):
    import matplotlib.pyplot as plt
    toado = []
    vitri = []
    bat_dau = 0
    for i in BoSo:
        # Lấy i từ bộ số
        i = i-1
        # Tham chiếu thời gian
        thoigianthuchien = pj[i]
        ket_thuc = bat_dau +thoigianthuchien
        vitri.append([bat_dau,pj[i]])
        toado.append([bat_dau,ket_thuc])
        bat_dau = ket_thuc
    # print(toado)


    fig, ax = plt.subplots()
    # tọa độ đã được tính ở trên
    # toado = [[0, 2], [2, 7], [7, 14]]

    ax.broken_barh(vitri, (10, 9),
                facecolors=('tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray', 'tab:olive', 'tab:cyan'))
    # Chỉnh giới hạn độ cao 
    ax.set_ylim(0, 30)
    # Chỉnh giới hạn độ rộng (14)
    # toado[-1][-1] là điểm cuối cùng
    tieude = "Hàm mục tiêu là: %d"%(Min_c)
    ax.set_xlim(0, ket_thuc)
    ax.set_xlabel(tieude)
    ax.set_yticks([10]) 
    # Danh sách là bộ số chuẩn
    # danhsach = [1,2,3]
    ax.set_yticklabels([str(BoSo)])
    ax.grid(True)

    def text_plot(ten,vitri):
        ax.annotate(ten, (0, 0),
                    #xytext: chỉnh vị trí text, x căn đúng giữa 2 khoảng
                    xytext=(vitri, 13.5),
                    fontsize=16,
                    horizontalalignment='center')
    # Chỗ này là bộ số hiển thị là lộn xộn không theo thứ tự 123
    # nhưng tọa độ là vẽ lần lượt nên theo thứ tư (chỉnh vị trí của chữ phải theo biến tọa độ)
    # vì thế phải tạo 1 biến giả theo thứ tự để mà truy xuất text bằng 1 nửa khoảng 2 biên 
    biengia = 0
    for i in BoSo:
        text_plot(i,(toado[biengia][0]+toado[biengia][1])/2)
        biengia +=1
    tieude = "Hàm mục tiêu là: %d"%(Min_c)

    plt.show()
    
def XuatDuLieu(TGKetThuc,TGTreHan,pj,n,name):
    TongTG = sum(TGKetThuc)
    TGHoanThanhTB = sum(TGKetThuc)/n
    DoHuuDung = round(sum(pj)/sum(TGKetThuc)*100,2)
    SoLuongCVTB = round(sum(TGKetThuc)/sum(pj),2)
    DoTreTrungBinh = sum(TGTreHan)/n
    with open('output.txt','a+',encoding='UTF-8') as Xuat:
        Xuat.write("Bảng kết quả của luật: %s \n"%name)
        Xuat.write("Tổng thời gian các công việc: {} \n".format(TongTG))
        Xuat.write("Tổng thời gian hoàn thành công việc trung bình: {} \n".format(TGHoanThanhTB))
        Xuat.write("Độ hữu dụng: {} \n".format(DoHuuDung))
        Xuat.write("Số lượng công việc trung bình: {} \n".format(SoLuongCVTB))
        Xuat.write("Độ trễ trung bình: {} \n".format(DoTreTrungBinh))
        Xuat.write('-------------------------------\n')  

# Thuật toán WSPT
def thuat_toan_WSPT(n,pj,wj):
    thutu = [i for i in range(1,n+1)]
    list1 = [pj[i]/wj[i] for i in range(n)]
    list2 = thutu.copy()
    list1, list2 = zip(*sorted(zip(list1, list2)))  
    # Chỉ có thứ tự là đổi còn pj phải giữ lại vì nó tham chiếu theo pj
    thutu = list2

    Cj = 0
    Min_c = 0
    for i in thutu:
        Cj+= pj[i-1]
        Min_c += Cj*wj[i-1]
    BoSo = thutu
    return BoSo,Min_c

# Thuật toán SPT
def thuat_toan_SPT(n,pj):
    thutu = [i for i in range(1,n+1)]
    list1 = pj.copy()
    list2 = thutu.copy()
    list1, list2 = zip(*sorted(zip(list1, list2)))   
    # Chỉ có thứ tự là đổi còn pj phải giữ lại vì nó tham chiếu theo pj
    thutu = list2
    Cj = 0
    Min_c = 0
    for i in thutu:
        Cj+= pj[i-1]
        Min_c += Cj
    BoSo = thutu
    return BoSo,Min_c

# Thuật toán ERD
def thuat_toan_ERD(n,pj,dj):
    thutu = [i for i in range(1,n+1)]
    Cj = 0
    TGKetThuc = []
    TGTreHan = []
    Min_c = 0
    for i in range(len(pj)):
        Cj += pj[i]
        Delay = Cj -dj[i]
        TGKetThuc.append(Cj)
        Min_c += Cj
        if Delay <=0:
            TGTreHan.append(0)
        else:
            TGTreHan.append(Delay)
    BoSo = thutu
    print(TGKetThuc)
    print(TGTreHan)
    print("Tổng thời gian các công việc: {}".format(sum(TGKetThuc)))
    print("Tổng thời gian hoàn thành công việc trung bình {}".format(sum(TGKetThuc)/len(pj)))
    print("Độ hữu dụng {}% ".format(round(sum(pj)/sum(TGKetThuc)*100),4))
    print("Số lượng công việc trung bình {} ".format(sum(TGKetThuc)/sum(pj)))
    print("Độ trễ trung bình {}".format(sum(TGTreHan)/len(pj)))


    def vetkERD(n,pj,dj):
        Cj = 0
        TGKetThuc = []
        TGTreHan = []
        for i in range(n):
            Cj += pj[i]
            Delay = Cj -dj[i]
            TGKetThuc.append(Cj)
            if Delay <=0:
                TGTreHan.append(0)
            else:
                TGTreHan.append(Delay)
        
        g1 = sum(TGKetThuc)
        g2 = sum(TGKetThuc)/n
        g3 = round(sum(pj)/sum(TGKetThuc)*100,2)
        g4 = round(sum(TGKetThuc)/sum(pj),2)
        g5 = sum(TGTreHan)/n

        e1.configure(state=NORMAL) # make the field editable
        e1.delete(0, 'end') # remove old content
        e1.insert(0, str(g1)) # write new content
        # e1.configure(state=DISABLED) # make the field read only

        #Final Debt Amount:
        e2.configure(state=NORMAL) # make the field editable
        e2.delete(0, 'end') # remove old content
        e2.insert(0, str(g2)) # write new content
        # e2.configure(state=DISABLED) # make the field read only
        
        e3.configure(state=NORMAL) # make the field editable
        e3.delete(0, 'end') # remove old content
        e3.insert(0, str(g3)+"%") # write new content
        # e3.configure(state=DISABLED) # make the field read only

        e4.configure(state=NORMAL) # make the field editable
        e4.delete(0, 'end') # remove old content
        e4.insert(0, str(g4)) # write new content
        # e4.configure(state=DISABLED) # make the field read only

        e5.configure(state=NORMAL) # make the field editable
        e5.delete(0, 'end') # remove old content
        e5.insert(0, str(g5)) # write new content
        # e5.configure(state=DISABLED) # make the field read only
        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("FCFS")

    Label(master, text="Bảng FCFS").grid(row=0)


    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)


    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkERD(n,pj,dj)

    # Button(master, text='Quit', command=master.quit).grid(row=6, column=0, sticky=E, pady=4)
    # Button(master, text='Show', command=lambda: tiensieuthi(pj,dj)).grid(row=6, column=1, sticky=W, pady=4)

    
    tieude = "Hàm mục tiêu là: %d"%(Min_c)
    #Vẽ gantt
    gantt(BoSo,pj,Min_c)
    # mainloop( )
    # return BoSo, Min_c

# Thuật toán SPT có thời gian tới hạn
def thuat_toan_SPT_d(n,pj,dj):
    thutu = [i for i in range(1,n+1)]
    list1 = pj.copy()
    list2 = thutu.copy()
    list1, list2 = zip(*sorted(zip(list1, list2)))   
    thutu = list2
    Cj = 0
    TGKetThuc = []
    TGTreHan = []
    Min_c = 0
    for i in thutu:
        i -=1
        Cj += pj[i]
        Delay = Cj -dj[i]
        TGKetThuc.append(Cj)
        Min_c += Cj
        if Delay <=0:
            TGTreHan.append(0)
        else:
            TGTreHan.append(Delay)
    BoSo = thutu

    def vetkSPT_d(TGKetThuc,TGTreHan,pj,n):
        
        g1 = sum(TGKetThuc)
        g2 = sum(TGKetThuc)/n
        g3 = round(sum(pj)/sum(TGKetThuc)*100,2)
        g4 = round(sum(TGKetThuc)/sum(pj),2)
        g5 = sum(TGTreHan)/n

        e1.configure(state=NORMAL) # make the field editable
        e1.delete(0, 'end') # remove old content
        e1.insert(0, str(g1)) # write new content
        # e1.configure(state=DISABLED) # make the field read only

        #Final Debt Amount:
        e2.configure(state=NORMAL) # make the field editable
        e2.delete(0, 'end') # remove old content
        e2.insert(0, str(g2)) # write new content
        # e2.configure(state=DISABLED) # make the field read only
        
        e3.configure(state=NORMAL) # make the field editable
        e3.delete(0, 'end') # remove old content
        e3.insert(0, str(g3)+"%") # write new content
        # e3.configure(state=DISABLED) # make the field read only

        e4.configure(state=NORMAL) # make the field editable
        e4.delete(0, 'end') # remove old content
        e4.insert(0, str(g4)) # write new content
        # e4.configure(state=DISABLED) # make the field read only

        e5.configure(state=NORMAL) # make the field editable
        e5.delete(0, 'end') # remove old content
        e5.insert(0, str(g5)) # write new content
        # e5.configure(state=DISABLED) # make the field read only
        print(TGTreHan)
        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("SPT_d")

    Label(master, text="Bảng SPT").grid(row=0)


    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)


    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkSPT_d(TGKetThuc,TGTreHan,pj,n)

    
    tieude = "Hàm mục tiêu là: %d"%(Min_c)
    #Vẽ gantt
    gantt(BoSo,pj,Min_c)

# Thuật toán EDD có thời gian tới hạn
def thuat_toan_EDD(n,pj,dj):
    thutu = [i for i in range(1,n+1)]
    list1 = dj.copy()
    list2 = thutu.copy()
    list1, list2 = zip(*sorted(zip(list1, list2)))
    # Chỉ có thứ tự là đổi còn pj phải giữ lại vì nó tham chiếu theo pj
    thutu = list2
    Cj = 0
    TGKetThuc = []
    TGTreHan = []
    Min_c = 0
    for i in thutu:
        i -=1
        Cj += pj[i]
        Delay = Cj -dj[i]
        TGKetThuc.append(Cj)
        Min_c += Cj
        if Delay <=0:
            TGTreHan.append(0)
        else:
            TGTreHan.append(Delay)
    BoSo = thutu

    def vetkEDD(TGKetThuc,TGTreHan,pj,n):
        
        g1 = sum(TGKetThuc)
        g2 = sum(TGKetThuc)/n
        g3 = round(sum(pj)/sum(TGKetThuc)*100,2)
        g4 = round(sum(TGKetThuc)/sum(pj),2)
        g5 = sum(TGTreHan)/n

        e1.configure(state=NORMAL) # make the field editable
        e1.delete(0, 'end') # remove old content
        e1.insert(0, str(g1)) # write new content
        # e1.configure(state=DISABLED) # make the field read only

        #Final Debt Amount:
        e2.configure(state=NORMAL) # make the field editable
        e2.delete(0, 'end') # remove old content
        e2.insert(0, str(g2)) # write new content
        # e2.configure(state=DISABLED) # make the field read only
        
        e3.configure(state=NORMAL) # make the field editable
        e3.delete(0, 'end') # remove old content
        e3.insert(0, str(g3)+"%") # write new content
        # e3.configure(state=DISABLED) # make the field read only

        e4.configure(state=NORMAL) # make the field editable
        e4.delete(0, 'end') # remove old content
        e4.insert(0, str(g4)) # write new content
        # e4.configure(state=DISABLED) # make the field read only

        e5.configure(state=NORMAL) # make the field editable
        e5.delete(0, 'end') # remove old content
        e5.insert(0, str(g5)) # write new content
        # e5.configure(state=DISABLED) # make the field read only
        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("EDD")

    Label(master, text="Bảng EDD").grid(row=0)


    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)


    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkEDD(TGKetThuc,TGTreHan,pj,n)

    
    tieude = "Hàm mục tiêu là: %d"%(Min_c)
    #Vẽ gantt
    gantt(BoSo,pj,Min_c)

# Thuật toán LPT có thời gian tới hạn
def thuat_toan_LPT(n,pj,dj):
    thutu = [i for i in range(1,n+1)]
    list1 = pj.copy()
    list2 = thutu.copy()
    list1, list2 = zip(*sorted(zip(list1, list2),reverse=True))   
    # Chỉ có thứ tự là đổi còn pj phải giữ lại vì nó tham chiếu theo pj
    thutu = list2
    Cj = 0
    TGKetThuc = []
    TGTreHan = []
    Min_c = 0
    for i in thutu:
        i -=1
        Cj += pj[i]
        Delay = Cj -dj[i]
        TGKetThuc.append(Cj)
        Min_c += Cj
        if Delay <=0:
            TGTreHan.append(0)
        else:
            TGTreHan.append(Delay)
    BoSo = thutu
    C_max = Cj

    def vetkLPT(TGKetThuc,TGTreHan,pj,n):
        
        g1 = sum(TGKetThuc)
        g2 = sum(TGKetThuc)/n
        g3 = round(sum(pj)/sum(TGKetThuc)*100,2)
        g4 = round(sum(TGKetThuc)/sum(pj),2)
        g5 = sum(TGTreHan)/n

        e1.configure(state=NORMAL) # make the field editable
        e1.delete(0, 'end') # remove old content
        e1.insert(0, str(g1)) # write new content
        # e1.configure(state=DISABLED) # make the field read only

        #Final Debt Amount:
        e2.configure(state=NORMAL) # make the field editable
        e2.delete(0, 'end') # remove old content
        e2.insert(0, str(g2)) # write new content
        # e2.configure(state=DISABLED) # make the field read only
        
        e3.configure(state=NORMAL) # make the field editable
        e3.delete(0, 'end') # remove old content
        e3.insert(0, str(g3)+"%") # write new content
        # e3.configure(state=DISABLED) # make the field read only

        e4.configure(state=NORMAL) # make the field editable
        e4.delete(0, 'end') # remove old content
        e4.insert(0, str(g4)) # write new content
        # e4.configure(state=DISABLED) # make the field read only

        e5.configure(state=NORMAL) # make the field editable
        e5.delete(0, 'end') # remove old content
        e5.insert(0, str(g5)) # write new content
        # e5.configure(state=DISABLED) # make the field read only
        print(TGTreHan)
        print("Tổng thời gian các công việc:", g1)
        print("Tổng thời gian hoàn thành công việc trung bình:", g2)
        print("Độ hữu dụng:", g3)
        print("Số lượng công việc trung bình:",g4)
        print("Độ trễ trung bình:", g5)

    master = Tk()
    master.title("LPT")

    Label(master, text="Bảng LPT").grid(row=0)


    Label(master, text="Tổng thời gian các công việc:").grid(row=1)
    Label(master, text="Tổng thời gian hoàn thành công việc trung bình:").grid(row=2)
    Label(master, text="Độ hữu dụng:").grid(row=3)
    Label(master, text="Số lượng công việc trung bình:").grid(row=4)
    Label(master, text="Độ trễ trung bình:").grid(row=5)


    e1 = Entry(master, state=NORMAL)
    e1.grid(row=1, column=1)
    e2 = Entry(master, state=NORMAL)
    e2.grid(row=2, column=1)
    e3 = Entry(master, state=NORMAL)
    e3.grid(row=3, column=1)
    e4= Entry(master, state=NORMAL)
    e4.grid(row=4, column=1)
    e5 = Entry(master, state=NORMAL)
    e5.grid(row=5, column=1)

    vetkLPT(TGKetThuc,TGTreHan,pj,n)

    
    tieude = "Hàm mục tiêu là: %d"%(C_max)
    #Vẽ gantt
    gantt(BoSo,pj,C_max)
# thuat_toan_LPT(5,[6,2,8,3,9],[8,6,18,15,23])

# gantt([1,2,3,4],[9,4,3,5],21)

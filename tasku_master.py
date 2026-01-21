tasks = []

def commandProcess(command):
    try :
        if command.startswith("tasku add"):
            try: 
                taskAdd = command.split('"')[1]
                tasks.append(taskAdd)
                print(f"Tugas [{taskAdd}]: berhasil ditambahkan")
                homePage("fin")
            except Exception as e:
                print(f"Terjadi kesalahan saat menyimpan tugas")
                print("Pesan Error : ", e)
                homePage("err")
        elif command.startswith("tasku rm"):
            try:
                taskRemove = command.split('"')[1]
                tasks.remove(taskRemove)
                print(f"Tugas {taskRemove} berhasil dihapus")
                homePage("fin")
            except Exception as e:
                print("Terjadi kesalahan saat menghapus tugas")
                print("Pesan Error: ", e)
                homePage("err")
        elif command.startswith("tasku list"):
            try:
                for task, i in tasks:
                    print(f"{i}. {task}")
                print("Proses berhasil")
                homePage("fin")
            except Exception as e:
                print("Terjadi kesalahan, mohon ulangi proses")
                print("Pesan Error: ", e)
                homePage("err")
        elif command.startswith("tasku exit"):
            print("Proses Berhasil, Terimakasih")
    except Exception as e:
        print(f"Kesalahan sistem, mohon untuk mengulangi perintah anda | {e}")
        homePage("err")

def homePage(homeStatus) :
    print("")
    print("Tasku for your task")
    if homeStatus == "fin":
        print("Status : Proses terakhir berhasil")
    elif homeStatus == "st":
        print("Status : null")
    elif homeStatus == "err" :
        print("Status : Proses terakhir error")
    else:
        print("Status : unexpexted error")
    print("------------------")
    commandInput = input("> ")
    commandProcess(commandInput)

homePage("st")

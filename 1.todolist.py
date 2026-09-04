# 할 일 추가하기
def add_todo(todos,content): # 매개변수는 전달받는 통로
    todos.append({"할일":content,"완료":False})

# 할 일 목록보기
def show_todos(todos):
    num = 1
    for todo in todos:
        if todo["완료"] == False:
            print(f"{num}.[] {todo['할일']}")
        else:
            print(f"{num}.[V] {todo['할일']}")
        num += 1

# 할 일 완료하기
def complete_todo(todos,num):
    todos[num -1]["완료"] = True

# 할 일 삭제하기
def delete_todo(todos,num):
    del todos[num-1]

# 설계
print("todo 리스트에 오신 것을 환영합니다.")
todos = []

while True:
    print(f"1.할 일 추가하기\n2.할 일 목록보기\n3.할 일 완료하기\n4.할 일 삭제하기\n5.종료하기")
    menu = int(input("원하시는 메뉴의 번호를 입력하세요"))

    if menu == 1:
        content = input("추가하실 할 일을 입력하세요:")
        add_todo(todos,content)
    elif menu == 2:
        show_todos(todos)
    elif menu == 3:
        num = int(input("완료하실 할 일의 번호를 입력하세요"))
        if 1 <= num <= len(todos):
            complete_todo(todos,num)
        else:
            print("번호를 제대로 입력하십시오.")
    elif menu == 4:
        num = int(input("삭제하실 할 일의 번호를 입력하세요"))
        if 1 <= num <= len(todos):
            delete_todo(todos,num)
        else:
            print("번호 좀 똑바로 쳐라")
    elif menu == 5:
        break
    else:
        print("번호를 제대로 입력하십시오.")
    



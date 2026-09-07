class TodoList:
    def __init__(self):
        self.todos = []

    def add_todo(self,content):
        self.todos.append({"할일":content,"완료":False})

    def show_todos(self):
        num = 1
        for todo in self.todos:
            if todo["완료"] == False:
                print(f"{num}.[] {todo['할일']}")
            else:
                print(f"{num}.[V] {todo['할일']} ")
            num += 1

    def complete_todo(self,num):
        self.todos[num-1]["완료"] = True

    def delete_todo(self,num):
        del self.todos[num-1]


# 설계
print("todo 리스트에 오신 것을 환영합니다.")
todo_list = TodoList()

while True:
    print(f"1.할 일 추가하기\n2.할 일 목록보기\n3.할 일 완료하기\n4.할 일 삭제하기\n5.종료하기")
    menu = int(input("원하시는 메뉴의 번호를 입력하세요"))

    if menu == 1:
        content = input("추가하실 할 일을 입력하세요:")
        todo_list.add_todo(content)
    elif menu == 2:
        todo_list.show_todos()
    elif menu == 3:
        num = int(input("완료하실 할 일의 번호를 입력하세요"))
        if 1 <= num <= len(todo_list.todos):
            todo_list.complete_todo(num)
        else:
            print("번호를 제대로 입력하십시오.")
    elif menu == 4:
        num = int(input("삭제하실 할 일의 번호를 입력하세요"))
        if 1 <= num <= len(todo_list.todos):
            todo_list.delete_todo(num)
        else:
            print("번호 좀 똑바로 쳐라")
    elif menu == 5:
        break
    else:
        print("번호를 제대로 입력하십시오.")
    



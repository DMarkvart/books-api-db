# from fastapi import FastAPI, Depends
#
# app = FastAPI()
#
# def read_file():
#     print("Opening file 🔓 ")
#     try:
#         yield "Reading file ->>>>"
#     finally:
#         print("🔒Закрываю соединение")
#
#
# @app.get("/")
# def get_users(rf = Depends(read_file)):
#     print("что-то делаю, подключаю БД с пользователем", rf)
#     print("Ищем нужного пользователя и выводим на экран")
#
# @app.get("/books")
# def get_books(rf =Depends(read_file)):
#     print("что-то делаю, подключаю БД с  книгами", rf)
#     print("Ищем нужную книгу и выводим на экрану ")
#
# #Этот код выполнится ТОЛЬКО если файл запустили напрямую
# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("sand:app", reload=True)
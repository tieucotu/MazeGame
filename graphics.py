

from tkinter import Tk, BOTH, Canvas

#WINDOW CLASS'S CONSTRUCTOR
#1. The constructor should take a width and height. This will be the size of the new window we create in pixels.
    # Có 2 construcor là width và height. Đây cũng là kích thước của màn hình window game.
#2. It should create a new root widget using Tk() and save it as a data member
    # Bằng cách dử dụng Tk, nó sẽ tạo ra một widget gốc mới và lưu làm một dữ liệu. 
#3. Set the title property of the root widget
    # Đặt một thuộc tính title cho widget gốc.
#4. Create a Canvas and save it as a data member.
    # Tạo một Canvas/ khung vẽ và lưu nó như 1 dữ liệu.
#5. Pack the canvas so that it's ready to be drawn
    # Đóng gói khung vẽ/ canvas để nó ở trạng thái sẵn sàng vẽ đc.
#6. Create a data member to represent that the window is "running", and set it to False
    # Tạo 1 thông tin thể hiện rằng Window đang thực hiện công việc và set nó là False.

class Window:
    def __init__(self, width, height):  #1.
        self.__root = Tk()              #2.
        self.__root.title("Maze Solver")    #3.
        self.__root.protocol("WM_DELETE_WINDOW", self.close)
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width) #4.
        self.__canvas.pack(fill=BOTH, expand=1)     #5.
        self.__running = False                      #6.
        
        
#REDRAW() METHOD
    # We need a method we can call that will redraw all the graphics in the window. 
        # Cần có 1 method để có thể redraw tất cả các graphics in the window.
    # Tkinter is not a reactive framework like React or Vue - we need to tell the window when it should render to visuals.
        # Tkinter không phải reactive framwork như React or Vue -> Cần phải đưa chỉ lệnh cho window khi nó cần render to visuals.
    # The redraw() method on the window class should simply call the root widget's update_idletasks() and update() methods. 
        # method redraw() trong WINDOW class, method của root widget được gọi đơn giản là update_idletasks() và update().
    # Each time this is called, the window will redraw itself.
        # Mỗi lần nó được gọi, window sẽ vẽ lại chính nó.

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        

#WAIT_FOR_CLOSE() METHOD
    #1 This method should set the data member we created to track the "running" state of the window to True. 
        # Method nay đặt 1 data đã tạo trước đó để track tình trạng của running hiện trên window thành True.
    #2 Next, it should call self.redraw() over and over as long as the running state remains True.
        # Tiếp theo, trong khi function running, nó sẽ lặp lại việc gọi ra lệnh self.redraw() 

    def wait_for_close(self):
        self.__running = True       #1
        while self.__running:
            self.redraw()           #2
        print("window closed...")
        
#WINDOW CLASS DRAW_LINE() METHOD
#1 We need a draw_line method on our Window class.
# It should take an instance of a Line and a fill_color as inputs, then call the Line's draw() method.
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)


#THE CLOSE() METHOD
#1 Lastly, the close() method should simply set the running state to False. 
    # Cuối cùng, method close() dùng để set running state to False.
# You'll also need to add another line to the constructor to call the protocol method on the root widget, 
    # Cần add another line to constructor để gọi ra protocol method trong root widget,
# to connect your close method to the "delete window" action. This will stop your program from running when you close the graphical window.
    # để kết nối close methos với hành động "delete window". Lệnh này sẽ dừng lại chương trình đang chạy khi đóng/ tắt màn hình hiển thị game.
    def close(self):
        self.__running = False

#POINT CLASS
#1 Let's make a little Point class. It should simply store 2 public data members:
    # x - the x-coordinate (horizontal) in pixels of the point
    # y - the y-coordinate (vertical) in pixels of the point
    # x=0 is the left of the screen.
    # y=0 is the top of the screen.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#LINE CLASS
#1 The line class has a bit more logic in it. Its constructor should take 2 points as input, and save them as data members.
class Line:
    def __init__(
        self, 
        point1, 
        point2,
    ):
        self.point1 = point1
        self.point2 = point2
#DRAW() METHOD
#1 The Line class needs a draw() method that takes a Canvas and a "fill color" as input.The fill_color will just be a string like "black" or "red".
#2 Next it should call the Canvas's create_line method.
    def draw(self, canvas, fill_color ="black"):
        canvas.create_line(
            self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill= fill_color, width=2
        )
#3 Finally, pack the canvas again, just like you did in the constructor.
        #canvas.pack(fill=BOTH, expand=1)


        
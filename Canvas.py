import picture as graph_gui

class Canvas:

    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def canvas(self):
        graph_gui.new_picture(self.width,self.height)
    
    def background(self,color):

        graph_gui.set_fill_color(color)
        graph_gui.draw_filled_rectangle(0,0,self.width,self.height)
    
    def color(self,color):
        graph_gui.set_outline_color(color)

    def run(self):
        graph_gui.run()
    
    
    
    






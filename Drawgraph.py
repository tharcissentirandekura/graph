from Canvas import Canvas as canvas
from graph import Graph as graph


class Draw:

    def __init__(self):
        self.graph = graph()
        self.canvas = canvas(500,500)
        self.canvas.canvas()
        

    


def main():

    draw = Draw()
    draw.canvas.canvas()
    draw.canvas.background("white")
    draw.canvas.color('red')
    draw.canvas.run()

if __name__ == "__main__":
    main()



    

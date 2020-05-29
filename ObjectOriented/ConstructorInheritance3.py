class A:
    
    def __init__(self):
        print("In A init")
        
    def feature1(self):
        print("Feature 1 working")
        
        
class B(A):
    
    def __init__(self):
        print("In B init")
        super().__init__()
        
    def feature2(self):
        print("Feature 2 working")
        
        
b = B()
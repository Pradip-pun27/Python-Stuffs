#Instance-method:Best for operations on instances(objects) of the class.
#Class-method:Best for class-level data or require access to the class itself.
#Static-method:Best for utility funcs that don't need access to class' data.

class School:
    scl_num =0 #Class_level variable or attribute
    def __init__(self,n,no): #Constructor:instance_method
        self.name=n #object_level attributes
        self.num_std = no #object_level attributes
        School.scl_num+=1;
        
    def __str__(self): #Instance_method
        return (f"Name of School is {self.name}")
        
    def get_info(self): #Instance_method
        print(f"{self.name} has {self.num_std} students.")
        
    @staticmethod
    def check_teacher_post(post):
        posts = ['Principal','Vice-Principal','Accountant','Chairman','Coordinator','Shareholder']
        return post.capitalize() in posts
        
    @classmethod
    def get_nums_scl(cls):
        print(f"There are {cls.scl_num} schools in total.")

s1= School('DVC',2000) #Instantiating class named School
s2=School('PPMSS',6000)
School.get_nums_scl() #Calling class_method
print(School.check_teacher_post('Coordinator')) #Calling static_method
print(s1) #Calling instance_method(__str__())
s2.get_info() #Calling another instance_method(get_info())
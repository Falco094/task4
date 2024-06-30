class student :
    def __init__(self , name ,courses):
        
        self.name = name
        self.courses = []
        print(f'{name} , {courses}')
        
    def enroll (self, cours_name):
        self.courses.append(cours_name)
        print('Hello')
        
    def get_courses(self):
        return self.courses
    
student=student('Falco','python')
student.enroll('python')
print(student.get_courses())
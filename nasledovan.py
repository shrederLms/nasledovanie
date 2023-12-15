class human:
    
    def __init__(self,n,a,h):
        print('')
        self.__name=n
        self.__age=a
        self.height=h
        
    def print(self):

        print(f'name:{self.__name}')
        print(f'age:{self.__age}')
        print(f'heigh:{self.height}')
        print('-'*30)
        
    @property        
    def name(self):
        return '' + self.__name
    
    @name.setter
    def name(self,n):
        if len(n)>=2 and len(n)<=20:
            self.__name=n
        else:
            print(f'ошибка:{n}')
            
    @property
    def age(self):
        return 'Мне:' + self.__age
    
    @name.setter
    def age(self,a):
        if int(a)>=2 and int(a)<=20:
            self.__age=a
        else:
            print(f'ошибка:{a}')
 
    
q=human('Кирилл',18,180)
q.name='Соня'
name=q.name
print(name)
q.age='18'
age=q.age
q.print()


class stud(human):
    def study(self):
        print(f'{self.name} study')
a=stud('Grisha',18,170)
a.study()

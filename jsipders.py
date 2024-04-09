class j_spiders:
    name='jspiders'
    branch='Marathahalli'
    ph=7674856231
    c1='python'
    c2='java'
    c3='mern'
    def __init__(self,s_name,s_id,ph,course,trainer,fees,password,b_code):
        self.s_name=s_name
        self.s_id=s_id
        self.ph=ph
        self.course=course
        self.trainer=trainer
        self.fees=fees
        self.password=password
        self.b_code=b_code
    @staticmethod
    def get_password():
        return str(input('Enter the password: '))
    def validate(self):
        return self.password==self.get_password()
    def change_trainer(self):
        if self.validate():
            c_t=('Enter the new trainer name')
            self.trainer=c_t
        else:
            print('wronng password')
    def get_fees(self):
        if self.validate():
            print(f'your fees is {self.fees}')
        else:
            print('wrong password')
    def add_newbatch(self):
        if self.validate():
            n_batch=input('Enter new batch code : ')
            self.b_code=n_batch
            print('batch added succesfully')
        else:
            print('wrong password')
    def change_password(self):
        if self.password==input('Enter the old password: '):
            new_p1=input('Enter the new password: ')
            new_p2=input('Enter the new password: ')
            if(new_p1==new_p2):
                self.password=new_p1
                print('Password changed succesfully')
            else:
                print('Both password should be equal')
        
j1=j_spiders('ashish',12,6386352801,'python','santosh',30000,'1234','PTD-m8')

j1.change_password()
j1.add_newbatch()
j1.get_fees()
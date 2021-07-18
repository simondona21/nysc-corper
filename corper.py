######Imports#######
from datetime import datetime,date


class NyscCorps():    

    def __init__(self, full_name, state, lga, gender, religion,callup_number,state_code,birthday):
        self.name = full_name
        self.birthday = birthday#yyyymmdd
        self.state = state
        self.lga = lga
        self.gender = gender
        self.religion = religion
        self.uniform = ['green','white']
        self.callup_number = callup_number
        self.state_code = state_code

        #extracting the first and last name
        name_pieces = full_name.split(" ") 
        self.first_name = name_pieces[0]
        self.last_name = name_pieces[-1]

    def age(self):
        today = datetime.today().strftime('%Y%m%d')
        current_yr = int(today[0:4])
        curren_mm = int(today[4:6])
        current_dd = int(today[6:8])
        today_date = date(current_yr,curren_mm,current_dd)
        yyyy = int(self.birthday[0:4])
        mm = int(self.birthday[4:6])
        dd = int(self.birthday[6:8])
        dob = date(yyyy,mm,dd)
        age_in_days = (today_date - dob).days
        age_in_years = age_in_days / 365
        return int(age_in_years)

    def speak(self, *languages):

        """Function takes a set of langs as input  and returns a list of languages"""
        
        if any(not isinstance(lang, str) for lang in languages):
            raise TypeError('You need to pass in the right datatype')

        return list(languages)
  
    def read(self,*articles):
        """Function takes a set of langs as input  and returns a list of languages"""
        
        if any(not isinstance(lang, str) for lang in articles):
            raise TypeError('You need to pass in the right datatype')

        return list(articles)

    def sleep(self, tm = '00:00'):
        """
        function takes in the time a corper sleeps in str format and return
        converts the time to a datetime.time format.
        """
        sleep_time = None
        try:
            if not isinstance(sleep_time, str):
                #convert to str
                corper_sleep_time = str(tm)
                #convert str to datetime
                datetime_object = datetime.strptime(corper_sleep_time, '%H:%M')
                #format datetime to time
                sleep_time = datetime_object.strftime("%H:%M %p")
        except ValueError as error:
            print(error, ' You need to pass in the right datatype')
        else:
            return 'Corper sleeps at', sleep_time


    def walk(self,):
     
        if isinstance(self.name, str) & isinstance(self.birthday, str) &  isinstance(self.gender, str)  & isinstance(self.religion, str) :
            if (self.name and self.birthday and self.gender and self.religion):
                movement = True
        else:
            raise TypeError('You need to pass in the right datatype')
            
        return movement
    
    def __repr__(self):

      return "Nysc Corper Informations are ( Name ='{0}', Age = '{1}',Callup_number ='{2}', State ='{3}', Lga ='{4}', Gender ='{5}',  Religion ='{6}', StateCode ='{7}') \
                                                ".format(self.name,self.age(),self.callup_number, self.state, self.lga, self.gender, self.religion,self.state_code )
    
    def __str__(self):
        return self.__repr__()
         

class PirmaryPlaceOfAssignment(NyscCorps):
    
    def __init__(self, ppa_name, ppa_lga):

        self.ppa_name = ppa_name
        self.ppa_lga = ppa_lga
        self.days_of_week = ['monday','tuesday','wednesday','thursday', 'fiday']

    def school(self, discipline,workdays,school_type = 'public'):
        course = []

        discipline,workdays,school_type = discipline.lower(),workdays.lower(), school_type.lower()
        if isinstance(discipline, str):
            if discipline== 'Science':
                course.append(('maths', 'physics','chemistry','biology','english'))
            elif discipline == 'Art':
                course.append(('literature', 'government','crs','civic','english'))
            elif discipline == 'Social Science':
                course.append(('maths', 'marketing','economics','accounting','english'))
            else:
                print("You did not enter the right descipline, enter the right discipline")
        else:
            print(TypeError)
            print('You entered the wrong type')
        pos = 0
        day = None
        while pos < len(self.days_of_week) and isinstance(workdays, str):
            if workdays in (self.days_of_week):
                day = {'workday' : workdays}
                break
            else:
                return None
        
        if isinstance(school_type, str):
            if school_type == 'public':
                type, starttime_endtime = {'school_type': school_type}, {'Resumption & closing time': " 8:00AM - 4:00PM"}
            elif school_type == 'private':
                type, starttime_endtime = {'school_type': school_type}, {'Resumption & closing time': " 8:00AM - 4:00PM"}

        return course, day, (type, starttime_endtime)      
        
    def health_sector(self, profession,workdays):
        """
        function takes in corpers discipline and workday and it outputs
        his profession,workday and the time he went for work on that given day
        """
        profession = profession.lower()
        workdays = workdays.lower()

        field = ['surgeon', 'pharmacy', 'dentist']
        day = 0
        starttime_endtime = 0
        if isinstance(profession,  str) and isinstance(workdays,str):
            
            if profession in field:
                profession = {'profession':profession}
                starttime_endtime = {'Resumption & closing time': " 8:00AM - 4:00PM"}
            else:
                profession = None
                starttime_endtime = None

            for i in range(len(self.days_of_week)):
                if workdays in self.days_of_week:
                    day = {'workday' : workdays}
                    i+=1
                    break
                day = 'pass in the work day of the week'

            return profession, day, starttime_endtime              
        else:
            print(TypeError)
            print('You entered the wrong type')

    def ministry(self,name_of_ministry, workdays):

        """
        function takes in corpers discipline and workday and it outputs
        his profession,workday and the time he went for work on that given day
        """
        name_of_ministry = name_of_ministry.lower()
        workdays = workdays.lower()
        field = ['ministry of education', 'ministry of works', 'ministry of Finance', 'ministry of agriculture', 'ministry of science & tech', 'ministry of foreign affairs']
        day = 0
        starttime_endtime = 0
        if isinstance(name_of_ministry,  str) and isinstance(workdays,str):
            
            if name_of_ministry in field:
                name_of_ministry = {'Ministry': name_of_ministry}
                starttime_endtime ={'Resumption & closing time': " 8:00AM - 4:00PM"}
            else:
                name_of_ministry = None
                starttime_endtime = None

            for i in range(len(self.days_of_week)):
                if workdays in self.days_of_week:
                    day = {'workday' : workdays}
                    i+=1
                    break
                day = 'pass in the work day of the week'

            return name_of_ministry, day, starttime_endtime

    def __iter__(self):
        """Yield a batch of day of the week"""
        for day in self.days_of_week: 
            yield day

    def __len__(self):
        """Number of workdays"""
        return len(self.days_of_week)
                   
    def __repr__(self):

        return "Your PirmaryPlaceOfAssignment are (Ppa-Name='{}', Ppa-Local-Govt='{}')".format(self.ppa_name, self.ppa_lga)
    
    def __str__(self):
        return self.__repr__()

class CDS(NyscCorps):
    def __init__(self,lga, batch,card_submission, prayers,card_signing,saed_lecture,group_talk,closing):
        self.lga = lga
        self.batch = batch
        self.card_submission = card_submission
        self.prayers = prayers
        self.card_signing = card_signing
        self.saed_lecture = saed_lecture
        self.group_talk = group_talk
        self.closing = closing

        self.time = "10AM - 12PM"
        # self.group = group
        # self.programe = self.programe

    def corper_cds_info(self,day,group):
        cds_days = ['wednesday','thursday']
        cds_groups = ['Servicom','Sanitation']

        if (day in cds_days) and (group in cds_groups):
            return day, group           
        else:
            print('you entered the wrong cds day')    

    def activities(self,card_submissionprayers,card_signing,saed_lecture,group_talk,closing):
        pass 

    def drama(self, act):
        if isinstance(self.lga, str) and isinstance(self.batch, str) and isinstance(self.prayers) and isinstance(self.card_signing):
            if self.lga and self.batch and self.prayers and self.card_signing:
                act = True
            else:
                raise ValueError

            return act


    
    def dancing():
        pass


        
    def groups(self):
        pass


    def skills(self,craft, tech,resources):
        """ listing the various craft skill,tech skill and resources one can do while serving"""
        kinds = ['tailoring','embroidry','make_up','cubling','hair_making']
        types = ['data science','developer','excel analyst','website designer']
        aspects = ['foreign_language','Hr','ican_exam','toefel','gre']
        if isinstance(craft, str) and isinstance(tech, str) and isinstance(resources,str):
            if craft in kinds:
                craft == craft
            elif tech in types:
                    tech = tech
            elif resources in  aspects:
                resources = resources
            else:
                raise 'assign a corper to particular place'
       
        return craft, tech, resources
                       

        

    def other(self):
        pass
    
    def sports(self,*games):
         """taking a set of game as input  and returns a list of games"""
         
         if any(not isinstance(game, str) for game in games):
            raise TypeError('enter a game type')

         return list(games)



    def __iter__(self):
        """Yield a batch of day of the week"""
        for corpers in self.batch: 
            yield corpers

# cd = CDS()
# print(cd.corper_cds_info('wednesday','Sanitation'))


#         day = ['thursday']
#         areas = ['sports_group','dance_drame','sanitation','aditorial','drugs_free']
#         if isinstance(group,str) and isinstance(days, str):
#             if group in areas:
#                 group = group
#             else:
#                 group = None

#             for i in range(len(day)):
#                 if days in day:
#                     i+=1
#                     break
#                 day = 'enter the correct day'




#############TESTING###############


# corper = NyscCorps('chuks','Delta state','Oshimili South', 'Male', 'Christian')
# print(corper.religion)
    
# ppa = PirmaryPlaceOfAssignment('Abu primary school', ',' 'sho log')
# print(ppa.ministry('Ministry of Works','MONDAY'))
# print(ppa.health_sector('pharmacy','monday'))

#full_name, state, lga, gender, religion,callup_number,state_code,birthday
# corper = NyscCorps('chuks okolie','Delta state','Oshimili South', 'Male', 'Christian', 'NYSC/DPU/2020/140760', 'AN/20B/3132', '19910820')
# print(corper.age())

cds = CDS(NyscCorps)
print(cds.skills('tailoring','data science','Hr'))
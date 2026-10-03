class studentClass:
    def __init__(self):
        self.full_name = ''
        self.date_of_birth = ''
        self.age = ''
        self.gender = ''
        self.mobile_number = ''
        self.email_address = ''
        self.password = ''
        self.preferred_language = ''
        self.school_college_name = ''
        self.class_grade = ''
        self.board_curriculum = ''
        self.academic_year = ''
        self.subjects_for_tuition = []
        self.current_level_per_subject = {}
        self.areas_topics_needing_help = []
        self.parent_guardian_name = ''
        self.parent_guardian_relationship = ''
        self.parent_guardian_mobile_number = ''
        self.parent_guardian_email_address = ''
        self.preferred_communication_method = ''



    def setuserNameandPassword(self, email, password):
        self.email_address = email
        self.password = password  

    def setBasicDetails(self, full_name, date_of_birth, gender, mobile_number, preferred_language, school_college_name, class_grade, board_curriculum, academic_year):
        '''
        This method sets the basic details of the student, including full name, date of birth, gender, mobile number, preferred language, school/college name, class/grade, board/curriculum, and academic year.
        '''
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.gender = gender
        self.mobile_number = mobile_number

        self.preferred_language = preferred_language
        self.school_college_name = school_college_name
        self.class_grade = class_grade
        self.board_curriculum = board_curriculum
        self.academic_year = academic_year

    def saveToDB(self):
        import sqlite3
        connetion = sqlite3.connect("tution.db")
        cursor = connetion.cursor()
        cursor.execute("""
                INSERT INTO students (
                full_name,
                age,
                mobile_number,
                email_address,
                password,
            dob,
            gender,
            preferred_language,
            school_college_name,
            class_grade,
            borad_curriculum,
            acaemic_year
            ) values (?,?,?,?,?,?,?,?,?,?,?)
            """,(
                self.full_name,
                self.age,
                self.mobile_number,
                self.email_address,
                self.password,
                self.date_of_birth,
                self.gender,
                self.preferred_language,
                self.school_college_name,
                self.class_grade,
                self.board_curriculum,
                self.academic_year
                ))

        # Save changes and close connection
        connetion.commit()
        connetion.close()
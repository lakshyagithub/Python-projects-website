class doctor:
    def __init__(self):
        print("This is the doctor class.")
    def bmi(weight, height):
        bmi = weight/(height*height)
        print("Your BMI is", str(bmi))
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great, your heart is good!")
        else:
            print("Oops, your heart rate is not good and you need to vist a doctor ASBP!")

class paitent(doctor):
    def __init__(self, name, weight, height, heart_rates):
        self.paitent_name = name
        self.paitent_weight = weight
        self.paitent_height = height
        self.paitent_heart_rates = heart_rates
    def heartCheck(self):
        print("\n Your name:", self.paitent_name)
        doctor.bmi(self.paitent_weight, self.paitent_height)
        doctor.heart_rate(self.paitent_heart_rates)


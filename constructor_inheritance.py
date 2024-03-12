class OTTSubscription:                      # main class 
    def __init__(self, ID, Plan, Total_Payment):
        self.id = ID
        self.plan = Plan
        self.Total_Payment = Total_Payment
    def subscription(self):
        print(f"Subscriber with {self.id} id subscribe to {self.plan} plan ")
    def unsubscription(self):
        print(f"Subscriber with {self.id} id unsubscribe to {self.plan} plan By paying {self.Total_Payment}")
        
class premiumSubscription(OTTSubscription):                 #  inheriated class : argument is parent class 
    def __init__(self,ID,Plan,Total_Payment,MAx_screen):
        super().__init__(ID,Plan,Total_Payment)                 # by using super keywod we use main class Methods & Properties
        self.MAx_screen = MAx_screen

    def SnowMAx_screen(self):
        print(f"Subscribe view content only {self.MAx_screen} Screen")
        
Jiocinema = premiumSubscription(1578,"1 Yearly",580, 4)                 # Object created 
print(Jiocinema.id)
print(Jiocinema.MAx_screen)

Jiocinema.subscription()
Jiocinema.unsubscription()
Jiocinema.SnowMAx_screen()


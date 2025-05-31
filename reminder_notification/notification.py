import time
from plyer import notification
def notify():
    while True:
        notification.notify(
            title = "It's time to take a break!", 

            message = "You have been working for 25 minutes. Please take a 5-minute break.",
            
            app_icon = None, # You can specify an icon path if you have one
             
            timeout = 2 # Notification will stay for 10 seconds
       )
        time.sleep(10) # Notify every 2 hours
    
notify()
    

  

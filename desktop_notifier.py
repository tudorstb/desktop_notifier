from plyer import notification
title ="Hello"
message='go wash'

notification.notify(title = title,
                    message=message,
                    app_icon = None,
                    timeout =10,
                    toast="ammamama")
def intro():
    print('Welcome to the notification app')
    new_notification=input("If you wish to add a notification press (N):")
    return new_notification

verify_redo='Nn'

while verify_redo.find(intro())>-1:

    print('-------------------')

print('Good bye')
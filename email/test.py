from transactions import *

n = NewsletterSender(["giorgosera@gmail.com", "george@avocarrot.com"], "Hello", "/home/george/akka.txt")
n.send(logging=True)
# to run the pyscreenshot library we need its parent library called Pillow
# use the pyscreenshot library to capture the screen shot and save it


import pyscreenshot as pyss
import timer as t

while True:
    a = 0
    b = None
    user = str(input("Take a screenshot? Y for yes and N for no: "))
    input = user.lower()
    while input in 'y':
        try:
            image = pyss.grab()

            image.show()
            a += 1
        except ValueError:
            print("Error")

        finally:
            try:
                image.save(f"screenshot_{a}.png")
            except FileExistsError:
                b += 1
                image.save(f"screenshot_{a}.png")
                break
            


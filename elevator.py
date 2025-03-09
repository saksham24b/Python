def elevator(entry, exit):
    floor=entry
    elevator_direction= ""
    if entry>exit:
        elevator_direction = "Going Down: "
        while(floor>=exit):
            elevator_direction += str(floor)
            if(floor>exit):
                elevator_direction+=" | "
            floor-=1
    else:
        elevator_direction = "Going up: "
        while(floor<=exit):
            elevator_direction+=str(floor)
            if(floor<exit):
                elevator_direction+=" | "
            floor+=1
    return elevator_direction

def main():
    entry = int(input("Entry floor: "))
    exit = int(input("Exit floor: "))
    print(elevator(entry,exit))


if __name__=="__main__":
    main()

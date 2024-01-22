
file=open("practial-2.txt",'w')
option=int(input("option to select:\n1.Area of Rectangle\n2.Perimeter of rectangle\n"))
if (option == 1) :
    length = int(input("length of the Rectangle :"))
    breadth = int(input("Breadth of the Rectangle :"))
    Area = length * breadth
    file.write(f"Area of rectangle is: {str(Area)}")
elif (option == 2) :
    length = int(input("length of the Rectangle :"))
    breadth = int(input("Breadth of the Rectangle :"))
    Perimeter = 2 *( length + breadth)
    file.write(f"perimeter of rectangle is: {str(Perimeter)}")
else :
    file.write( )
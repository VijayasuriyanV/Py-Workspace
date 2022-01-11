def full_pyramid ():
    print("Full Pyramid Pattern of Stars (*): ")
    n=int(input("Enter the no.of rows to print pyramid pattern"))
    for i in range(n):
        for s in range(-n, -i):
            print(" ", end="")
        for j in range(i+1):
            print("* ", end="")
        print()
# output

 #         * 
 #        * * 
 #       * * * 
 #      * * * * 
 #     * * * * * 
  

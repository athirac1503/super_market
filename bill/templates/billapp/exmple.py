# arr = [1, 2, 3, 4, 2, 7, 8, 8, 3];    
# for i in range(0, len(arr)):    
#     for j in range(i+1, len(arr)):    
#         if(arr[i] == arr[j]):    
#             print(arr[j]);  

#--------------------------------------
def pypart(n):
     
    # outer loop to handle number of rows
    # n in this case
    for i in range(0, n):
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ",end="")
      
        # ending line after each row
        print("\r")
 
# Driver Code
n = 10
pypart(n)
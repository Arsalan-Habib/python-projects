dataset=[i for i in range(0,1000,2)]

x=int(input("Enter a value to search for..\n"))


def binary_search(n,arr):
    first=0
    last=len(arr)-1
    checks=1

    while(first<=last):

        mid=(first+last)//2
        
        if arr[mid]==n:
            return mid,checks

        elif arr[mid]>n:
            last=mid-1
            checks+=1

        elif arr[mid]<n:
            first=mid+1
            checks+=1
    return -1,checks

index,tries=(binary_search(x,dataset))
if index==-1:
    print("Sorry but your number isn't in the list.\nIt still took me "+str(tries)+" tries though.")
else:
    print("Your element was found at index "+str(index)+ "\nThe search was completed in "+str(tries) +" tries.")

input("press enter to continue...")



# List of numbers from 1 to 10
numbers = list( range ( 1, 11 ))  # This is a simple list from 1 to 10

# Function to calculate the sum of even numbers using bitwise operator
def sum_of_even_numbers( nums ):
    total = 0
    for num in nums:
        # Bitwise operation for even check: number & 1 should be 0 if even
        if ( num & 1 ) == 0:  # bitwise operator combined
            total += num  # Add even number to the total
    return total

# Main code block
if __name__ == "__main__":
    # Calculate the sum of even numbers from the list
    even_sum = sum_of_even_numbers( numbers )
    
    # Output the sum of even numbers
    print( "Sum of even numbers:", even_sum)

    # Check if a number is even or odd using bitwise operator
    for num in numbers:
        if ( num % 2 ) == 0:  # If the number is even
            print( "The", num, "is even")
        else:  # If the number is odd
            print( "The", num, "is odd")
def compute_crc(input_bits, polynomial_bits):
    n = len(input_bits)
    m = len(polynomial_bits)
    
    # Append m-1 zeros to the input bits
    dividend = input_bits + '0' * (m - 1)
    dividend = list(dividend)
    
    for i in range(n):
        if dividend[i] == '1':
            for j in range(m):
                dividend[i + j] = '0' if dividend[i + j] == polynomial_bits[j] else '1'
    
    return ''.join(dividend[-(m-1):])

if __name__ == "__main__":
    input_bits = input("Enter the input binary string: ")
    polynomial_bits = input("Enter the polynomial binary string: ")
    
    crc = compute_crc(input_bits, polynomial_bits)
    transmitted_message = input_bits + crc
    
    print("The computed CRC is:", crc)
    print("The transmitted message is:", transmitted_message)

#!/usr/bin/python3

def validUTF8(data):
     # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to identify the most significant bits
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    # Traverse each integer (byte) in the data
    for num in data:
        # Mask to keep only the least significant 8 bits
        byte = num & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            # If num_bytes is 1, it's a single-byte character (ASCII)
            if num_bytes == 0:
                continue

            # UTF-8 characters are 1 to 4 bytes long
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            # All continuation bytes must start with '10xxxxxx'
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the count of bytes to process in the current character
        num_bytes -= 1

    # If we're done processing all bytes, num_bytes should be 0
    return num_bytes == 0

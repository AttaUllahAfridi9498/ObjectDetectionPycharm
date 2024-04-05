
blocks = int(input("Enter the number of blocks: "))
heights = 0
layer_blocks = 1
while blocks >= layer_blocks:
    heights += 1
    blocks -= layer_blocks
    layer_blocks += 1
print("The height of the pyramid:", heights)

"""
def calculate_pyramid_height(blocks):
    height = 0
    total_blocks = 0
    while total_blocks <= blocks:
        height += 1
        total_blocks += height
    return height - 1 
     
test_cases = [6, 20, 1000, 2]
for blocks in test_cases:
    print("Sample input:", blocks)
    print("Expected output: The height of the pyramid:", calculate_pyramid_height(blocks))
"""
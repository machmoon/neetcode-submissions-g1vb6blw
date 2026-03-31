class Solution:
    def canJump(self, nums: List[int]) -> bool:

        jumps = 0
        
        for i in range(len(nums)-1):
            
            if jumps < nums[i]:
                jumps = nums[i]
            elif jumps == 0:
                return False

            jumps -= 1
            
        return True
        # # Literailly the algo is just look in the jump window and take the highest jump and then 
        # current_jump_value = nums[0]
        # current_jump_index = 0


        # while current_jump_index + current_jump_value < len(nums):
            
        #     if current_jump_value == 0:
        #         return False
        #     i = 0
        #     max_num = 0
        #     temp_jump_index = 0
            
        #     while current_jump_index + i < len(nums) and i < current_jump_value:
        #         i+=1
        #         if nums[current_jump_index + i] > max_num:
        #             max_num = nums[current_jump_index + i]
        #             temp_jump_index = current_jump_index + i

        #     current_jump_value = nums[temp_jump_index]

        # # if current_jump_index + current_jump_value <= len(nums):
        # return True



# 24400042001201
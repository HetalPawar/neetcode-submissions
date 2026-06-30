class Solution:
    def trap(self, height: List[int]) -> int:

        l,r = 0, len(height)-1
        water = 0
        leftwall = height[l]
        rightwall = height[r]

        while l<r:

            if leftwall < rightwall:
                #left
                l +=1 #Move the pointer.

                #If the new bar is shorter than the wall, add water.
                if height[l] < leftwall:
                    water += leftwall - height[l] 

                #Update the wall.
                leftwall = max (height[l],leftwall)
                
                
            else:
                #right
                r-=1
                if height[r] < rightwall:
                    water += rightwall - height[r]
                rightwall = max (height[r],rightwall)
       
    
        return water
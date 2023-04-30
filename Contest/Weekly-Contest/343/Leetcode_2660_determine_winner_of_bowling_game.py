class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        total1 = 0
        total2 = 0
        player1 = [0] * 2 + player1
        player2 = [0] * 2 + player2
        
        for i in range(2, len(player1)):
            if player1[i - 1] == 10 or player1[i - 2] == 10:
                total1 += 2 * player1[i]
            else:
                total1 += player1[i]
                
        for i in range(2, len(player2)):
            if player2[i - 1] == 10 or player2[i - 2] == 10:
                total2 += 2 * player2[i]
            else:
                total2 += player2[i]
                

                    
        if total1 == total2:
            return 0
        elif total1 > total2:
            return 1
        else:
            return 2
                    
                    
# Time Complexity: O(n)
# Space Complexity: O(1)
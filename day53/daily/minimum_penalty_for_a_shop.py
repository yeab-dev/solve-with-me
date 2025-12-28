class Solution:
    def bestClosingTime(self, customers: str)-> int:
        n = len(customers)
        
        prefix_n = [0] * (n + 1)
        prefix_y = [0] * (n + 1)

        for i in range(1, n+1):
            prefix_n[i] = prefix_n[i-1]
            if customers[i-1] == 'N':
                prefix_n[i] += 1

        for i in range(n, 0, -1):
            prefix_y[i-1] = prefix_y[i]
            if customers[i-1] == 'Y':
                prefix_y[i-1] += 1

        smallest = 0
        minimum = prefix_n[0] + prefix_y[0]
        for i in range(n+1):
            if prefix_n[i] + prefix_y[i] < minimum:
                smallest = i
                minimum = prefix_n[i] + prefix_y[i]
        return smallest
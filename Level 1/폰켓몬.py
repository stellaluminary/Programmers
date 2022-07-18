"""
Method 2

"""
def solution(nums):
    return min(len(set(nums)), len(nums)//2)

"""
Method 1

"""
def solution(nums):
    max_diversity = len(set(nums))
    half_total_poketmons = len(nums) // 2
    answer = half_total_poketmons if half_total_poketmons < max_diversity else max_diversity
    return answer
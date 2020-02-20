class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        outputs = []
        ratings = []
        for i, r, v, p, d in restaurants:
            if veganFriendly and not v:
                continue
            if p > maxPrice:
                continue
            if d > maxDistance:
                continue
            if len(outputs) == 0:
                outputs.append(i)
                ratings.append(r)
            else:
                j = 0
                while j < len(outputs):
                    if r > ratings[j]:
                        outputs.insert(j, i)
                        ratings.insert(j, r)
                        break
                    elif r == ratings[j]:
                        if i > outputs[j]:
                            outputs.insert(j, i)
                            ratings.insert(j, r)
                        else:
                            outputs.insert(j+1, i)
                            ratings.insert(j+1, r)
                        break
                    else:
                        j += 1
                if j == len(outputs):
                    outputs.append(i)
                    ratings.append(r)
        return outputs

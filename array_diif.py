#Implement a difference function, which subtracts one list from another and returns the result.
#It should remove all values from list a, which are present in list b keeping their order.
#Examples (Input --> Output)
#array_diff([1,2],[1]) == [2]
#If a value is present in b, all of its occurrences must be removed from the other:
#array_diff([1,2,2,2,3],[2]) == [1,3]
import codewars_test as test

def array_diff(a, b):
    for item in b:
        while item in a:
            a.remove(item)
    return a

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(array_diff([1,2], [1]), [2], "a was [1,2], b was [1], expected [2]")
        test.assert_equals(array_diff([1,2,2], [1]), [2,2], "a was [1,2,2], b was [1], expected [2,2]")
        test.assert_equals(array_diff([1,2,2], [2]), [1], "a was [1,2,2], b was [2], expected [1]")
        test.assert_equals(array_diff([1,2,2], []), [1,2,2], "a was [1,2,2], b was [], expected [1,2,2]")
        test.assert_equals(array_diff([], [1,2]), [], "a was [], b was [1,2], expected []")
        test.assert_equals(array_diff([1,2,3], [1, 2]), [3], "a was [1,2,3], b was [1, 2], expected [3]")

#fixed_tests()
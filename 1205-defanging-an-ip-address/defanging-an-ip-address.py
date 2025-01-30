class Solution(object):
    def defangIPaddr(self, address):
        new_ad = address.replace(".","[.]")
        return new_ad
        
import java.util.Scanner;

class Solution {
    // This method checks if a number is a palindrome
    public boolean isPalindrome(int number) {
        // Negative numbers cannot be palindromes
        if (number < 0) {
            return false;
        }

        int originalNumber = number;
        int reversedNumber = 0;

        // Reverse the number
        while (number != 0) {
            int digit = number % 10;
            reversedNumber = reversedNumber * 10 + digit;
            number /= 10;
        }

        // Check if the original number is equal to the reversed number
        return originalNumber == reversedNumber;
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = s.nextInt();

        Solution solution = new Solution();
        if (solution.isPalindrome(num)) {
            System.out.println("True");
        } else {
            System.out.println("False");
        }

        s.close();
    }
}

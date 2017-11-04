//Daily Challenge: Write a function that computes the sum of the numbers in a given list using a for-loop

using System;
using System.Collections.Generic;
using System.Linq;

public class Class1
{
    int[] numberList = new[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

    static void Main()
    {
        Console.WriteLine("This is the expected output.");
    }

    public void ForLoopSum()
  {
        for (int i = 0; i < numberList.Length; i++)
        {
            int sum = sum + i;
            Console.WriteLine(i);
        }
    }

}

    




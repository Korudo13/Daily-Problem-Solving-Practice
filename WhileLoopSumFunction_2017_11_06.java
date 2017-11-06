public class WhileLoopSumFunction_2017_11_06 {

    //Write a function that computes the sum of the numbers in a given list using a while-loop
        public static void main(String[] args) {

            System.out.println(forLoopSumFunction());
        }

        public static int forLoopSumFunction(){
            int[] numberList = {1,2,3,4,5,6,7,8,9,10};
            int sum = 1;
            int i = 1;

            while (i < numberList.length){
                i++;
                sum = sum + i;
            }
            return sum;
        }
}

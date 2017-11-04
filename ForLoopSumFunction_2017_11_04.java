public class ForLoopSumFunction_2017_11_04 {

    //Write a function that computes the sum of the numbers in a given list using a for-loop
        public static void main(String[] args) {

            System.out.println(forLoopSumFunction());
        }


        public static int forLoopSumFunction(){
            int[] numberList = {1,2,3,4,5,6,7,8,9,10};
            int sum = 0;

            for(int i=0; i<numberList.length; i++){
                sum += numberList[i];
            }

            return sum;
        }
}

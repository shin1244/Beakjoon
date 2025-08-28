import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        var sc = new Scanner(System.in);
        sc.nextLine(); // 시험장 개수, 여기서는 사용하지 않음
        var rooms = sc.nextLine().split(" ");
        var observer = sc.nextLine().split(" ");
        var mainObserver = Integer.parseInt(observer[0]);
        var subObserver = Integer.parseInt(observer[1]);

        // 결과 값이 int 범위를 넘어갈 수 있으므로 long으로 선언
        long result = 0; 

        for (var room : rooms){
            var people  = Integer.parseInt(room);
            
            // 1. 총감독관은 무조건 1명 필요
            result += 1;

            // 2. 총감독관이 감시한 인원 제외
            people -= mainObserver;

            // 3. 남은 인원이 있을 경우 부감독관 계산 (올림 처리)
            if (people > 0){
                result += (long)Math.ceil((double)people / subObserver);
                // 또는 아래 방법 사용
                // result += (people + subObserver - 1) / subObserver;
            }
        }
        System.out.println(result);
        sc.close();
    }
}
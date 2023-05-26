import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Main {
	static int N;
	static int K;
	static int ans;
	static boolean[] used;
	static int[] kit;
	public static void dfs(int cnt, int weight) {
		if (cnt == N) {
			ans++;
			return;
			
		} else if (weight < 500) {
			return;
		}
		
		for (int i = 0; i < N; i++) {
			if (!used[i]) {
				weight += kit[i];
				used[i] = true;
				dfs(cnt+1, weight-K);
				used[i] = false;
				weight -= kit[i];
			}
		}
	}
	
	public static void main(String args[]) throws Exception	{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		K = Integer.parseInt(st.nextToken());
		used = new boolean[N];
		kit = new int[N];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < N; i++) {
			kit[i] = Integer.parseInt(st.nextToken());
		}

		dfs(0,500);
		
		System.out.println(ans);
		
		}
		
	}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;

public class PatchMethod {

	public static void main(String[] args) throws IOException {
		URL url ;
		String a;		
		try {
			url= new URL("http://imdhanush.herokuapp.com/dcn");
			HttpURLConnection con = (HttpURLConnection) url.openConnection();
			con.setRequestMethod("PATCH");
			//System.out.println(con.getInputStream());
			
			BufferedReader in = new BufferedReader(new InputStreamReader(url.openStream()));
			while((a = in.readLine()) != null)
			{
				System.out.println(a);
			}
			in.close();	
		} catch (MalformedURLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
}

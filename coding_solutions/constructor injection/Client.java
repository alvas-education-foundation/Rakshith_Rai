package coder;

public class Client {
	private Interface service;
	
	public Client(Interface service)
	{
		this.service=service;
	}
	public void call()
	{
		String call=service.sendmessage();
		System.out.println(call);
		
	}
	public static void main(String Args[])
	{
		Interface a2=new ServerA();
		Client a=new Client(a2);
		a.call();
		
	}
	
	
	

}

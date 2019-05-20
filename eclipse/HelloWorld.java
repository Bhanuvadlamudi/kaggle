package simpleapp;

public class HelloWorld {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Hello World!");
		   method1();
	  }
	  public static void method1(){
	    System.out.println("method1");
	    method2();
	  }

	  public static void method2(){
	    System.out.println("method2");
	    String a=null;
	    a.toLowerCase();
	    method3();
	  }

	  public static void method3(){
	    System.out.println("method3");
	  }

}

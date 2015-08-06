package com.born2code.spring.aop;

//import com.born2code.spring.camera.accessories.Lens;
import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class App {
    public static void main(String[] args) {
        ApplicationContext context = new ClassPathXmlApplicationContext("com/born2code/spring/aop/beans.xml");
        Camera camera = (Camera) context.getBean("camera");
//        Car car = (Car) context.getBean("car");
        camera.snap();
        camera.snap(1000);
        camera.snap("hello World");
//        car.start();

        ((ClassPathXmlApplicationContext) context).close();
    }
}

